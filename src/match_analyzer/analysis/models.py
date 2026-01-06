from __future__ import annotations

from datetime import date


class Match:
    """Representerar en matchrad från CSV.
    
    Förväntande kolumner i CSV:
    - league
    - date (YYYY-MM-DD)
    - home_team
    - away_team
    - home_goals
    - away_goals
    """

    def __init__(
        self,
        league: str,
        match_date: date,
        home_team: str,
        away_team: str,
        home_goals: int,
        away_goals: int,
    ) -> None:
        self.league = league
        self.match_date = match_date
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals


    @classmethod
    def from_csv_row(cls, row: dict[str, str]) -> Match:
        """Skapar en Match-instans från en CSV-rad (dict)"""
        league = row["league"]
        match_date = date.fromisoformat(row["date"])
        home_team = row["home_team"]
        away_team = row["away_team"]
        home_goals = int(row["home_goals"])
        away_goals = int(row["away_goals"])
        return cls(league, match_date, home_team, away_team, home_goals, away_goals)


    def total_goals(self) -> int:
        """Returnerar totalt antal mål i matchen"""
        return self.home_goals + self.away_goals
        

    def both_teams_scored(self) -> bool:
        """Returnerar True om båda lagen gjort mål"""
        if self.home_goals > 0 and self.away_goals > 0:
            return True
        else:
            return False


    def over_2_5_goals(self) -> bool:
        """Returnerar True om matchen har 3 mål eller fler totalt."""
        if self.total_goals() >= 3:
            return True
        else:
            return False
        

    def under_2_5_goals(self) -> bool:
        """Returnerar True om match har 0, 1 eller 2 mål totalt."""
        if self.total_goals() <= 2:
            return True
        else:
            return False