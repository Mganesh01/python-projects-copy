"""Encapsulation examples showing controlled access to private data."""


class Professor:
    """Demonstrate encapsulation by hiding internal data."""

    def __init__(self, secret_plan: str) -> None:
        self.__secret_plan = secret_plan

    def get_secret_plan(self) -> str:
        """Expose data only through a controlled method."""
        return self.__secret_plan


class SecuritySystem:
    """Only allow access when a valid password is provided."""

    def __init__(self, secret_code: str) -> None:
        self.__secret_code = secret_code

    def reveal_code(self, password: str) -> str:
        if password == "1234":
            return self.__secret_code
        return "Access denied."


if __name__ == "__main__":
    professor = Professor("Bank heist plan")
    print(professor.get_secret_plan())

    secure_system = SecuritySystem("Alpha-42")
    print(secure_system.reveal_code("1234"))
    print(secure_system.reveal_code("0000"))

