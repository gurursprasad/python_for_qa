# Getting Started

This guide will help you set up Python for QA automation on Windows, macOS, and Linux. It covers Python installation, setting up a virtual environment, and installing dependencies from a `requirements.txt` file.

---

## 1. Install Python

### Windows
- Download Python from the [official website](https://www.python.org/downloads/windows/).
- Run the installer and **check the box** that says "Add Python to PATH".
- Complete the installation.
- Verify installation:
  ```bash
  python --version
  ```

### macOS
- Open Terminal and run:
  ```bash
  brew install python3
  ```
- Or download from the [official website](https://www.python.org/downloads/mac-osx/).
- Verify installation:
  ```bash
  python3 --version
  ```

### Linux (Ubuntu/Debian)
- Open Terminal and run:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```
- Verify installation:
  ```bash
  python3 --version
  ```

---

## 2. Set Up a Virtual Environment

A virtual environment keeps your project dependencies isolated.

### Create a Virtual Environment

- **Windows:**
  ```bash
  python -m venv .venv
  ```
- **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  ```

### Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

---


## 3. About pip & Installing Dependencies

`pip` is Python's package installer. It allows you to install and manage additional libraries and dependencies that are not part of the Python standard library.

- To check if pip is installed:
  ```bash
  pip --version
  ```
  or (on some systems):
  ```bash
  python3 -m pip --version
  ```

- To install a single package:
  ```bash
  pip install package_name
  ```

If you have a `requirements.txt` file, you can install all dependencies listed in it with:

```bash
pip install -r requirements.txt
```

> **Note:** Always activate your virtual environment before installing packages or running scripts.

---

## 4. Deactivate the Virtual Environment

When done, deactivate with:

```bash
deactivate
```

---

## 5. Additional Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)

---

You are now ready to start working on the Python for QA project!
