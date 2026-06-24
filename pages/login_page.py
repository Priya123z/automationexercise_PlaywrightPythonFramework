from sys import exception

from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page: Page):
        self.page = page
        self.login_email = page.locator("input[name='email'][data-qa='login-email']")
        self.login_password = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.txt_error_message = page.locator("p:has-text('Your email or password is incorrect!')")
        self.login_Id = page.locator("a:has-text(' Logged in as ')")
        self.login_header = page.locator(".login-form h2")

    def set_email(self,email: str):
        try:
            self.login_email.fill(email)
        except exception as e:
            print(f"Error in typing in the Email: {e}")
            raise
    def set_password(self,password: str):
        try:
            self.login_password.fill(password)
        except exception as e:
            print(f"Error in typing in the Password: {e}")
            raise
    def click_login(self):
        try:
            self.login_button.click()
        except exception as e:
            print(f"Error in clicking on Login button: {e}")
            raise
    def getLoginId(self):
        try:
            return self.login_Id
        except exception as e:
            print(f"Error in getting Login Id: {e}")
            raise

    def get_LoginHeader(self):
        try:
            return self.login_header
        except exception as e:
            print(f"Error in getting Login Header: {e}")
            raise
    def login_process(self,email: str, password: str):
        """Perform the complete login process"""
        #Enter Email
        #Enter Password
        #Click login  button
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        return self.login_Id

    def login_error(self):
        """:return error message if login fails due to invalid credentials"""
        try:
            return self.txt_error_message
        except Exception as e:
            print(f"Error in logging in: {e}")
            return None


