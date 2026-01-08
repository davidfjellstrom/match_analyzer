from match_analyzer.analysis.metrics import percents_per_league
from match_analyzer.io_utils import save_export, save_text_export
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


from datetime import datetime


def export_league_report_txt(rows, stem="league_report", source=""):
    """
    Exporterar även ligarapporten som en textfil. 
    CSV rapportens roll är "data output", och TXT rapporten är för "human readable summary".
    """

    lines = []
    lines.append("=" * 70)
    lines.append("Match Analyzer – League Report")
    lines.append("=" * 70)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if source:
        lines.append(f"Data Source: {source}")
    lines.append("")

    lines.append("-" * 70)
    lines.append("League Summary")
    lines.append("-" * 70)
    lines.append("")

    if not rows:
        lines.append("No leagues matched the filter.")
        lines.append("")
    else:
        for row in rows:
            lines.append(f"League: {row['league']}")
            lines.append(f"Matches: {row['matches']}")
            lines.append("")
            lines.append(f"Over 2.5 goals:   {row['over_2_5_pct']:.2f} %")
            lines.append(f"Under 2.5 goals:  {row['under_2_5_pct']:.2f} %")
            lines.append(f"BTTS:             {row['btts_pct']:.2f} %")
            lines.append("")
            lines.append("-" * 70)
            lines.append("")

    lines.append("=" * 70)

    path = save_text_export(lines, stem=stem)
    log.info(f"TXT report exported to: {path}")
    return path