from playwright.sync_api import expect

from config import Config
from pages import home_page
from pages import login_page
from pages.Product_page import ProductPage
from utilities import data_reader_util

def test_add_to_cart_module(page):
    # home_page_obj = home_page.HomePage(page)
    # home_page_obj.click_login_signup_link()
    # login_page_obj = login_page.LoginPage(page)
    # login_page_obj.login_process(Config.email, Config.password)
    # # ProductPageobj = ProductPage(page)
    # # ProductPageobj.goto_product_page()
    # # ProductPageobj.AddProductstoCart(Config.product_name)
    # # ProductPageobj.Navigate_to_cart()
    Product_obj = ProductPage(page)
    Product_obj.goto_product_page()
    # Product_obj.GetAllProductNames()
    #Product_obj.SearchSpecificProduct(Config.One_product_name)
    # Product_obj.ViewProduct(Config.One_product_name)
    # Product_obj.AddQty(Config.product_quantity)
    # Product_obj.ContinueShopping()
    # Product_obj.GoToCart()
    csv_data = data_reader_util.read_csv_data("C://Users//pbhagoriya//PycharmProjects//FrameworkDevelopment//testdata//ProductsAdd.csv")
    ProductNames = []
    for row in csv_data:
        productName = row["product_name"]
        ProductNames.append(productName)
    print(ProductNames)
    Product_obj.AddMultipleProducts(ProductNames)
    Product_obj.GoToCart()

def test_Verify_All_Products_and_Product_Details_Page(page):
    HomePage_obj = home_page.HomePage(page)
    expect(page).to_have_title("Automation Exercise")
    ProductPage1_obj = ProductPage(page)
    ProductPage1_obj.goto_product_page()
    expect(page).to_have_title("Automation Exercise - All Products")
    expect(ProductPage1_obj.GetAllProducts().first).to_be_visible()

def test_Verify_search_results(page):
    HomePage_obj = home_page.HomePage(page)

