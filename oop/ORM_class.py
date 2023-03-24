from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


e1 = Employee("Vik", "Technology", 75000)

print(f"{type(e1)} {e1} {e1.name}")
