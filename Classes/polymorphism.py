"""Polymorphism examples: same method name, different behavior."""


class Barbarian:
    """A melee fighter."""

    def attack(self) -> None:
        print("Barbarian attacks with a sword.")


class Archer:
    """A ranged fighter."""

    def attack(self) -> None:
        print("Archer attacks with arrows.")


class Character:
    """Base behavior that may be overridden by child classes."""

    def reaction(self) -> None:
        print("Common reaction.")


class Amrutham(Character):
    """Override the parent reaction method."""

    def reaction(self) -> None:
        print("Amrutham: Are you ready for a workout?")


class Appaji(Character):
    """Override the parent reaction method with different output."""

    def reaction(self) -> None:
        print("Appaji: Start with a small investment.")


class Business:
    """A method whose behavior changes based on the arguments provided."""

    def start_business(self, idea: str, investment: int = 0) -> None:
        if investment:
            print(f"Starting {idea} business with {investment} investment.")
        else:
            print(f"Starting {idea} business.")


if __name__ == "__main__":
    barbarian = Barbarian()
    archer = Archer()
    barbarian.attack()
    archer.attack()

    amrutham = Amrutham()
    appaji = Appaji()
    amrutham.reaction()
    appaji.reaction()

    business = Business()
    business.start_business("Food")
    business.start_business("Food", 50000)


