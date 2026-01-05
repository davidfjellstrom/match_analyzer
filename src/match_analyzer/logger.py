from __future__ import annotations

import logging
from pathlib import Path
from match_analyzer.config import PROJECT_ROOT

# ---------------------------------------------------------
# Cache för skapade loggers
# ---------------------------------------------------------
# Syfte:
# - Se till att man inte skapar samma logger flera gånger
# - Undviker dubbla loggar i terminal och fil
_LOGGERS: dict[str, logging.Logger] = {}


def _ensure_log_dir() -> Path:
    """Create a log directory if it doesn't exist"""
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    return log_dir


def get_logger(name: str = "match_analyzer", level: int = logging.INFO) -> logging.Logger:
    """
    Create or reuse a configured logger.
    Logs to both console and a file in ./logs/
    Prevents duplicate handlers if called multiple times
    """
    if name in _LOGGERS:
        return _LOGGERS[name]
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False # Avoid double logging

    # Avoid adding handlers multiple times
    if not logger.handlers:
        log_dir = _ensure_log_dir()
        log_file = log_dir / f"{name}.log"

        fmt = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(fmt)

        # File handler
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(level)
        fh.setFormatter(fmt)

        logger.addHandler(ch)
        logger.addHandler(fh)

    _LOGGERS[name] = logger
    return logger


# Hjälpfunktioner för loggning med olika nivåer (debug, info, warning, error)
def log_debug(message: str, *, logger: logging.Logger | None = None) -> None:
    (logger or get_logger()).debug(message)


def log_info(message: str, *, logger: logging.Logger | None = None) -> None:
    (logger or get_logger()).info(message)


def log_warning(message: str, *, logger: logging.Logger | None = None) -> None:
    (logger or get_logger()).warning(message)


def log_error(message: str, *, logger: logging.Logger | None = None) -> None:
    (logger or get_logger()).error(message)


def log_exception(message: str, *, logger: logging.Logger | None = None) -> None:
    """Log an error including stack trace (use inside except-blocks)."""
    (logger or get_logger()).exception(message)