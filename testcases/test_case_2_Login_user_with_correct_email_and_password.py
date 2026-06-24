import pytest
from playwright.sync_api import expect

from pathlib import Path
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.data_reader_util import read_csv_data


file_path = Path(__file__).parent.parent / "testdata" / "logindata.csv"
csv_data = read_csv_data(file_path)
valid_data = [data for data in csv_data if data["testName"] == "Valid Login"]

@pytest.mark.sanity
@pytest.mark.parametrize("LoginData",valid_data)
def test_LoginValidUser(page,LoginData):

    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    #3. Verify that home page is visible successfully
    home_page = HomePage(page)
    login_page = LoginPage(page)

    #3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")

    # 4. Click on 'Signup / Login' button
    home_page.click_login_signup_link()

    #5. Verify 'Login to your account' is visible
    expect(login_page.get_LoginHeader()).to_have_text("Login to your account")

    #6. Enter correct email address and password
    login_page.set_email(LoginData["email"])
    login_page.set_password(LoginData["password"])
    #7. Click 'login' button
    login_page.click_login()
    #8. Verify that 'Logged in as username' is visible
    expect(login_page.getLoginId()).to_contain_text(f"Logged in as {LoginData['Name']}")



