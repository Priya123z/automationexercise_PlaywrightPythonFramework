from openpyxl.styles.builtins import check_cell
from playwright.sync_api import Page
class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_up_name = page.locator("input[data-qa = 'signup-name']")
        self.sign_up_email = page.locator("input[data-qa = 'signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.select_gender = page.locator(".radio-inline")
        self.sign_up_password = page.locator("#password")
        self.DateofBirth_date = page.locator("#days")
        self.DateofBirth_month = page.locator("#months")
        self.DateofBirth_year = page.locator("#years")
        self.CheckboxSignup = page.locator(".checkbox")
        self.address_name = page.locator("#first_name")
        self.address_last_name = page.locator("#last_name")
        self.address_line1 = page.locator("input#address1")
        self.company_name= page.locator("#company")
        self.country = page.locator("#country")
        self.state  = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile = page.locator("#mobile_number")
        self.Create_Account_button= page.locator("button[data-qa='create-account']")
        self.confirmationMsg = page.locator("p:has-text('Congratulations! Your new account has been successfully created!')")
        self.new_user_signup = page.locator("h2",has_text="New User Signup!")
        self.ContinueBtn = page.locator(".pull-right a",has_text="Continue")
        self.Enter_accountinfo_header  = page.locator(".title b",has_text="Enter Account Information")
        self.AccountCreatedMsg = page.locator("h2.title b")
        self.LoggedinAsUserName = page.locator("li:has-text('Logged in as')")
        self.Delete_accountbtn = page.locator("a[href='/delete_account']")
        self.ExistingEmailAddress= page.locator("p:has-text('Email Address already exist!')")

    def get_signup_header(self):
        try:
            return self.new_user_signup
        except Exception as e:
            print("Error getting signup header")
            raise
    def Enter_signup_email(self,SignupEmail):
        try:
            self.sign_up_email.fill(SignupEmail)
        except Exception as e:
            print(f"Error while typing in the signup Email field: {e}")
            raise
    def Enter_signup_name(self,signUpName):
        try:
            self.sign_up_name.fill(signUpName)
        except Exception as e:
            print(f"Error while typing in the signup Name field: {e}")
            raise
    def ClickSignupBtn(self):
        try:
            self.signup_button.click()
        except Exception as e:
            print(f"Error while clicking the signup button: {e}")
            raise
    def gender_selection(self,genderName):
        try:
            self.select_gender.locator(f"input[value='{genderName}']").click()
        except Exception as e:
            print(f"Error while clicking the gender selection button: {e}")
            raise
    def enter_account_information_header(self):
        try:
            return self.Enter_accountinfo_header
        except Exception as e:
            print("Error while entering the account information header")
            raise

    def signup_password_enter(self,signupPassword):
        try:
            self.sign_up_password.fill(signupPassword)
        except Exception as e:
            print(f"Error while entering the password field: {e}")
            raise
    def Enter_Dob_Date(self,Date_of_Birth_date):
        try:
            self.DateofBirth_date.select_option(value=Date_of_Birth_date)
        except Exception as e:
            print(f"Error while entering the date of birth field: {e}")
            raise
    def Enter_Dob_Month(self,Date_of_Birth_month):
        try:
            self.DateofBirth_month.select_option(label=Date_of_Birth_month)
        except Exception as e:
            print(f"Error while entering the date of birth month field: {e}")
            raise
    def Enter_Dob_Year(self,Date_of_Birth_year):
        try:
            self.DateofBirth_year.select_option(label=Date_of_Birth_year)
        except Exception as e:
            print(f"Error while entering the date of birth year field: {e}")
            raise

    def Check_SignUp_for_Newsletter_SpecialOffers(self):
        checkboxes = self.CheckboxSignup.all()
        for checkbox in checkboxes:
            checkbox.click()

    def Enter_addressname(self, addressName):
        try:
            self.address_name.fill(addressName)
        except Exception as e:
            print(f"Error while entering the address name field: {e}")
            raise
    def Enter_addresssurname(self,addressSurname):
        try:
            self.address_last_name.fill(addressSurname)
        except Exception as e:
            print(f"Error while entering the address surname field: {e}")
            raise
    def Enter_companyname(self,companyName):
        try:
            self.company_name.fill(companyName)
        except Exception as e:
            print(f"Error while entering the company name field: {e}")
            raise
    def Enter_addressline(self,addressLine1):
        try:
            self.address_line1.fill(addressLine1)
        except Exception as e:
            print(f"Error while entering the address field: {e}")
            raise
    def Select_country(self, country):
        try:
            self.country.select_option(label=country)
        except Exception as e:
            print(f"Error while selecting country field: {e}")
            raise

    def Enter_state(self, state):
        try:
            self.state.fill(state)
        except Exception as e:
            print(f"Error while entering the state field: {e}")
            raise
    def Enter_city(self, city):
        try:
            self.city.fill(city)
        except Exception as e:
            print(f"Error while entering the city field: {e}")
            raise

    def Enter_zipcode(self, zipcode):
        try:
            self.zipcode.fill(zipcode)
        except Exception as e:
            print(f"Error while entering the zipcode field: {e}")
            raise

    def Enter_mobile(self,mobile):
        try:
            self.mobile.fill(mobile)
        except Exception as e:
            print(f"Error while entering the mobile field: {e}")
            raise

    def Click_Create_Account_button(self):
        try:
            self.Create_Account_button.click()
        except Exception as e:
            print(f"Error while clicking the create account button: {e}")
            raise

    def get_signup_successful_message(self):
        return self.confirmationMsg

    def return_account_created_msg(self):
        return self.AccountCreatedMsg
    def click_continue_btn(self):
        self.ContinueBtn.click()

    def return_logged_in_as_username(self):
        return self.LoggedinAsUserName
    def delete_account(self):
        self.Delete_accountbtn.click()

    def get_existing_email_msg(self):
        return self.ExistingEmailAddress

    def end_to_end_registration_process(self, userData: dict):
        """Complete the Registration process with the provided data"""
        self.Enter_signup_email(userData["SignupEmail"])
        self.Enter_signup_name(userData["SignupName"])
        self.ClickSignupBtn()
        self.gender_selection(userData["genderName"])
        self.signup_password_enter(userData["SignupPassword"])
        self.Enter_Dob_Date(userData["DobDate"])
        self.Enter_Dob_Month(userData["DobMonth"])
        self.Enter_Dob_Year(userData["DobYear"])
        self.Enter_addressline(userData["addressLine1"])
        self.Enter_addressname(userData["address_name"])
        self.Enter_addresssurname(userData["address_surname"])
        self.Enter_state(userData["state"])
        self.Enter_mobile(userData["mobile"])
        self.Enter_city(userData["city"])
        self.Enter_zipcode(userData["zipcode"])
        self.Click_Create_Account_button()
        return self.confirmationMsg


