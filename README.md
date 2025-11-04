# Robot Framework + Selenium + Python Demo

This repository shows a minimal working setup of **Robot Framework** with **Selenium** for browser automation using Python.

This README includes quick setup, examples, test execution and troubleshooting steps so you can get running quickly.

## 🧰 Prerequisites
- Python 3.8 or newer
- pip
- A supported browser:
  - Google Chrome (recommended) or
  - Mozilla Firefox
- The matching WebDriver for your browser on PATH (or configured in your environment):
  - chromedriver for Chrome
  - geckodriver for Firefox

Tip: Use webdriver-manager for automatic driver management (see Installation).

## ⚙️ Installation

1. Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Optional: If you don't want to manage WebDriver binaries manually, install webdriver-manager:
```bash
pip install webdriver-manager
```

## 📁 Repository layout (example)
- tests/ - Robot Framework test suites (*.robot)
- resources/ - shared resource files
- keywords/ - Python keyword libraries (if any)
- requirements.txt - Python dependencies
- README.md - this file

(Adjust these paths if your repo uses a different layout.)

## 🧪 Writing tests

A minimal Robot Framework test file (tests/example.robot):

```robot
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://example.com

*** Test Cases ***
Open Example And Check Title
    Open Browser    ${URL}    chrome
    Title Should Be    Example Domain
    [Teardown]    Close Browser
```

If you use webdriver-manager in a Python keyword library, you can configure browser binaries automatically. Otherwise make sure chromedriver or geckodriver is installed and on PATH.

## ▶️ Running tests

Run all Robot tests in the `tests/` directory:
```bash
robot tests
```

Run a single test file:
```bash
robot tests/example.robot
```

Run using a specific browser (environment variable example):
```bash
# Example using environment variable inside your .robot or resource files
BROWSER=chrome robot tests
```

If you prefer pytest + robotframework integration, you can run Robot tests from Python tooling — but the commands above are the simplest.

## 🧩 Example requirements.txt

A minimal requirements.txt for this repo might include:
```
robotframework>=5.0
robotframework-seleniumlibrary>=6.0
selenium>=4.0
webdriver-manager>=4.0
```

(Adjust versions to match your compatibility needs.)

## 🛠 CI / GitHub Actions (example)

A simple GitHub Actions workflow can run Robot tests in headless Chrome:

```yaml
name: Robot Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run robot tests
        run: |
          # run Chrome in headless mode via capabilities or by setting browser options in tests/ resources
          robot tests
```

Adjust the workflow to install browser binaries or run in a container that already has Chrome.

## 🐞 Troubleshooting

- "chromedriver not found" or similar:
  - Ensure chromedriver is installed and on PATH, or use webdriver-manager to download/manage it automatically.
- Browser version mismatches:
  - Chromedriver must match the installed Chrome version. Update either Chrome or the driver.
- Headless issues:
  - When running in CI, run the browser in headless mode (configure options in your tests or keyword libraries).
- Robot import/library errors:
  - Confirm dependencies are installed in the environment you're running Robot in.

## ✅ Tips & Best Practices

- Put reusable selectors and variables in resource files.
- Keep tests small and focused — one assertion per test where possible.
- Use page object or keyword libraries for complex interactions.
- Run tests locally before pushing to CI to reduce noisy failures.

## Contributing

Contributions are welcome. To contribute:
1. Fork the repository.
2. Create a branch for your feature/fix.
3. Open a pull request with a clear description of the change.

Please include tests for new features where applicable.

## License

Specify your license here (e.g., MIT). If you don't have a license, consider adding one to clarify usage rights.
