from playwright.sync_api import Page
class HomePage:
    """Page object model class for the Home page"""
    def __init__(self, page:Page):
        '''Constructor for Homepage class to initialize all the objects and identify all the locators'''
        self.page = page
        self.login_signup_link = page.locator("li a[href='/login']")
        self.products_link = page.locator("li a[href='/products']")
        self.cart_link = page.locator("li a[href='/view_cart']")
        self.logout_link = page.locator('li a[href="/logout"]')
        self.Home_page_link = page.locator("li a[href='/']")
        self.Subscription_text = page.locator(".single-widget h2")
        self.Subscription_email = page.locator("#susbscribe_email")
        self.Subscription_email_submit_btn = page.locator("#subscribe")
        self.Subscription_Successful = page.locator("#success-subscribe")
        self.Delete_account_btn = page.locator("a[href='/delete_account']")
        self.success_delete_account_msg = page.locator(".title b")
    # Action methods to be performed in Home page
    def get_page_title(self) -> str:
        #return the title of the page
        return self.page.title()


    def click_login_signup_link(self):
        #To click on Login/signup link
        try:
            self.login_signup_link.click()
        except Exception as e:
            print(f"Failed to click login signup link: {e}")
            raise
    def click_home_page_link(self):
        try:
            self.Home_page_link.click()
        except Exception as e:
            print(f"Failed to click home page link: {e}")
            raise

    def click_products_link(self):
        try:
            self.products_link.click()
        except Exception as e:
            print(f"Failed to click products link: {e}")
            raise
    def click_cart_link(self):
        try:
            self.cart_link.click()
        except Exception as e:
            print(f"Failed to click cart link: {e}")
            raise
    def click_logout_link(self):
        try:
            self.logout_link.click()
        except Exception as e:
            print(f"Failed to click logout link: {e}")
            raise
    def Subscribe_header(self):
        return self.Subscription_text
    def set_subscription_email(self,email):
        self.Subscription_email.fill(email)
    def click_subscription_btn(self):
        self.Subscription_email_submit_btn.click()
    def get_Suscription_successful_msg(self):
        return self.Subscription_Successful
    def delete_account(self):
        self.Delete_account_btn.click()
    def success_delete(self):
        return self.success_delete_account_msg