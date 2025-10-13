# AGENT CODING GUIDELINES

## 1. Commands

| Action | Command | Notes |
| :--- | :--- | :--- |
| **Install** | `pip install -r requirements.txt` | |

## 2. Code Style

### General
- **Language:** Python 3.10+ (due to `match` statement usage).
- **Indentation:** 4 spaces.

### Imports
- Follow **PEP 8** (Standard library, then third-party, then local imports).
- Separate import groups with a blank line.

### Naming Conventions
- **Functions/Variables:** `snake_case`.
- **Internal Functions:** Prefix with a single underscore (`_`).

### Types
- **Type Hints:** Not currently used, but highly encouraged for new code.

### Error Handling
- **Exceptions:** Catch specific exceptions, not bare `except:`.
- **Logging:** Use standard Python `logging` module for errors.
