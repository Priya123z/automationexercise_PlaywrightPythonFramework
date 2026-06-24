from itertools import count

from playwright.sync_api import expect

from pages.Product_page import ProductPage
from pages.home_page import HomePage


def test_Verify_all_products_and_details_page(page):

    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    HomePageobj = HomePage(page)

    #3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")

    # 4. Click on 'Products' button
    HomePageobj.click_products_link()

    #5. Verify user is navigated to ALL PRODUCTS page successfully
    expect(page).to_have_title("Automation Exercise - All Products")

    #6. The products list is visible
    ProductPageobj = ProductPage(page)
    expect(ProductPageobj.GetAllProducts()).not_to_have_count(0)

    #7. Click on 'View Product' of first product
    ProductPageobj.ReturnFirstProduct()

    #8. User is landed to product detail page
    expect(page).to_have_title("Automation Exercise - Product Details")

    #9. Verify that detail is visible: product name, category, price, availability, condition, brand
    expect(ProductPageobj.Return_product_name()).not_to_be_empty()
    expect(ProductPageobj.Return_product_price()).not_to_be_empty()
    expect(ProductPageobj.Return_product_availability()).not_to_be_empty()
    expect(ProductPageobj.Return_product_condition()).not_to_be_empty()
    expect(ProductPageobj.Return_product_brand()).not_to_be_empty()
    expect(ProductPageobj.Return_product_category()).not_to_be_empty()
