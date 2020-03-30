from collections import namedtuple
from dataclasses import dataclass

Person = namedtuple('Person', ['name', 'age', 'alive'])
noah = Person('Noah', 19, True)
print(noah)


@dataclass
class Person:
    name: str
    age: int
    alive: bool = True

    @property
    def description(self):
        return f'My name is {self.name} and I am {self.age} years old.'


noah = Person('Noah', 19)  # ưu điểm hơn namedtuple là có thể định nghĩa kiểu dữ liệu và default
print(noah)
print(noah.description)
