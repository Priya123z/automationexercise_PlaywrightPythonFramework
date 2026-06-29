from datetime import datetime

from faker import Faker
import random


class RegistrationFaker:

    def __init__(self):
        self.fake = Faker()

    def generate_registration_data(self):

        gender = random.choice(["Mr", "Mrs"])
        unique = datetime.now().strftime("%Y%m%d%H%M%S%f")

        return {
            "SignupEmail": f"{self.fake.unique.email()}_{unique}",

            "SignupName": self.fake.first_name(),

            "genderName": gender,

            "SignupPassword":
                self.fake.password(
                    length=12,
                    special_chars=True,
                    digits=True,
                    upper_case=True,
                    lower_case=True
                ),

            "DobDate": str(random.randint(1, 28)),

            "DobMonth":
                random.choice([
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]),

            "DobYear":
                str(random.randint(1985, 2005)),

            "address_name":
                self.fake.first_name(),

            "address_surname":
                self.fake.last_name(),

            "companyName":
                self.fake.company(),

            "addressLine1":
                self.fake.street_address(),
            "country":
                random.choice(['India','United States','Canada','Australia','Israel','New Zealand','Singapore']),

            "state":
                self.fake.state(),

            "city":
                self.fake.city(),

            "zipcode":
                self.fake.postcode(),

            "mobile":
                self.fake.msisdn()[:10]
        }
    def generate_ContactUs_data(self):
        return{
            "name": self.fake.first_name(),
            "email": self.fake.email(),
            "subject": self.fake.sentence(nb_words=7),
            "message": self.fake.paragraph(nb_sentences=7),
        }
    def generate_Card_details(self):
        return{
            "name_on_card": self.fake.name_nonbinary(),
            "card_number":self.fake.credit_card_number(),
            "cvv_number":self.fake.msisdn()[:3],
            "expiry_month":self.fake.month(),
            "expiry_year":self.fake.year()

        }


# Example usage
# if __name__ == "__main__":
#     data = RegistrationFaker().generate_registration_data()
#
#     for key, value in data.items():
#         print(f"{key}: {value}")