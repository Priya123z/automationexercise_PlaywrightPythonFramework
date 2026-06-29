import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RegistrationFaker


# def test_registration_process(page):
#     home_page = HomePage(page)
#     registration_page = RegistrationPage(page)
#     home_page.click_login_signup_link()
#     registration_data_creator = RegistrationFaker()
#     data = registration_data_creator.generate_registration_data()
#     DataWriter.write_csv("C://Users//pbhagoriya//PycharmProjects//FrameworkDevelopment//testdata//new_user_registration_dump.csv", data)
#     msg = registration_page.end_to_end_registration_process(data)
#     expect(msg).to_have_text("Congratulations! Your new account has been successfully created!")


# Test Case 1: Register User
@pytest.mark.sanity
@pytest.mark.registerUser
def test_register_user(page):
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

    #6. Enter name and email address
    registrationData = registration_faker.generate_registration_data()
    registration_page.Enter_signup_name(registrationData["SignupName"])
    registration_page.Enter_signup_email(registrationData["sign_up_email"])

    #7. Click 'Signup' button
    registration_page.ClickSignupBtn()

    #8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(registration_page.enter_account_information_header()).to_be_visible()

    #9. Fill details: Title, Name, Email, Password, Date of birth
    registration_page.gender_selection(registrationData["genderName"])
    registration_page.signup_password_enter(registrationData["SignupPassword"])
    registration_page.Enter_Dob_Date(registrationData["DobDate"])
    registration_page.Enter_Dob_Month(registrationData["DobMonth"])
    registration_page.Enter_Dob_Year(registrationData["DobYear"])

    #10. Select checkbox 'Sign up for our newsletter!'

    #11. Select checkbox 'Receive special offers from our partners!'

    registration_page.Check_SignUp_for_Newsletter_SpecialOffers()

    #12. Fill details: First name, Last name, Company, Address, Country, State, City, Zipcode, Mobile Number
    registration_page.Enter_addressname(registrationData["address_name"])
    registration_page.Enter_addresssurname(registrationData["address_surname"])
    registration_page.Enter_companyname(registrationData["companyName"])
    registration_page.Enter_addressline(registrationData["addressLine1"])
    registration_page.Select_country(registrationData["country"])
    registration_page.Enter_city(registrationData["city"])
    registration_page.Enter_state(registrationData["state"])
    registration_page.Enter_zipcode(registrationData["zipcode"])
    registration_page.Enter_mobile(registrationData["mobile"])

    #13. Click 'Create Account button'
    registration_page.Click_Create_Account_button()

    #14. Verify that 'ACCOUNT CREATED!' is visible
    expect(registration_page.return_account_created_msg()).to_contain_text("Account Created!")
    registration_page.click_continue_btn()

    #16. Verify that 'Logged in as username' is visible
    expect(registration_page.return_logged_in_as_username()).to_contain_text(f" Logged in as {registrationData['SignupName']}")

    #17. Click 'Delete Account' button
    registration_page.delete_account()

    #18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(page.get_by_text("Account Deleted!")).to_be_visible()

