

class Checkout:
    def __init__(self, page):
        self.page = page
        self.comments_area= page.locator("#ordermsg textarea")
        self.place_order_btn = page.locator("div a[href='/payment']")
        self.continue_btn_link = page.get_by_role("link", name="Continue")
    def add_comments(self,comments):
        self.comments_area.fill(comments)
    def click_place_order(self):
        self.place_order_btn.click()
    def click_continue(self):
        self.continue_btn_link.click()

