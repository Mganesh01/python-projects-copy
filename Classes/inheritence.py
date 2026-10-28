"""Inheritance examples: single inheritance, multiple inheritance, and MRO."""


class Character:
    """Base class for all game characters."""

    def run(self) -> None:
        print("Character is running.")


class Cop(Character):
    """A police officer inherits from Character."""

    def arrest(self) -> None:
        print("Cop arrested the criminal.")


class Weapon:
    """A second base class for a weapon capability."""

    def shoot(self) -> None:
        print("Shooting.")


class Agent(Character, Weapon):
    """Multiple inheritance combines behavior from more than one base class."""

    pass


class SWAT(Cop):
    """A SWAT officer inherits from Cop, which itself inherits from Character."""

    pass


class PoliceOfficer:
    """A class that overrides a method from a parent class."""

    def run(self) -> None:
        print("Police officer is running.")


class SpecialAgent(Character, PoliceOfficer):
    """Python resolves method conflicts using the method resolution order."""

    pass


if __name__ == "__main__":
    cop = Cop()
    cop.arrest()
    cop.run()

    agent = Agent()
    agent.run()
    agent.shoot()

    swat = SWAT()
    swat.run()

    special_agent = SpecialAgent()
    special_agent.run()
    print(SpecialAgent.mro())

