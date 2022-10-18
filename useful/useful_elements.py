import random


class useful:
    URL = "http://automationpractice.com/index.php"
    number = random.randint(0, 1000)
    number = str(number)

    LastName = "George"
    Password_Pozitive = 12345
    Password_Negative = 1234
    mail = "test261George@yahoo.com"

    random_mail_gen = "test" + number + "George@yahoo.com"
    random_firstname_gen = "test"
    random_phone_gen = "+15204928" + number
    random_address_gen = "test" + number + "Address, P.O. Box no. 27"
    random_zip_gen = 50026

    def Random_Zip_Gen(self, zip_number=number):
        if len(zip_number) < 5:
            zip_number *= 10
        else:
            return zip_number


class SignIn:
    TEST_ACCOUNT = "testDaniel@yahoo.com"
    TEST_PASSWORD = "123456"
    TEST_FIRSTNAME = "test"
    TEST_LASTNAME = "Daniel"
    TEST_ADDRESS = "testAddress, P.O. Box no. 27"
    TEST_CITY = "Tucson"
    TEST_ZIP = "85641"
    TEST_MOBILE_PHONE = "+152049289191"
