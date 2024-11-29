from abc import ABC, abstractmethod

# Прокси
class RealSubject:
    def request(self) -> str:
        return "Реальный субъект: обработка запроса"

class Proxy(ABC):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    @abstractmethod
    def request(self) -> str:
        pass

class ConcreteProxy(Proxy):
    def request(self) -> str:
        print("прокси: проверка перед передачей запроса.")
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        else:
            return "прокси: доступ запрещен."

    def check_access(self) -> bool:
        print("прокси: проверка доступа.")
        return True

    def log_access(self):
        print("прокси: логирование доступа.")

# Мост
class Implementor(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementorA(Implementor):
    def operation_implementation(self) -> str:
        return "реализация A"

class ConcreteImplementorB(Implementor):
    def operation_implementation(self) -> str:
        return "реализация B"

class Abstraction(ABC):
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    @abstractmethod
    def operation(self) -> str:
        pass

class RefinedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"абстракция с {self._implementor.operation_implementation()}"

# Адаптер
class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

class Adaptee:
    def specific_request(self) -> str:
        return "метод специфического запроса"

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self) -> str:
        return f"адаптированный запрос: {self._adaptee.specific_request()}"

# Main функция
def main():
    # Паттерн Прокси
    print("Паттерн Прокси:")
    real_subject = RealSubject()
    proxy = ConcreteProxy(real_subject)
    print(proxy.request())

    # Паттерн Мост
    print("Паттерн Мост:")
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    abstraction1 = RefinedAbstraction(implementor_a)
    abstraction2 = RefinedAbstraction(implementor_b)

    print(abstraction1.operation())
    print(abstraction2.operation())

    # Паттерн Адаптер
    print("Паттерн Адаптер:")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())

if __name__ == "__main__":
    main()
