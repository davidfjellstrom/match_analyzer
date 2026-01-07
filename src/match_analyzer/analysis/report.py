from match_analyzer.analysis.metrics import percents_per_league
from match_analyzer.io_utils import save_export
from match_analyzer.logger import get_logger

log = get_logger(__name__)


def league_report(matches, min_matches):
    """
    Skapar och visar en enkel rapport per liga.
    """
    rows = percents_per_league(matches)

    filtered_rows = []
    for row in rows:
        if row["matches"] >= min_matches:
            filtered_rows.append(row)

    # skriv ut i terminal
    print("League".ljust(30), "Matches".rjust(8), "O2.5%".rjust(8), "U2.5%".rjust(8), "BTTS%".rjust(8))
    print("-" * 70)

    for row in filtered_rows:
        print(
            row["league"].ljust(30),
            str(row["matches"]).rjust(8),
            f'{row["over_2_5_pct"]:.2f}'.rjust(8),
            f'{row["under_2_5_pct"]:.2f}'.rjust(8),
            f'{row["btts_pct"]:.2f}'.rjust(8),
        )

    return filtered_rows


def export_league_report(rows, stem="league_report"):
    """
    Tar emot rapport-raderna från metrics,
    sparar dem som en CSV-fil i exports/-mappen
    och returnerar filens sökväg.
    """
    path = save_export(rows, stem=stem)
    log.info(f"Report exported to: {path}")
    return path