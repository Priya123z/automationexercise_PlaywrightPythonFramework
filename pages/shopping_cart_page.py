from playwright.sync_api import Page


class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.items= page.locator("tbody tr")
        self.NameofItems = page.locator("tbody tr td.cart_description a")
        self.quantity = page.locator("td.cart_quantity button")
        self.delete_product = page.locator("td.cart_delete a")
        self.price = page.locator("td.cart_price p")
        self.totals = page.locator("td.cart_total p")
        self.proceed_to_checkout_btn = page.locator("a:has-text('Proceed To Checkout')")
        self.Register_login_link = page.locator("p a[href='/login']")
    def get_number_of_items(self):
        return self.items.count()
    def get_NameofItems(self):
        return self.NameofItems.all_inner_texts()
    def get_quantity(self):
        return self.quantity.all_inner_texts()
    def delete_products_from_cart(self):
        self.delete_product.click()
    def get_product_prices(self):
        return self.price.all_inner_texts()
    def get_totals(self):
        return self.totals.all_text_contents()
    def proceed_to_checkout(self):
        self.proceed_to_checkout_btn.first.click()
    def click_login_register_signin_link(self):
        self.Register_login_link.click()





