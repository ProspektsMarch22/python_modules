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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    num_proc = NumericProcessor()
    print("\nTesting Numeric Processor")
    print(" Trying to validate input '42':", num_proc.validate(42))
    print(" Trying to validate input 'Hello':", num_proc.validate('Hello'))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest('foo')  # This raises an unavoidable mypy error
        print("Something went wrong :[")
    except TypeError as e:
        print("Got exception:", e)
    data_num: list[int | float] = [1, 2, 3, 4, 5]
    print("Processing data:", data_num)
    num_proc.ingest(data_num)
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}:", num_proc.output()[1])
    print("\nTesting Text Processor")
    txt_proc = TextProcessor()
    print(" Trying to validate input '42':", txt_proc.validate(42))
    data_txt: list[str] = ['Hello', 'Nexux', 'World']
    print("Processing data:", data_txt)
    txt_proc.ingest(data_txt)
    print("Extracting 1 value...")
    print("Text value 0:", txt_proc.output()[1])
    print("\nTesting Log Processor")
    log_proc = LogProcessor()
    print(" Trying to validate input 'Hello':", log_proc.validate('Hello'))
    data_log: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to Server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized Access!!'}
    ]
    print("Processing data: ", data_log)
    log_proc.ingest(data_log)
    print("Extracting 2 values...")
    for i in range(2):
        print(f"Log entry {i}:", log_proc.output())


if __name__ == '__main__':
    main()
