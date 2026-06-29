# Books UI Automation Project

## Project Overview

This project contains automated UI tests for the [Books to Scrape](https://books.toscrape.com/index.html) website using **Python**, **Pytest**, and **Playwright**.


Target website:

```text
https://books.toscrape.com/index.html
```
Published Allure Report:

**[https://rangonroyutsab.github.io/books-ui-automation-rangon/](https://rangonroyutsab.github.io/books-ui-automation-rangon/)**


---

## Features

The project covers the main user-facing parts of the Books to Scrape website.

Current test coverage includes:

* Homepage loading and URL validation
* Page title verification
* Homepage heading visibility
* Book section visibility
* Random book navigation from homepage to details page
* Book title matching between homepage and details page
* Book price consistency checking
* Broken link validation
* Product image validation
* Pagination-based image checking
* HTML report generation
* Allure result generation
* Screenshot, video, and trace retention for failed tests

---

## Tech Stack

This project uses:

```text
Python
Pytest
Playwright
pytest-html
allure-pytest
GitHub Actions
```

---

## Installation

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

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Dependencies

The project uses the following main dependencies:

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

The main Pytest settings are stored in:

```text
pytest.ini
```

Shared test configuration and Playwright setup are stored in:

```text
conftest.py
```

---

## Running the Tests

Run all tests:

```bash
pytest
```

Run tests with the browser visible:

```bash
pytest --headed
```

Run tests with browser view, video enabled, and slow motion:

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

---

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

---

## Test Case Coverage

| Test Area             | File                                  | What It Checks                                                              |
| --------------------- | ------------------------------------- | --------------------------------------------------------------------------- |
| Homepage validation   | `tests/test_homepage.py`              | Checks homepage URL, title, heading, and book section                       |
| Book navigation       | `tests/test_book_navigation.py`       | Opens random books and verifies details page navigation                     |
| Book data consistency | `tests/test_book_data_consistency.py` | Compares book title and price between homepage and details page             |
| Broken links          | `tests/test_broken_links.py`          | Collects homepage links and checks whether they return successful responses |
| Product images        | `tests/test_product_images.py`        | Checks product images across multiple listing pages                         |

---

## Report Generation

Run the test suite:

```bash
pytest
```

After the test run, the following outputs may be generated:

```text
reports/html-report.html
allure-results/
test-results/
```

The `test-results/` folder stores Playwright artifacts such as screenshots, videos, and trace files depending on the test result and configuration.

Current artifact behavior:

```text
Screenshots: captured on failure
Videos: retained on failure
Traces: retained on failure
```

---

## HTML Report

The HTML report is generated using `pytest-html`.

Run:

```bash
pytest
```

Report path:

```text
reports/html-report.html
```

Open the file in a browser to view the test summary.

---

## Allure Report

This project also supports Allure result generation using `allure-pytest`.

Run tests normally:

```bash
pytest
```

Allure result files are generated inside:

```text
allure-results/
```

To generate Allure results explicitly:

```bash
pytest --alluredir=allure-results
```

To view the Allure report, the Allure CLI needs to be installed separately.

Install Allure CLI:

```bash
npm install -g allure-commandline
```

Check the installation:

```bash
allure --version
```

Serve the report:

```bash
allure serve allure-results
```

---

## GitHub Actions

The GitHub Actions workflow file is located at:

```text
.github/workflows/playwright.yml
```

The workflow runs the automation tests when code is pushed to the `main` or `master` branch, and also when a pull request is created for those branches.



---

## Design Choices

Page Object Model pattern has been used to keep the tests easier to read and maintain.

The test files mainly contain the validation steps, while the page classes inside the `pages/` folder contain selectors and reusable browser actions. This makes the tests cleaner because the same page methods can be reused in multiple test cases.

Common helper functions are kept inside the `utils/` folder. For example, URL-related logic and random item selection are separated from the test files to avoid repeating the same code.

Reusable values such as the base URL are stored inside:

```text
test_data/constants.py
```

This keeps the test files simpler and avoids hardcoding the same value in multiple places.


Playwright’s built-in waiting behavior is used instead of adding hardcoded sleep statements. This helps make the tests more stable.

---

## Known Limitations

* The tests depend on the public Books to Scrape website being available.
* Broken link tests may be affected by network issues or temporary server problems.
* Random book selection may choose different books in different test runs.
* Product image validation is currently limited to a maximum of 5 pages.
* Allure report viewing requires the Allure CLI to be installed separately.
* The current setup uses Chromium by default.

---

## Author 

Rangon Roy Utsab
