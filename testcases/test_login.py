from playwright.sync_api import expect

from config import Config
from pages import home_page
from pages import login_page


def test_Valid_login_module(page):
    home_page_obj = home_page.HomePage(page)
    home_page_obj.click_login_signup_link()
    login_page_obj = login_page.LoginPage(page)
    expect(login_page_obj.login_process(Config.email, Config.password)).to_contain_text(" Logged in as ")

def test_Invalid_login_module(page):
    home_page_obj = home_page.HomePage(page)
    home_page_obj.click_login_signup_link()
    login_page_obj = login_page.LoginPage(page)
    login_page_obj.set_email(Config.invalid_email)
    login_page_obj.set_password(Config.invalid_password)
    login_page_obj.click_login()
    expect(login_page_obj.login_error()).to_be_visible(timeout=3000)



