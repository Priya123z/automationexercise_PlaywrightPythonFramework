# 🎭 Automation Exercise - Playwright Python Framework

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)]()
[![PyTest](https://img.shields.io/badge/PyTest-Test%20Framework-orange.svg)]()
[![Allure](https://img.shields.io/badge/Allure-Reports-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)]()

## 📌 Overview

Automation Exercise Playwright Python Framework is an enterprise-grade End-to-End Test Automation Framework built using **Python**, **Playwright**, and **PyTest** following the **Page Object Model (POM)** design pattern.

The framework is designed to automate user workflows on the Automation Exercise application with a focus on:

* Scalability
* Reusability
* Maintainability
* Parallel Execution
* Rich Reporting
* CI/CD Readiness

---

## 🚀 Key Features

✅ Page Object Model (POM) Architecture

✅ Data-Driven Testing

✅ PyTest Fixtures

✅ Cross-Browser Execution

✅ Parallel Execution

✅ Screenshot Capture on Failure

✅ Logging and Reporting

✅ Allure Reports

✅ HTML Reports

✅ Headless Execution

✅ Environment Configuration

✅ Reusable Utilities and Helper Methods

✅ CI/CD Integration Ready

---

## 🛠️ Tech Stack

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming Language   |
| Playwright     | Browser Automation     |
| PyTest         | Test Framework         |
| Allure         | Reporting              |
| PyTest HTML    | HTML Reports           |
| Faker          | Test Data Generation   |
| Git            | Version Control        |
| GitHub         | Source Code Repository |
| GitHub Actions | Continuous Integration |

---

## 🏗️ Framework Architecture

```text
Tests
   ↓
Page Objects
   ↓
Utilities
   ↓
Playwright APIs
   ↓
Browser
```

---

## 📂 Project Structure

```text
automationexercise_PlaywrightPythonFramework
│
├── pages/
├── tests/
├── data/
├── utils/
├── reports/
├── screenshots/
├── config/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .github/workflows/
```

---

## 🎯 Automated Test Scenarios

### User Registration

* Register User
* Register During Checkout
* Register Before Checkout
* Delete Account

### Authentication

* Login with Valid Credentials
* Login with Invalid Credentials
* Logout User

### Products

* View Products
* Search Products
* View Product Details

### Cart

* Add Products to Cart
* Remove Products from Cart
* Verify Cart Contents

### Checkout

* Place Order
* Verify Address Details
* Verify Order Summary

### End-to-End Flow

* Register User
* Login
* Add Product to Cart
* Checkout
* Place Order
* Delete Account

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Priya123z/automationexercise_PlaywrightPythonFramework.git
cd automationexercise_PlaywrightPythonFramework
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Execute Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test

```bash
pytest tests/test_login.py
```

### Run Tests in Parallel

```bash
pytest -n auto
```

### Run in Headless Mode

```bash
pytest --headed=False
```

---

## 📊 Generate Reports

### HTML Report

```bash
pytest --html=reports/report.html
```

### Allure Report

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 📸 Framework Capabilities

* Automatic Screenshot Capture on Failures
* Detailed Execution Logs
* Rich Allure Reporting Dashboard
* Parallel Execution Support
* Cross-Browser Compatibility
* CI/CD Pipeline Ready

---

## 🌐 Supported Browsers

* Chromium
* Firefox
* WebKit

---

## 🔄 CI/CD Integration

This framework is designed to be integrated with:

* GitHub Actions
* Jenkins
* Docker
* Linux Build Agents

Typical pipeline flow:

```text
Checkout Code
      ↓
Install Dependencies
      ↓
Install Browsers
      ↓
Execute Tests
      ↓
Generate Reports
      ↓
Publish Artifacts
```

---

## 📈 Why Playwright?

* Auto Waiting Mechanism
* Fast Execution
* Powerful Locator Strategies
* Cross-Browser Support
* Built-in Screenshot and Video Support
* Parallel Test Execution
* Modern Web Application Testing

---

## 🔮 Future Enhancements

* API Automation Integration
* Database Validation
* Docker Support
* Slack Notifications
* AWS Integration
* Self-Healing Locators
* Test Analytics Dashboard

---

## 👩‍💻 Author

**Priya**

QA Automation Engineer | Python | Playwright | PyTest | Selenium | API Testing | CI/CD

Passionate about building scalable, maintainable, and enterprise-grade automation frameworks that deliver reliable software quality.
