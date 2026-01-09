from match_analyzer.io_utils import load_dataset
from match_analyzer.analysis.models import Match
from match_analyzer.analysis.report import league_report, export_league_report, export_league_report_txt
from match_analyzer.logger import get_logger

log = get_logger(__name__)


DATASET_MENU = {
    "1": ("Premier League (Dec 2025)", "premier_league_dec_2025.csv", "premier_league_dec_2025"),
    "2": ("Serie A (Dec 2025)", "serie_a_dec_2025.csv", "serie_a_dec_2025"),
    "3": ("La Liga (Dec 2025)", "la_liga_dec_2025.csv", "la_liga_dec_2025"),
}


def safe_input(prompt: str):
    """
    - Läser input på ett säkert sätt.
    - Returnerar en sträng eller None om användaren avbröt (Ctrl+C eller Ctrl+D).
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
    
    
def get_menu_choice() -> str:
    """
    Validerar menyval för CLI:t.
    Loopar tills användaren anger ett giltigt val (1/2/3/q) eller avbryter.
    """
    while True:
        choice = safe_input("Välj alternativ (1, 2, 3 eller q): ")

        if choice is None:
            print("\nAvslutar...\n")
            raise SystemExit(0)

        choice = choice.strip().lower()

        # Endast giltiga menyval
        if choice in ["1", "2", "3", "q"]:
            return choice

        print("Ogiltigt val. Välj 1, 2, 3 eller q.")


def interactive_pick_file() -> tuple[str, str, str]:
    print("\nWelcome to Match Analyzer\n")
    for key, (label, _, _) in DATASET_MENU.items():
        print(f"{key}) Generate report for {label}")
    print("\nq) Quit\n")

    while True:
        choice = get_menu_choice()

        if choice == "q":
            raise SystemExit(0)

        if choice in DATASET_MENU:
            label, filename, stem = DATASET_MENU[choice]
            log.info("Valde dataset: %s (%s)", label, filename)
            return filename, stem, label

        print("Ogiltigt val. Välj 1, 2, 3 eller q.")


def run_report(file_arg: str, min_matches: int, no_export: bool, stem: str) -> None:
    # 1) Läs rådata
    rows = load_dataset(file_arg)
    log.info("Rader i dataset: %s", len(rows))

    # 2) Skapa Match-objekt
    matches = []
    for row in rows:
        matches.append(Match.from_csv_row(row))

    log.info("Antal matcher som används i analys: %s", len(matches))

    # 3) Skapa rapport
    report_rows = league_report(matches, min_matches=min_matches)
    log.info("Antal ligor i rapport (efter filter): %s", len(report_rows))

    # 4) Exportera rapport
    if no_export:
        log.info("Export avstängd (--no-export).")
        return

    csv_path = export_league_report(report_rows, stem=stem)
    txt_path = export_league_report_txt(report_rows, stem=stem, source=file_arg)

    print(f"\nCSV export klar: {csv_path}")
    print(f"TXT export klar: {txt_path}\n")


def main() -> None:
    file_arg, stem, _label = interactive_pick_file()
    # Startpunkt för programmet
    # Användaren väljer vilket dataset som ska analyseras, därefter körs analysen och rapport genereras.
    run_report(
        file_arg=file_arg,
        min_matches=30,
        no_export=False,
        stem=stem,
    )


if __name__ == "__main__":
    main()
