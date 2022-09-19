import random


class useful:
    URL = "http://automationpractice.com/index.php"
    number = random.randint(0, 1000)
    LastName = "George"
    Password_Pozitive = 12345
    Password_Negative = 1234
    mail = "test261George@yahoo.com"

    def Random_Email_Gen(self):
        mail = "test261George@yahoo.com"
        return mail

    def Random_FirstName_Gen(self):
        return "test" + str(useful.number)

    def Random_Phone_Number_Gen(self):
        return "+15204928" + str(useful.number)

    def Random_Address_Gen(self):
        return "test" + str(useful.number) + "Address, P.O. Box no. 27"

    def Random_Zip_Gen(self):
        return str(useful.number)

    def Random_Mobile_Phone_Gen(self):
        return "+152049289" + str(useful.number)


class SignIn:
    TEST_ACCOUNT = "testDaniel@yahoo.com"
    TEST_PASSWORD = "123456"
    TEST_FIRSTNAME = "test"
    TEST_LASTNAME = "Daniel"
    TEST_ADDRESS = "testAddress, P.O. Box no. 27"
    TEST_CITY = "Tucson"
    TEST_ZIP = "85641"
    TEST_MOBILE_PHONE = "+152049289191"
