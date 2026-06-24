import pytest
from playwright.sync_api import expect
from pathlib import Path
from pages.home_page import HomePage
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from config import Config
from utilities.data_reader_util import  read_csv_data

file_path = Path(__file__).parent.parent/ "testdata"/"logindata.csv"
csv_data = read_csv_data(file_path)

valid_data = [data for data in csv_data if data["testName"] == "Valid Login"]

@pytest.mark.regression
@pytest.mark.parametrize("loginData",valid_data)
def test_user_logout(page, loginData):
    HomePageObj = HomePage(page)
    HomePageObj.click_login_signup_link()
    LoginPagebj = LoginPage(page)
    LoginPagebj.set_email(loginData["email"])
    LoginPagebj.set_password(loginData["password"])
    LoginPagebj.click_login()
    LogOutObject = LogoutPage(page)
    LogOutObject.click_logout()
    expect(LogOutObject.logintextDisplay).to_contain_text("Login to your account")
