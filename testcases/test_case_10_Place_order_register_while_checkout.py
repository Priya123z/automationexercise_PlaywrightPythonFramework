import faker
import pytest

from pages.Checkout_page import Checkout
from pages.PaymentDetails_page import paymentDetails
from pages.Product_page import ProductPage
from pages.home_page import HomePage
from playwright.sync_api import expect
from utilities.random_data_util import RegistrationFaker
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import CartPage
from utilities.data_reader_util import read_csv_data
from pathlib import Path


def test_place_order_and_register_while_checkingout(page):
    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    #3. Verify that home page is visible successfully
    home_page_obj = HomePage(page)
    product_page_obj = ProductPage(page)
    cart_page_obj = CartPage(page)
    expect(page).to_have_title("Automation Exercise")

    home_page_obj.click_products_link()
    #4. Add products to cart
    file_path = Path(__file__).parent.parent / "testdata" / "ProductsAdd.csv"
    csv_data = read_csv_data(file_path)
    product_name = []
    for data in csv_data:
        product_name.extend(data.values())
    product_page_obj.AddMultipleProducts(product_name)
    #5. Click 'Cart' button
    home_page_obj.click_cart_link()
    #6. Verify that cart page is displayed
    expect(page).to_have_title("Automation Exercise - Checkout")
    #7. Click Proceed To Checkout
    cart_page_obj.proceed_to_checkout()
    #8. Click 'Register / Login' button
    cart_page_obj.click_login_register_signin_link()
    Registrationobj = RegistrationPage(page)
    RegistrationFakerobj = RegistrationFaker()
    UserData = RegistrationFakerobj.generate_registration_data()
    #9. Fill all details in Signup and create account
    Registrationobj.end_to_end_registration_process(UserData)

    #10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    expect(Registrationobj.return_account_created_msg()).to_contain_text("Account Created!")
    Registrationobj.click_continue_btn()
    #11. Verify ' Logged in as username' at top
    expect(Registrationobj.return_logged_in_as_username()).to_contain_text(
        f" Logged in as {UserData['SignupName']}")
    #12.Click 'Cart' button
    home_page_obj.click_cart_link()
    #13. Click 'Proceed To Checkout' button
    cart_page_obj.proceed_to_checkout()
    #14.Verify Address Details and Review Your Order
    CheckoutPageobj = Checkout(page)
    CheckoutPageobj.add_comments("Some comments")
    CheckoutPageobj.click_place_order()
    #16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    CardDetails = RegistrationFakerobj.generate_Card_details()
    print(CardDetails)
    paymentdetailsobj = paymentDetails(page)
    paymentdetailsobj.set_name_on_card(CardDetails['name_on_card'])
    paymentdetailsobj.set_card_number(CardDetails['card_number'])
    paymentdetailsobj.set_cvc_number(CardDetails['cvv_number'])
    paymentdetailsobj.set_expiry_month(CardDetails['expiry_month'])
    paymentdetailsobj.set_expiry_year(CardDetails['expiry_year'])
    #17. Click 'Pay and Confirm Order' button
    paymentdetailsobj.click_confirm_order_btn()
    #18. Verify success message 'Your order has been placed successfully!'
    successmsg = page.get_by_text("Your order has been placed successfully!")
    # print(successmsg)
    # expect(successmsg).to_contain_text("Your order has been placed successfully!")
    #19. Click 'Delete Account' button
    home_page_obj.delete_account()
    #20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    expect(home_page_obj.success_delete_account_msg).to_have_text("Account Deleted!")