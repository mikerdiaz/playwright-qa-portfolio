markdown
# Playwright QA Portfolio

End-to-end test automation framework built with Playwright and Python,
targeting real-world QA scenarios for job-ready portfolio demonstration.

## Tech Stack

- Python 3.13
- Playwright
- Pytest
- pytest-html
- Page Object Model (POM)
- GitHub Actions CI/CD

## Project Structure

```
playwright-qa-portafolio/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
├── reports/
│   └── report.html
├── screenshots/
│   ├── login_success.png
│   ├── login_failed.png
│   └── add_to_cart.png
├── tests/
│   ├── test_google.py
│   └── test_saucedemo.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Cases

### Google Tests
- Google title validation
- Google search functionality

### SauceDemo Tests
- Successful login with valid credentials
- Failed login with invalid credentials
- Add product to cart and verify cart count

## How to Run

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## CI/CD

Tests run automatically on every push to main via GitHub Actions.

## Author

Mike Diaz – QA Automation Engineer
Vancouver, BC, Canada
github.com/mikerdiaz