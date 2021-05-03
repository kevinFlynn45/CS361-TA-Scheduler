from django.test import TestCase
from django.test import Client
from .models import myAccount
# Create your tests here.
class login_test(TestCase):

    def setUp(self):
        #Setup client, account and something in the list
        self.client = Client()
        self.adminUser = myAccount.objects.create(userName="admin", password="password")
        self.standardUser = myAccount.objects.create(userName="dude", password = "pass")
        self.emptyUser = myAccount.objects.create(userName= "", password= "" )
        #create a course

    def test_good_login(self):
        #Good login with admin
        response = self.client.post("/", {"userName": self.adminUser.userName, "password": self.adminUser.password})
        #Check redirect: Should it redirect to a homepge when the user logs in?
        self.assertEqual("/home/", response.url,"Log in as admin with correct credentials admin failed."
                                                    "Expected redirect URL to be /home")
        #Good login with standard user
        response = self.client.post("/", {"userName": self.standardUser.userName, "password": self.standardUser.password})
        #Check redirect: Should it redirect to a homepge when the user logs in?
        self.assertEqual("/home/", response.url,"Log in a standard user with correct credentials admin failed."
                                                    "Expected redirect URL to be /home")

    def test_empty_credentials(self):
        #Login with an empty username
        response = self.client.post("/", {"userName": self.standardUser.userName, "password": self.emptyUser.password})
        self.assertEqual("No Password Provided!", response.context['errorMessage'],
        "Log in with an empty password should fail. Expected <No Password Provided!> message")
        # Login with an empty password
        response = self.client.post("/", {"userName": self.emptyUser.userName, "password": self.emptyUser.password})
        self.assertEqual("No Username Provided!", response.context['errorMessage'],
                         "Log in with an empty password should fail. Expected <No Username Provided!> message")
        #login with empty username and password
        response = self.client.post("/", {"userName": self.emptyUser.userName, "password": self.emptyUser.password})
        self.assertEqual("No Username Provided!", response.context['errorMessage'],"Log in with an empty "
        "password and username should fail. Expected <No Username Provided!> message")

    def test_inexisting_credentials(self):
        #Login with an inexisting username
        response = self.client.post("/", {"userName": "ret8578", "password": self.standardUser.password })
        self.assertEqual("User Doesn't Exist", response.context['errorMessage'],
        "Log in with an incorrect username. Expected <User Doesn't Exist> message")
        # Login with an inexisting username
        response = self.client.post("/", {"userName": "ret8578", "password": self.adminUser.password})
        self.assertEqual("User Doesn't Exist", response.context['errorMessage'],
                         "Log in with an incorrect username. Expected <User Doesn't Exist> message")

        # Login with an inexisting password
        response = self.client.post("/", {"userName": self.standardUser.userName, "password": "eddee"})
        self.assertEqual("Incorrect Password!", response.context['errorMessage'],
                         "Log in with an incorrect password. Expected <Incorrect Password!> message")
        # Login with an inexisting username
        response = self.client.post("/", {"userName": self.adminUser.userName, "password": "eddee"})
        self.assertEqual("Incorrect Password!", response.context['errorMessage'],
                         "Log in with an incorrect password. Expected <Incorrect Password!> message")

    def test_unmatching_credentials(self):#we test existing username and password that do not match
        #Login with a standard username and admin password
        response = self.client.post("/", {"userName": self.standardUser.userName, "password": self.adminUser.password })
        self.assertEqual("Incorrect Password!", response.context['errorMessage'],
        "Log in with an incorrect password. Expected <Incorrect Password!> message")
        # Login with a standard password and admin username
        response = self.client.post("/", {"userName": self.adminUser.userName, "password": self.standardUser.password})
        self.assertEqual("Incorrect Password!", response.context['errorMessage'],
                         "Log in with an incorrect password. Expected <Incorrect Password!> message")