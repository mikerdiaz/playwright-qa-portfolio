markdown

# Playwright QA Portfolio

End-to-end test automation framework built with Playwright and Python,
targeting real-world QA scenarios for job-ready portfolio demonstration.

## Tech Stack

- Python 3.13
- Playwright
- Pytest
- Page Object Model (POM)

## Project Structure
playwright-qa-portafolio/
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_google.py
│   └── test_saucedemo.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## Test Cases

### Google Tests
- Google title validation
- Google search functionality

### SauceDemo Tests
- Successful login with valid credentials
- Failed login with invalid credentials (error message validation)

## How to Run

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v
```

## Author

Mike Diaz – QA Automation Engineer
Vancouver, BC, Canada
github.com/mikerdiaz