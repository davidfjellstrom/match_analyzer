# Match Analyzer

Match Analyzer is a terminal-based Python tool for analyzing football matches using CSV data.
The program reads match data, performs basic statistical analysis, and generates summary reports
that are printed to the terminal and exported as files.

The project is built with a focus on clear project structure, modular code, configurable path handling,
and simple execution from the command line.

---

## Features

The program can, among other things:

- Read match data from CSV files
- Process and analyze match results
- Generate reports and export results to files
- Log events using different log levels
- Run via a menu-based CLI interface

---

## Installation

Follow the steps below to install the project. The instructions are compatible with macOS, Linux, and Windows.

1. Clone the repository and enter the project directory:

git clone https://github.com/davidfjellstrom/match_analyzer.git
cd match_analyzer

2. Create and activate a virtual environment.

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

Windows (PowerShell):
py -m venv .venv
.venv\Scripts\Activate.ps1

3. Install the project in editable mode:

pip install -e .

This installs the project locally and registers the `match_analyzer` CLI command.

---

## Running the Program


Run the program using the CLI entrypoint (recommended and OS-independent):

match_analyzer

Alternatively, run the program as a Python module:

macOS / Linux:
python3 -m match_analyzer

Windows:
py -m match_analyzer

Note: On some systems (such as macOS), the `python` command may not exist. In those cases, `python3` should be used instead.

When the program starts, a menu will be displayed where you can select which analysis or report to run.
Generated files are saved in the `exports/` directory.

---

## Project Structure (Overview)

```
match_analyzer/
├── data/                # Input CSV data
├── exports/             # Generated reports and exports
├── src/
│   └── match_analyzer/
│       ├── analysis/    # Analysis and calculation logic
│       ├── cli.py       # Menu and user interaction
│       ├── config.py    # Central paths and configuration
│       ├── io_utils.py  # File handling and CSV IO
│       ├── logger.py    # Custom logger
│       └── __main__.py  # Entrypoint
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

## Design Choices

To keep the project easy to follow, several related tasks (like file handling and exporting) are collected in the io_utils.py file.

In a bigger project, this would probably be divided into multiple modules.
---

## Logging

The project uses a custom logger with support for multiple log levels
(information, warnings, and errors). Logging is used consistently throughout
the application to improve traceability and simplify debugging.

---

## Dependencies

The project uses only Python’s standard library.
All dependencies are listed in `requirements.txt` and `pyproject.toml`.

---

## Version Control

The project is version-controlled using Git and developed with feature branches.

The final version is available as a public GitHub repository.
