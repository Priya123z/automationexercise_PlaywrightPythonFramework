class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.logoutButton = self.page.locator("a[href='/logout']")
        self.logintextDisplay = self.page.locator("h2:has-text('Login to your account')")
    def click_logout(self):
        self.logoutButton.click()
        return self.logintextDisplay