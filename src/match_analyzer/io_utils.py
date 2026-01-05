from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Any

from match_analyzer.config import CSV_DELIMITER, DATA_DIR, EXPORT_DIR
from match_analyzer.logger import get_logger

log = get_logger(__name__)


# -----------------------------------------------------------------------
# Hjälpfunktioner för filer och mappar
# -----------------------------------------------------------------------

def ensure_dir(path: Path) -> Path:
    """Skapar en mapp om den inte finns och returnerar samma Path"""
    path.mkdir(parents=True, exist_ok=True)
    return path


def data_path(filename: str) -> Path:
    """Bygger en absolut sökväg till en fil i /data."""
    return DATA_DIR / filename


def export_path(filename: str) -> Path:
    """Bygger en absolut sökväg till en fil i /exports"""
    return EXPORT_DIR / filename


def timestamped_filename(stem: str, suffix: str = ".csv") -> str:
    """Skapar ett filnamn med tidsstämpel"""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{stem}_{ts}{suffix}"


# -----------------------------------------------------------------------
# Läsa / skriva CSV
# -----------------------------------------------------------------------

def read_csv_dicts(path: Path, *, delimiter: str = CSV_DELIMITER, encoding: str = "utf-8") -> list[dict[str, str]]:
    """Läser en CSV och returnerar en lista med dicts (en dict per rad). 
    Nycklarna kommer från header-raden.
    """

    if not path.exists():
        raise FileNotFoundError(f"Hittar inte filen: {path}")

    log.info(f"Läser CSV: {path}")

    with path.open("r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        rows: list[dict[str, str]] = [dict(row) for row in reader]

    log.info(f"Antal rader lästa: {len(rows)}")
    return rows


def write_csv_dicts(
    path: Path,
    rows: list[dict[str, Any]],
    *,
    delimiter: str = CSV_DELIMITER,
    encoding: str = "utf-8",
) -> None:
    """Skriver en lista med dicts till en CSV. Kolumner tas från keys i första raden."""
    ensure_dir(path.parent)

    if not rows: # Tom lista
        log.warning(f"Inga rader att skriva till CSV: {path}")
        return
    
    fieldnames = list(rows[0].keys())

    log.info(f"Skriver CSV: {path} med {len(rows)} rader")

    with path.open("w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(rows)

    log.info("CSV sparad")


def load_dataset(filename: str) -> list[dict[str, str]]:
    """Läser en CSV från data/"""
    return read_csv_dicts(data_path(filename))


def save_export(rows: list[dict[str, Any]], *, stem: str = "export") -> Path:
    """
    Sparar en export i exports/ med tidsstämpel.
    Returnerar sökvägen till filen som skapades.
    """
    ensure_dir(EXPORT_DIR)
    filename = timestamped_filename(stem, ".csv")
    out_path = export_path(filename)
    write_csv_dicts(out_path, rows)
    return out_path