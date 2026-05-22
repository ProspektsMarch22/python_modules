#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._ingested: list[tuple[int, str]] = []
        self._total_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._ingested.pop(0)

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_total(self) -> int:
        return self._total_count

    def get_remaining(self) -> int:
        return len(self._ingested)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self._registered: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._registered.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            validated: bool = False
            for proc in self._registered:
                if proc.validate(element):
                    proc.ingest(element)
                    validated = True
                    break
            if not validated:
                print("Data Stream Error",
                      f"- Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream Statistics ==")
        if len(self._registered) == 0:
            print("No processor found, no data")
            return
        for proc in self._registered:
            print(f"{proc.get_name()}:",
                  f"total {proc.get_total()} items processed,",
                  f"remaining {proc.get_remaining()} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        ...


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return (type(data) is int
                    or type(data) is float)
        else:
            return all(isinstance(item, (int, float)) for item in data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if (type(data) is list):
            for item in data:
                self._ingested.append((self._total_count, str(item)))
                self._total_count += 1
        else:
            self._ingested.append((self._total_count, str(data)))
            self._total_count += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return (type(data) is str)
        else:
            return all(type(item) is str for item in data)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if type(data) is list:
            for item in data:
                self._ingested.append((self._total_count, item))
                self._total_count += 1
        elif type(data) is str:
            self._ingested.append((self._total_count, data))
            self._total_count += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            return (all(isinstance(k, str) for k in data.keys())
                    and all(isinstance(v, str) for v in data.values()))
        elif type(data) is list:
            return (all(type(item) is dict
                    and all(isinstance(k, str) for k in item.keys())
                    and all(isinstance(v, str) for v in item.values())
                    for item in data))
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if type(data) is list:
            for item in data:
                self._ingested.append((self._total_count,
                                      ": ".join(v for v in item.values())))
                self._total_count += 1
        elif type(data) is dict:
            self._ingested.append((self._total_count,
                                  ": ".join(v for v in data.values())))
            self._total_count += 1
