from match_analyzer.io_utils import load_dataset
from match_analyzer.analysis.models import Match
from match_analyzer.analysis.report import league_report, export_league_report
from match_analyzer.logger import get_logger

log = get_logger(__name__)


def main():
    """
    Huvudfunktion för CLI-verktyget.
    Laddar dataset, skapar rapport och exporterar den.
    """
    # 1. Läs rådata från CSV-fil
    rows = load_dataset("matches.csv")

    # 2. Skapa Match-objekt
    matches = []
    for row in rows:
        match = Match.from_csv_row(row)
        matches.append(match)

    # 3. Skapa rapport
    report_rows = league_report(matches, min_matches=30)

    # 4. Exportera rapport
    export_league_report(report_rows)


if __name__ == "__main__":
    main()