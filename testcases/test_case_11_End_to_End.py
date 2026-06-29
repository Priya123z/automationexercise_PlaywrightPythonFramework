import pytest
from playwright.sync_api import expect

import config
from pages.Checkout_page import Checkout
from pages.PaymentDetails_page import paymentDetails
from pages.Product_page import ProductPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import CartPage
from utilities.random_data_util import RegistrationFaker

@pytest.mark.end_to_end
def test_end_to_end_flow(page):
    """
    # End-to-End Test plan
    # 1. Register a new user
    # 2. Logout
    # 3. Login with valid credentials
    # 4. Search and add a product to cart
    # 5. Verify cart contents
    """
    # #Step 1: Register a new account and capture the generated email
    #
    # RegistrationFakerobj = RegistrationFaker()
    #
    # registrationobj = RegistrationPage(page)
    # UserData = RegistrationFakerobj.generate_registration_data()
    # HomePageobj = HomePage(page)
    # HomePageobj.click_login_signup_link()
    # expect(registrationobj.end_to_end_registration_process(UserData)).to_have_text("Congratulations! Your new account has been successfully created!")
    # UserEmail = UserData["SignupEmail"]
    # UserPassword = UserData["SignupPassword"]
    # registrationobj.click_continue_btn()
    # HomePageobj = HomePage(page)
    # #Step 2:
    # HomePageobj.click_logout_link()
    # #Step 3:Login with valid credentials
    # LoginPageobj = LoginPage(page)
    # LoginPageobj.set_email(UserEmail)
    # LoginPageobj.set_password(UserPassword)
    # LoginPageobj.click_login()
    # #4. Search and add a product to cart
    # Productpageobj = ProductPage(page)
    # HomePageobj.click_products_link()
    # Productpageobj.SearchSpecificProduct(config.Config.One_product_name)
    # Productpageobj.Add_to_cart_product(config.Config.One_product_name)
    # #5. Verify cart contents
    # HomePageobj.click_cart_link()
    # CartPageobj = CartPage(page)
    # ItemsAdded = CartPageobj.get_NameofItems()
    # assert config.Config.One_product_name in ItemsAdded
    # CartPageobj.proceed_to_checkout()
    # #6. Checkout
    # Checkoutobj = Checkout(page)
    # Checkoutobj.click_place_order()
    #
    # #6. Place the order succesfully
    # Paymentdetailsobj = paymentDetails(page)
    # CardDetails = RegistrationFakerobj.generate_Card_details()
    # Success_message = Paymentdetailsobj.End_to_End_paymentCheckout(CardDetails["name_on_card"],CardDetails["card_number"],CardDetails["cvv_number"],CardDetails["expiry_month"],CardDetails["expiry_year"])
    # expect(Success_message).to_have_text("Order Placed!")
    # Checkoutobj.click_continue()
    # HomePageobj.delete_account()
    #======================
    #1. Register user using Email Password Passed by Random generator
    UserEmail, UserPassword, HomePageobj = perform_registration(page)
    #2. Perform logout
    perform_logout(page,HomePageobj)
    #3. Perform Login
    perform_login(page,UserEmail,UserPassword)
    #Add to Cart products
    addProductsToCart(page,HomePageobj)
    #Verify Cart Content
    verify_cart_content(page,HomePageobj)
    #Checkout the cart
    Checkoutobj= Checkout_cart(page)
    #place order
    place_order(page,Checkoutobj)

#Helper function - 1. To Register a user
def perform_registration(page):
    RegistrationFakerobj = RegistrationFaker()

    registrationobj = RegistrationPage(page)
    UserData = RegistrationFakerobj.generate_registration_data()
    HomePageobj = HomePage(page)
    HomePageobj.click_login_signup_link()
    expect(registrationobj.end_to_end_registration_process(UserData)).to_have_text(
        "Congratulations! Your new account has been successfully created!")
    UserEmail = UserData["sign_up_email"]
    UserPassword = UserData["SignupPassword"]
    registrationobj.click_continue_btn()
    HomePageobj = HomePage(page)
    return UserEmail, UserPassword, HomePageobj

def perform_logout(page,HomePageobj):
    HomePageobj.click_logout_link()
def perform_login(page,UserEmail,UserPassword):
    #Step 3:Login with valid credentials
    LoginPageobj = LoginPage(page)
    LoginPageobj.set_email(UserEmail)
    LoginPageobj.set_password(UserPassword)
    LoginPageobj.click_login()
def addProductsToCart(page, HomePageobj):
    Productpageobj = ProductPage(page)
    HomePageobj.click_products_link()
    Productpageobj.SearchSpecificProduct(config.Config.One_product_name)
    Productpageobj.Add_to_cart_product(config.Config.One_product_name)
def verify_cart_content(page,HomePageobj):
    HomePageobj.click_cart_link()
    CartPageobj = CartPage(page)
    ItemsAdded = CartPageobj.get_NameofItems()
    assert config.Config.One_product_name in ItemsAdded
    CartPageobj.proceed_to_checkout()
def Checkout_cart(page):
    Checkoutobj = Checkout(page)
    Checkoutobj.click_place_order()
    return Checkoutobj
def place_order(page,Checkoutobj):
    RegistrationFakerobj = RegistrationFaker()
    Checkoutobj = Checkout(page)
    Paymentdetailsobj = paymentDetails(page)
    CardDetails = RegistrationFakerobj.generate_Card_details()
    Success_message = Paymentdetailsobj.End_to_End_paymentCheckout(CardDetails["name_on_card"],CardDetails["card_number"],CardDetails["cvv_number"],CardDetails["expiry_month"],CardDetails["expiry_year"])
    expect(Success_message).to_have_text("Order Placed!")
    Checkoutobj.click_continue()



