import pytest
from playwright.sync_api import expect
from pages.Contact_us_page import ContactsPage
from pages.home_page import HomePage
from utilities.random_data_util import RegistrationFaker
from pathlib import Path

file_path = Path(__file__).parent.parent/"FileInputs"/"Sample.txt"

@pytest.mark.regression
def test_ContactUsForm(page):
    '''
      1. Launch browser
      2. Navigate to url 'http://automationexercise.com'
    '''
    Home_Pageobj = HomePage(page)
    ContactPageobj = ContactsPage(page)
    Registration_Faker = RegistrationFaker()
    #3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Contact Us' button
    ContactPageobj.go_to_contactus_page()
    #5. Verify 'GET IN TOUCH' is visible
    expect(ContactPageobj.return_get_in_touch_title()).to_have_text("Get In Touch")
    #6. Enter name, email, subject and message
    FakeData = Registration_Faker.generate_ContactUs_data()
    ContactPageobj.set_email(FakeData['email'])
    ContactPageobj.set_name(FakeData['name'])
    ContactPageobj.set_subject(FakeData['subject'])
    ContactPageobj.set_messageinput(FakeData['message'])
    #7. Upload file
    ContactPageobj.set_file_upload(file_path)
    #8. Click 'Submit' button
    #9. Click OK button
    ContactPageobj.accept_dialog()
    ContactPageobj.click_submit_button()
    #10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    expect(ContactPageobj.return_success_message()).to_have_text('Success! Your details have been submitted successfully.')
    #11. Click 'Home' button and verify that landed to home page successfully
    Home_Pageobj.click_home_page_link()
    expect(page).to_have_title("Automation Exercise")

