import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities import data_reader_util


csv_data = data_reader_util.read_csv_data("C://Users//pbhagoriya//PycharmProjects//FrameworkDevelopment//testdata//logindata.csv")
@pytest.mark.parametrize("login_data",csv_data)
def test_login_data_driven_testing(page,login_data):
    #creating Home Page object to navigate to the login screen via Home Page
    HomePageobj = HomePage(page)
    #Creating Login Page object to perform login operation
    login_pageobj = LoginPage(page)
    #click on Signup/login link
    HomePageobj.click_login_signup_link()
    #enter Email
    login_pageobj.set_email(login_data["email"])
    #enter password
    login_pageobj.set_password(login_data["password"])
    #click login button
    login_pageobj.click_login()
    if login_data["expected"] == "Success":
        expect(login_pageobj.getLoginId()).to_contain_text(" Logged in as ")
    else:
        expect(login_pageobj.login_error()).to_be_visible(timeout=3000)

