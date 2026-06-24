from playwright.sync_api import Page
from pathlib import Path

class ContactsPage:
    def __init__(self, page:Page):
        self.page = page
        self.contact_us_link = page.locator("a[href='/contact_us']")
        self.get_in_touch_title = page.locator("h2.title",has_text ="Get In Touch")
        self.name = page.locator("input[name='name']")
        self.email = page.locator("input[name='email']")
        self.subject = page.locator("input[name='subject']")
        self.messageinput = page.locator("#message")
        self.file_upload = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("input[value='Submit']")
        self.success_message = page.locator("div.alert-success.status")

    def go_to_contactus_page(self):
        try:
            self.contact_us_link.click()
        except Exception as e:
            print(f"Error while clicking on Contact Us link: {e}")
            raise

    def return_get_in_touch_title(self):
        try:
            return self.get_in_touch_title
        except Exception as e:
            print(f"Error while checking the element with text Get in Touch: {e}")
            raise

    def set_name(self,name):
        try:
            self.name.fill(name)
        except Exception as e:
            print(f"Error while filling name: {e}")
            raise

    def set_email(self, email):
        try:
            self.email.fill(email)
        except Exception as e:
            print(f"Error while filling in email: {e}")
            raise
    def set_subject(self, subject):
        try:
            self.subject.fill(subject)
        except Exception as e:
            print(f"Error while filling subject: {e}")
            raise
    def set_messageinput(self, messageinput):
        try:
            self.messageinput.fill(messageinput)
        except Exception as e:
            print(f"Error while filling messageinput: {e}")
            raise

    def set_file_upload(self, filepath):
        try:
            self.file_upload.set_input_files(filepath)
        except Exception as e:
            print(f"Error while filling file upload: {e}")
            raise
    def accept_dialog(self):
        try:
            self.page.on("dialog", lambda dialog : dialog.accept())
        except Exception as e:
            print(f"Error while clicking accepting the dialog: {e}")
            raise

    def click_submit_button(self):
        try:
            self.submit_button.click()
        except Exception as e:
            print(f"Error while clicking submit button: {e}")
            raise

    def return_success_message(self):
        return self.success_message

