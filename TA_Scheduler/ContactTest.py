from django.test import TestCase
from django.test import Client
from .models import myContact
from TA_Scheduler.Contact import Contact
# Create your tests here.

class TestContact(TestCase):
    def setUp(self):
        self.client = Client()
        self.goodContact = Contact.createContact(4146142209, "good@uwm.edu")
        self.emptyContact = Contact.createContact("", "")

    def create_good_contact(self):
        response = self.client.post("/profile/", {"phoneNumber": "1", "courseName": "COMPSCI"})
        course_list = response.context["course_list"]
        coursePair = course_list[0]
        self.assertEqual("1", str(coursePair[0]),
                         "Creating a new course COMPSCI with number 1 failed. Expected course numbers to match. 1 = 1")
        self.assertEqual("COMPSCI", str(coursePair[1]),
                         "Creating a new course COMPSCI with number 1 failed. Expected course names to match. COMPSCI = COMPSCI")
        self.assertEqual("", response.context["errorMessage"],
                         "Creating a new course COMPSCI with number 1 failed. Expected errorMessage to be empty. '' = '' ")

        from django.test import TestCase
        from django.test import Client
        from .models import myContact

        # Create your tests here.
        class login_test(TestCase):
            def setUp(self):
                # Setup client, account and number and email
class loginUnitTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.adminUser = myAccount.objects.create(userName="admin", password="password")
        self.standardUser = myAccount.objects.create(userName="dude", password="pass")
        self.emptyUser = myAccount.objects.create(userName="", password="")
        self.longUsername = "0123456789012345678901234567890123456789blablabla"
        self.longPassword = "0123456789012345678901234567890123456789blablabla"
    def good_login_test(self):
        #the admin and standard username should be found in the database
        self.assertEquals(myLogin.login(self.adminUser.userName, self.adminUser.password), "", "The credentials were correct but the login failed")
        self.assertEquals(myLogin.login(self.standardUser.userName, self.standardUser.password), "", "The credentials were correct but the login failed")

    def long_inputs_test(self):
        #long username
        self.assertEquals(myLogin.login(self.longUsername, self.adminUser.password), "The Username Is Too Long!",  "The username was wrong but login did not fail")
        self.assertEquals(myLogin.login(self.longUsername, self.standardUser.password), "The Username Is Too Long!", "The username was wrong but login did not fail")
        #long password
        self.assertEquals(myLogin.login(self.adminUser.userName, self.longPassword), "The Password Is Too Long!",  "The username was wrong but login did not fail")
        self.assertEquals(myLogin.login(self.standardUser.userName, self.longPassword),"The Password Is Too Long!", "The username was wrong but login did not fail")
        #both inputs are too long
        self.assertEquals(myLogin.login(self.longUsername, self.longPassword),"The Username Is Too Long!",  "The username was wrong but login did not fail")

    def wrong_username_test(self):
        self.assertEquals(myLogin.login("wrong", self.adminUser.password), "User doesn't exist",  "The username was wrong but login did not fail")
        self.assertEquals(myLogin.login("wrong", self.standardUser.password),"User doesn't exist" , "The username was wrong but login did not fail")

    def wrong_password_test(self):
        self.assertEquals(myLogin.login(self.standardUser.userName, "wrong" ),"Incorrect Password!" , "The password was wrong but login worked")
        self.assertEquals(myLogin.login(self.adminUser.userName, "wrong" ), "Incorrect Password!","The password was wrong but login worked")


    def empty_inputs_test(self):
        #empty username
        self.assertEquals("No Username Provided", myLogin.login(self.emptyUser.userName, self.emptyUser.password),"The username was empty but login worked")
        #empty password
        self.assertEquals("No Password Provided", myLogin.login(self.standardUser.userName, self.standardUser.password), "The password was empty but  worked")
        #both inputs empty
        self.assertEquals("No Username Provided", myLogin.login(self.emptydUser.userName, self.emptyUser.password), "Both inputs were empty but login worked")

    def input_mismatch_test(self):
        self.assertEquals("Incorrect Password", myLogin.login(self.adminUser.userName, self.standardUser.password),"The inputs don't match but login worked")
