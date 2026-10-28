"""Abstraction example using abstract base classes in Python."""

from abc import ABC, abstractmethod


class Scoreboard(ABC):
    """A common interface that all scoreboards must implement."""

    @abstractmethod
    def show_score(self) -> None:
        """Display the current score."""


class IPLScoreboard(Scoreboard):
    """Concrete scoreboard for cricket match statistics."""

    def __init__(self, team: str, runs: int, wickets: int, overs: float) -> None:
        self.team = team
        self.runs = runs
        self.wickets = wickets
        self.overs = overs

    def show_score(self) -> None:
        print("🏏 IPL SCOREBOARD")
        print("----------------------")
        print(f"Team   : {self.team}")
        print(f"Score  : {self.runs}/{self.wickets}")
        print(f"Overs  : {self.overs}")
        print("----------------------")


class MatchScore(Scoreboard):
    """A scoreboard that calculates score details internally."""

    def __init__(self) -> None:
        self.runs = 0
        self.wickets = 0
        self.balls = 0

    def _calculate_score(self, runs: int) -> None:
        self.runs += runs

    def _validate_wicket(self) -> None:
        if self.wickets < 10:
            self.wickets += 1
        else:
            print("All wickets are already lost!")

    def _calculate_over(self) -> str:
        overs = self.balls // 6
        balls = self.balls % 6
        return f"{overs}.{balls}"

    def _process_ball(self, runs: int, wicket: bool = False) -> None:
        self._calculate_score(runs)
        if wicket:
            self._validate_wicket()
        self.balls += 1

    def show_score(self) -> None:
        print("\n🏏 MATCH SCOREBOARD")
        print("-------------------------")
        print(f"Score : {self.runs}/{self.wickets}")
        print(f"Overs : {self._calculate_over()}")
        print("-------------------------")


if __name__ == "__main__":
    scoreboard = IPLScoreboard("CSK", 185, 6, 20.0)
    scoreboard.show_score()

    match = MatchScore()
    for runs, wicket in [(4, False), (1, False), (6, False), (0, True), (2, False), (1, False)]:
        match._process_ball(runs, wicket)
    match.show_score()

