#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any


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


BATCH: list[Any] = [
    'Hello World',
    [3.14, -1, 2.71],
    [
        {'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead!'},
        {'log_level': 'INFO',
         'log_message': 'User K-RALEON is connected'}
    ],
    42,
    ['Hi', 'Five']
]


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)
    print("Send first batch of data on stream:", BATCH)
    ds.process_stream(BATCH)
    ds.print_processors_stats()
    print("\nRegistering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(txt_proc)
    ds.register_processor(log_proc)
    print("Send same batch again")
    ds.process_stream(BATCH)
    ds.print_processors_stats()
    print("\nConsume some elements from the data processors:",
          "Numeric: 3, Text: 2, Log: 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        txt_proc.output()
    log_proc.output()
    ds.print_processors_stats()


if __name__ == '__main__':
    main()
