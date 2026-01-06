from __future__ import annotations

from match_analyzer.analysis.models import Match


def percent(part: int, total: int) -> float:
    """Returnerar procentandel (0-100) med 2 decimaler."""
    if total == 0:
        return 0.0

    value = (part / total) * 100
    value = round(value, 2)
    return value


def group_by_league(matches: list[Match]) -> dict[str, list[Match]]:
    """Grupperar matcher per liga."""
    grouped: dict[str, list[Match]] = {}

    for match in matches:
        league = match.league

        if league not in grouped:
            grouped[league] = []

        grouped[league].append(match)

    return grouped


def count_over_2_5(matches: list[Match]) -> int:
    """Antal matcher med över 2.5 mål."""
    count = 0

    for match in matches:
        is_over = match.over_2_5_goals()
        if is_over:
            count += 1

    return count


def count_under_2_5(matches: list[Match]) -> int:
    """Antal matcher med under 2.5 mål."""
    count = 0

    for match in matches:
        is_under = match.under_2_5_goals()
        if is_under:
            count += 1

    return count


def count_btts(matches: list[Match]) -> int:
    """Antal matcher där båda lagen gör mål (BTTS)."""
    count = 0

    for match in matches:
        is_btts = match.both_teams_scored()
        if is_btts:
            count += 1

    return count


def percent_over_2_5(matches: list[Match]) -> float:
    """Procent matcher över 2.5 mål."""
    total = len(matches)
    over = count_over_2_5(matches)
    return percent(over, total)


def percent_under_2_5(matches: list[Match]) -> float:
    """Procent matcher under 2.5 mål."""
    total = len(matches)
    under = count_under_2_5(matches)
    return percent(under, total)


def percent_btts(matches: list[Match]) -> float:
    """Procent matcher med BTTS."""
    total = len(matches)
    btts = count_btts(matches)
    return percent(btts, total)


def percents_per_league(matches: list[Match]) -> list[dict[str, object]]:
    """
    Returnerar en lista med dicts per liga:
    - league
    - matches
    - over_2_5_pct
    - under_2_5_pct
    - btts_pct
    """
    grouped = group_by_league(matches)
    rows: list[dict[str, object]] = []

    for league in grouped:
        league_matches = grouped[league]

        league_total = len(league_matches)
        over_pct = percent_over_2_5(league_matches)
        under_pct = percent_under_2_5(league_matches)
        btts_pct = percent_btts(league_matches)

        row = {
            "league": league,
            "matches": league_total,
            "over_2_5_pct": over_pct,
            "under_2_5_pct": under_pct,
            "btts_pct": btts_pct,
        }
        rows.append(row)

    rows.sort(key=lambda r: r["matches"], reverse=True)
    return rows