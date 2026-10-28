"""Examples showing zip(), recursion, linked-list style nodes, and
read-only mapping dictionaries."""

from __future__ import annotations

from types import MappingProxyType


def pair_movies_and_years() -> None:
    """Match values from two lists using zip()."""
    movies = ["Indra", "Tagore", "Khaidi No. 150"]
    years = [2002, 2003, 2017]

    for movie, year in zip(movies, years):
        print(f"{movie} -> {year}")


def countdown(value: int) -> None:
    """Example of recursion with a countdown."""
    if value <= 0:
        print("Action!")
        return

    print(value)
    countdown(value - 1)


class Node:
    """A simple linked-list node demonstrating object references."""

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None


def create_linked_list() -> None:
    """Build a short linked list and traverse it."""
    rohit = Node("Rohit")
    virat = Node("Virat")
    surya = Node("Surya")

    rohit.next = virat
    virat.next = surya

    current = rohit
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def mapping_proxy_demo() -> None:
    """Use a read-only dictionary view with MappingProxyType."""
    wrestlers = {"Undertaker": "Deadman", "Cena": "Never Give Up"}
    read_only = MappingProxyType(wrestlers)

    print("Read-only mapping:", read_only)
    # read_only["Cena"] = "GOAT"  # This would raise TypeError


if __name__ == "__main__":
    pair_movies_and_years()
    countdown(3)
    create_linked_list()
    mapping_proxy_demo()
