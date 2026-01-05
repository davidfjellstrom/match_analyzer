from pathlib import Path


# ==========================================================================
# Project paths
# ==========================================================================
PROJECT_ROOT = Path(__file__).resolve().parents[2]


SRC_DIR = PROJECT_ROOT / "src"
EXPORT_DIR = PROJECT_ROOT / "exports"
DATA_DIR = PROJECT_ROOT / "data"



# ==========================================================================
# General configuration
# ==========================================================================
DATE_FORMAT = "%Y-%m-%d"
CSV_DELIMITER = ","