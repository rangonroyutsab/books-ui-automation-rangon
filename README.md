# Enterprise UI Automation Framework – Books to Scrape

## Project Overview

This project is a UI automation testing framework for the Books to Scrape website.

Target website:

```text
https://books.toscrape.com/index.html
```


## Features

* Homepage validation
* Page URL and title verification
* Heading visibility validation
* Book section visibility validation
* Random book navigation validation
* Book title verification between homepage and details page
* Book price consistency validation
* Broken link validation
* Product image validation
* Pagination-based image validation
* HTML report generation
* Allure result generation
* Screenshot capture on failure
* Video recording on failure
* Trace retention on failure


## Tech Stack

Python 
Pytest           
Playwright 
GitHub Actions 


## Installation Guide

Clone the repository:

```bash
git clone "https://github.com/rangonroyutsab/books-ui-automation-rangon.git"
cd books-ui-automation-rangon
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```


## Environment Setup

The project uses the following dependencies:

```text
pytest
pytest-playwright
playwright
pytest-html
allure-pytest
requests
python-dotenv
ruff
```

The main Pytest configuration is stored in `pytest.ini`.
The shared Pytest setup is stored in `conftest.py`.


## Running Tests

Run all tests:

```bash
pytest
```

Run tests with live browser view:

```bash
pytest --headed
```

Run tests with live browser view, video on and slow motion:

```bash
pytest --headed --slowmo=300 --video=on
```

Run a specific test file:

```bash
pytest tests/test_homepage.py
```

Run a specific test case:

```bash
pytest tests/test_homepage.py::test_homepage_loads_successfully
```


## Project Structure

```text
books-ui-automation/
│
├── allure-results/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── book_detail_page.py
│   └── home_page.py
│
├── reports/
│
├── test_data/
│   └── constants.py
│
├── test-results/
│
├── tests/
│   ├── __init__.py
│   ├── test_book_data_consistency.py
│   ├── test_book_navigation.py
│   ├── test_broken_links.py
│   ├── test_homepage.py
│   └── test_product_images.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── random_utils.py
│   └── url_utils.py
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Case Coverage

| Test Case                         | File                                  | Coverage                                                       |
| --------------------------------- | ------------------------------------- | -------------------------------------------------------------- |
| Homepage Validation               | `tests/test_homepage.py`              | Validates homepage URL, title, headings, and book section      |
| Random Book Navigation Validation | `tests/test_book_navigation.py`       | Selects 5 random books and verifies details page navigation    |
| Book Data Consistency Validation  | `tests/test_book_data_consistency.py` | Compares homepage book title and price with details page data  |
| Broken Link Validation            | `tests/test_broken_links.py`          | Collects homepage links and verifies successful HTTP responses |
| Product Image Validation          | `tests/test_product_images.py`        | Validates product images and pagination for up to 5 pages      |

## Report Generation Guide

Run the full test suite:

```bash
pytest
```

Generated outputs:

```text
reports/html-report.html
allure-results/
test-results/
```

The `test-results/` folder contains Playwright artifacts such as videos, screenshots, and trace files depending on the configured options.

Current artifact behavior:

```text
Screenshots: only on failure
Videos: retained on failure
Traces: retained on failure
```

## HTML Report Guide

The HTML report is generated using `pytest-html`.

Run:

```bash
pytest
```

HTML report path:

```text
reports/html-report.html
```


## Allure Report Guide

The project uses `allure-pytest` to generate Allure result files.

Run tests:

```bash
pytest
```

Allure results are generated inside:

```text
allure-results/
```

To generate Allure results explicitly:

```bash
pytest --alluredir=allure-results
```

To view the Allure report, the Allure CLI must be installed separately.

Install Allure CLI:

```bash
npm install -g allure-commandline
```

Verify installation:

```bash
allure --version
```

Serve the Allure report:

```bash
allure serve allure-results
```


## GitHub Actions Setup

The GitHub Actions workflow file should be located at:

```text
.github/workflows/playwright.yml
```

Example workflow:

```yaml
name: Playwright Pytest Automation

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Playwright browsers
        run: |
          playwright install --with-deps

      - name: Run automation tests
        run: |
          pytest

      - name: Upload HTML report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: html-report
          path: reports/

      - name: Upload Allure results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: allure-results
          path: allure-results/

      - name: Upload Playwright artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-artifacts
          path: test-results/
```

The workflow runs automatically when code is pushed to the `main` or `master` branch and when a pull request is created for those branches.

## Design Decisions

The framework uses the Page Object Model pattern to separate page-specific locators and actions from test cases.

Test files contain only validation logic, while page classes contain reusable browser interaction methods. This makes the framework easier to maintain and extend.

Reusable helper functions are placed inside the `utils/` directory. This avoids duplicate logic for common tasks such as random item selection and URL normalization.

Reusable test values are placed inside `test_data/constants.py`. This avoids repeated hardcoded values across multiple test files.

Pytest markers are used to organize test cases by category, such as `smoke`, `regression`, `navigation`, `data`, `links`, and `images`.

Playwright's built-in auto-waiting and assertion mechanisms are used instead of hardcoded waits. This improves test stability and reliability.

The framework is configured to generate reports and artifacts automatically so that test execution results can be reviewed locally and in CI/CD.

## Known Limitations

* The tests depend on the public availability of the Books to Scrape website.
* Network issues may affect broken link validation.
* Random book selection may select different books in different test runs.
* Allure report viewing requires Allure CLI to be installed separately.
* Product image validation is limited to a maximum of 5 pages.
* The current framework uses Chromium by default.
