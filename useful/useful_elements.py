import random

class useful:
    URL = "http://automationpractice.com/index.php"
    number = random.randint(0, 1000)
    LastName = "George"
    Password_Pozitive = 12345
    Password_Negative = 1234

    def Random_Email_Gen(self):
        return "test" + str(useful.number) + "George@yahoo.com"

    def Random_FirstName_Gen(self):
        return "test" + str(useful.number)

    def Random_Phone_Number_Gen(self):
        return "+15204928" + str(useful.number)

class SignIn:
    TEST_ACCOUNT = "testDaniel@yahoo.com"
    TEST_PASSWORD = "123456"
    TEST_FIRSTNAME = "test"
    TEST_LASTNAME = "Daniel"
    TEST_ADDRESS = "testAddress, P.O. Box no. 27"
    TEST_CITY = "Tucson"
    TEST_ZIP = "85641"
    TEST_MOBILE_PHONE = "+152049289191"

