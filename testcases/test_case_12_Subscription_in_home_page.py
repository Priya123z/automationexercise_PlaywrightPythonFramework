import time

from pygments.lexers import email

from pages.home_page import HomePage
from playwright.sync_api import expect

def test_SubscriptionFunction(page):
    #1. Launch browser
    #2. Navigate to url 'http://automationexercise.com'
    HomePageObj = HomePage(page)
    #3. Scroll down to footer
    HomePageObj.Subscription_text.scroll_into_view_if_needed()
    #4. Verify text 'SUBSCRIPTION'
    expect(HomePageObj.Subscription_text).to_have_text("Subscription")
    #5. Enter email address in input and click arrow button
    HomePageObj.set_subscription_email("Email@sample.com")
    HomePageObj.Subscription_email_submit_btn.click()
    #7. Verify success message 'You have been successfully subscribed!' is visible
    expect(HomePageObj.get_Suscription_successful_msg()).to_have_text("You have been successfully subscribed!")
