import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RegistrationFaker
from utilities.data_reader_util import read_csv_data
from pathlib import Path

file_path = Path(__file__).parent.parent / "testdata" / "RegisteredUser_EmailID.csv"

ValidData = read_csv_data(file_path)

print(ValidData)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.parametrize("login_data",ValidData)
def test_register_user_with_an_existing_email(page, login_data):
    '''
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    '''

    home_page = HomePage(page)
    registration_page = RegistrationPage(page)
    registration_faker = RegistrationFaker()
    #3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")

    #4. Click on 'Signup / Login' button
    home_page.click_login_signup_link()
    expect(page).to_have_title("Automation Exercise - Signup / Login")

    #5. Verify 'New User Signup!' is visible
    expect(registration_page.get_signup_header()).to_contain_text("New User Signup!")


    #6. Enter name and already registered email address
    registration_page.Enter_signup_name(login_data["Name"])
    registration_page.Enter_signup_email(login_data["Email"])

    #7. Click 'Signup' button
    registration_page.ClickSignupBtn()

    #8. Verify error 'Email Address already exist!' is visible
    expect(registration_page.get_existing_email_msg()).to_have_text("Email Address already exist!")