from playwright.sync_api import expect

from config import Config
from pages.Product_page import ProductPage
from pages.home_page import HomePage


def test_searchProduct(page):
    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    #3. Verify that home page is visible successfully
    home_page = HomePage(page)
    expect(page).to_have_title("Automation Exercise")
    #4. Click on 'Products' button
    home_page.click_products_link()
    #5. Verify user is navigated to ALL PRODUCTS page successfully
    expect(page).to_have_title("Automation Exercise - All Products")
    #6. Enter product name in search input and click search button
    ProductPageobj = ProductPage(page)
    ProductPageobj.SearchSpecificProduct(Config.One_product_name)
    #7. Verify 'SEARCHED PRODUCTS' is visible
    searchedProduct = ProductPageobj.GetAllProducts().locator("p").filter(has_text=Config.One_product_name).first

    expect(searchedProduct).to_be_visible()
    #8. Verify all the products related to search are visible
    expect(ProductPageobj.GetAllProducts()).not_to_have_count(0)





