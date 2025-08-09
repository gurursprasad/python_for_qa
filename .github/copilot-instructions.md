# Copilot Instructions for python_for_qa

## Project Overview
- This repository is a modular, topic-based Python learning resource for QA professionals and interview preparation.
- Each numbered directory (e.g., `01_getting_started/`, `02_language_fundamentals/`, etc.) covers a specific Python topic, with a dedicated `README.md` and example scripts.
- The root `README.md` provides a table of contents and learning roadmap.

## Architecture & Structure
- **Each topic = one directory**: All code, notes, and exercises for a topic are grouped together.
- **No central application**: This is not a monolithic app, but a collection of focused learning modules.
- **Naming conventions**: Directories and files are prefixed with numbers for ordering (e.g., `02_language_fundamentals/01_python_identifiers.py`).
- **README-driven**: Every topic directory contains a `README.md` with explanations, examples, and learning objectives.

## Developer Workflows
- **No build step required**: Run scripts directly with `python3 <script.py>`.
- **Testing**: If present, tests are typically in the same directory as the topic. Use `pytest` for any test files.
- **Virtual environment**: Use `python3 -m venv venv` and `pip install -r requirements.txt` to manage dependencies.
- **Requirements**: All dependencies are listed in the root `requirements.txt`.

## Project-Specific Patterns
- **Educational focus**: Code is written for clarity and learning, not production. Prefer explicit, readable code over clever tricks.
- **Section isolation**: Avoid cross-imports between topic directories unless demonstrating a specific concept.
- **Consistent file structure**: Example: `02_language_fundamentals/01_python_identifiers.py` always matches the topic and order in the README.

## Integration & Dependencies
- **External libraries**: All required libraries are in `requirements.txt`. If a version fails, prefer the latest available version.
- **No external services**: All code runs locally; no cloud or network dependencies unless explicitly stated in a topic.

## Examples
- To run an example: `python3 02_language_fundamentals/01_python_identifiers.py`
- To install dependencies: `pip install -r requirements.txt`
- To run tests (if present): `pytest <test_file.py>`

## Key Files & Directories
- `README.md` (root): Project overview and navigation
- `requirements.txt`: All dependencies
- `01_getting_started/`, `02_language_fundamentals/`, ...: Topic modules
- Each topic's `README.md`: Learning objectives and code examples

---

For new topics, follow the existing directory and README structure. Prioritize clarity and educational value in all code and documentation.
