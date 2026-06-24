from time import process_time

from pages.Product_page import ProductPage
from pages.home_page import HomePage
from playwright.sync_api import expect

from pages.shopping_cart_page import CartPage



def test_add_products_in_cart(page):
    HomePageObj = HomePage(page)
    ProductPageObj = ProductPage(page)
    CartPageObj = CartPage(page)
    NameOfProduct = []

    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    #3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    #4. Click 'Products' button
    HomePageObj.click_products_link()
    #5. Hover over first product and click 'Add to cart'
    ProductPageObj.add_specific_product_to_cart(0)
    NameOfProduct.append(ProductPageObj.get_specific_product_detail(0).inner_text())
    #6. Click 'Continue Shopping' button
    ProductPageObj.ContinueShopping()
    #7. Hover over second product and click 'Add to cart'
    ProductPageObj.add_specific_product_to_cart(1)
    NameOfProduct.append(ProductPageObj.get_specific_product_detail(1).inner_text())
    #8. Click 'View Cart' button
    ProductPageObj.click_on_view_cart_button_in_popup()
    #9. Verify both products are added to Cart
    actual_names = [name.strip() for name in CartPageObj.get_NameofItems()]
    assert actual_names == NameOfProduct
    #10. Verify their prices, quantity and total price
    # prices = []
    # for prices in CartPageObj.get_product_prices():
    #     clean_price = prices.replace("Rs.","").strip()
    #     prices.append(int(clean_price))
    prices = [int(price.replace("Rs.","").strip())for price in CartPageObj.get_product_prices()]

    # quantities=[]
    #
    # for quantity in CartPageObj.get_quantity():
    #     quantities.append(int(quantity.strip()))
    quantities = [int(quantity.strip()) for quantity in CartPageObj.get_quantity()]
    # # totals = []
    # for totals in CartPageObj.get_totals():
    #     clean_totals = totals.replace("Rs.","").strip()
    #     totals.append(int(clean_totals))
    totals = [int(total.replace("Rs.","").strip()) for total in CartPageObj.get_totals()]
    for price,quantity,total in zip(prices, quantities, totals):
        assert total==(price*quantity), f"Expected {price * quantity}, Actual{total}"

    for i in range(len(prices)):
        price = prices[i]
        quantity = quantities[i]
        total = totals[i]
        expected_total = price*quantity
        actual_total = total
        assert(expected_total==actual_total)

