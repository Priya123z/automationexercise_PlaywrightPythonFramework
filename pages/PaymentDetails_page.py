class paymentDetails:
    def __init__(self, page):
        self.page = page
        self.name_on_card = page.locator("input[name='name_on_card']")
        self.card_number = page.locator("input[name ='card_number']")
        self.cvc_number = page.locator("input[name='cvc']")
        self.expiry_month = page.locator("input[name ='expiry_month']")
        self.expiry_year = page.locator("input[name='expiry_year']")
        self.confirm_order_btn = page.locator("button#submit")
        self.Successful_text = page.locator(".text-center b")
        self.ClickContinue_button = page.get_by_role("link", name="Continue")

    def set_name_on_card(self,name):
        self.name_on_card.fill(name)
    def set_card_number(self,card_number):
        self.card_number.fill(card_number)
    def set_cvc_number(self,cvc_number):
        self.cvc_number.fill(cvc_number)
    def set_expiry_month(self,expiry_month):
        self.expiry_month.fill(expiry_month)
    def set_expiry_year(self,expiry_year):
        self.expiry_year.fill(expiry_year)
    def click_confirm_order_btn(self):
        self.confirm_order_btn.click()
    def End_to_End_paymentCheckout(self,name,card_number,cvc_number,expiry_month,expiry_year):
        self.name_on_card.fill(name)
        self.card_number.fill(card_number)
        self.cvc_number.fill(cvc_number)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year)
        self.confirm_order_btn.click()
        return self.Successful_text
    def Click_continue(self):
        self.ClickContinue_button.click()
