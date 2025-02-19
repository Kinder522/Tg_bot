class MyClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def get_a(self) -> int:
        return self.a

    def set_a(self, a: int):
        self.a = a

    def get_b(self) -> str:
        return self.b

    def set_b(self, b: str):
        self.b = b


def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number


m = MyClass(3, "heLLo")
print(say_something(m.get_a(), m.get_b()))
m.set_a("dsa")
m.set_b("TRY")
print(say_something(m.get_a(), m.get_b()))
