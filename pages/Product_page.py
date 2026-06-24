from playwright.sync_api import expect


class ProductPage:
    def __init__(self, page):
        self.page = page
        self.Product_page_link = page.locator("a[href='/products']")
        self.searchProduct_Input = page.locator("input#search_product")
        self.SearchProductButton = page.locator("button#submit_search")
        self.ViewProductButton = page.locator("a[href*='/product_details']")
        self.AllProducts = page.locator(".single-products")
        self.ContinueShoppingButton = page.locator("//button[text()= 'Continue Shopping']")
        self.GoToCartLink = page.locator("li a[href='/view_cart']")
        self.quantity = page.locator("#quantity")
        self.AddToBasketButton = page.locator("button",has_text="Add to cart")
        self.first_product = page.locator(".product-image-wrapper .choose").first
        self.product_Name = page.locator(".product-information h2")
        self.product_category = page.locator(".product-information p").nth(0)
        self.product_price = page.locator(".product-information span span:has-text('Rs.')")
        self.product_availability = page.locator("p:has-text('Availability')")
        self.product_condition = page.locator("p:has-text('Condition')")
        self.product_brand = page.locator("p:has-text('Brand')")
        self.ViewCart_button_in_popup = page.locator("p a[href='/view_cart']")

    def add_specific_product_to_cart(self,number):
        self.AllProducts.locator(".productinfo a").nth(number).click()

    def get_specific_product_detail(self,number):
        return self.AllProducts.locator(".productinfo p").nth(number)

    def get_title_of_the_page(self):
        return self.page.title()

    def goto_product_page(self):
        self.Product_page_link.click()

    def SearchSpecificProduct(self,ProductName):
        self.searchProduct_Input.fill(ProductName)
        self.SearchProductButton.click()
        count = self.AllProducts.count()
        if(count == 0):
            print("No products found")
        elif(count == 1):
            print("1 product found")
        else:
            print("more than 1 product found")
    def ViewProduct(self,ProductName):

        product = self.AllProducts.filter(has_text=ProductName).first
        if(product == None):
            return None
        else:
            product.hover()
            product.locator(" +div.choose a").click()
            return product
    def AddQty(self,quantity):
        self.quantity.fill("")
        self.quantity.fill(quantity)
        self.AddToBasketButton.click()

    def ContinueShopping(self):
        self.ContinueShoppingButton.click()

    def AddMultipleProducts(self,ProductList:list):
        for name in ProductList:
            product = self.AllProducts.filter(has_text=name).first
            product.wait_for(state="visible")

            product.hover()

            product.locator(".productinfo a",has_text="Add to cart").click()
            self.ContinueShopping()

            expect(self.ContinueShoppingButton).not_to_be_visible()

            print(f"Added {product.inner_text()}")
    def GoToCart(self):
        self.GoToCartLink.click()
    def GetAllProductNames(self):
        AllProductNames = self.AllProducts.all()
        for i in AllProductNames:
            print(i.locator(".productinfo p").inner_text())
    def GetAllProducts(self):
        return self.AllProducts

    def ReturnFirstProduct(self):
        self.ViewProductButton.first.click()

    def click_on_view_cart_button_in_popup(self):
        self.ViewCart_button_in_popup.click()

    def Return_product_name(self):
        return self.product_Name
    def Return_productDetails(self):
        return self.product_category
    def Return_product_price(self):
        return self.product_price
    def Return_product_availability(self):
        return self.product_availability
    def Return_product_condition(self):
        return self.product_condition
    def Return_product_brand(self):
        return self.product_brand
    def Return_product_category(self):
        return self.product_category
    def Add_to_cart_product(self,Product_name):
        product = self.AllProducts.filter(has_text=Product_name).first
        product.hover()
        product.locator(".productinfo a", has_text="Add to cart").click()
        self.ContinueShopping()




