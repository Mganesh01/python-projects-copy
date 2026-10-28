"""Beginner-friendly examples covering any(), all(), JSON parsing,
copying, and enums."""

from __future__ import annotations

import copy
import json
from enum import Enum


def evaluate_job_eligibility() -> None:
    """Demonstrate the difference between any() and all()."""
    requirements = {
        "python_skills": True,
        "projects": False,
        "communication": True,
        "problem_solving": True,
    }

    print("Eligibility checks:")
    print(f"At least one requirement: {any(requirements.values())}")
    print(f"All requirements satisfied: {all(requirements.values())}")


def parse_json_example() -> None:
    """Load raw JSON text into Python dictionaries and access values."""
    raw_json = """
    {
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age": 25,
        "location": "Hyderabad"
    }
    """
    data = json.loads(raw_json)

    print("JSON keys:", list(data.keys()))
    print("Name:", data["name"])
    print("Email:", data["email"])


def shallow_vs_deep_copy() -> None:
    """Show that deepcopy prevents nested data from being shared."""
    match = {"score": 250, "players": ["Rohit", "Babar"]}
    cloned_match = copy.deepcopy(match)

    cloned_match["score"] = 300
    cloned_match["players"][0] = "Virat"

    print("Original:", match)
    print("Cloned:", cloned_match)


class PaymentStatus(Enum):
    """Represent a small set of payment states."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"


def payment_status_demo() -> None:
    """Convert a string value into an enum and handle invalid values."""
    api_status = "Canceled"

    try:
        status = PaymentStatus(api_status)
        print("Valid payment status:", status)
    except ValueError:
        print("Invalid payment status!")


def movie_list_demo() -> None:
    """Show how append() and pop() work on a list."""
    movies = ["Baashha", "Robo", "Kabali", "Jailer"]
    movies.append("Jailer 2")
    popped_movie = movies.pop()
    print("Movie list:", movies)
    print("Last movie popped:", popped_movie)


if __name__ == "__main__":
    evaluate_job_eligibility()
    parse_json_example()
    shallow_vs_deep_copy()
    payment_status_demo()
    movie_list_demo()


