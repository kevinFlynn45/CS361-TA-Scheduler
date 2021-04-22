from django.test import TestCase
from django.test import Client
from .createLabFunctions import createLabFunctions


# Create your tests here.

class testCreateSection(TestCase):
    def setUp(self):
        self.client = Client()

    def acceptance_testCreateSection(self):
        response = self.client.post("/create-section/", {"sectionNumber": "1", "sectionName": "Section 1"})
        section_list = response.context["section_list"]
        testSection = section_list[0]
        self.assertEqual("1", str(testSection[0]), "New section creation failed at sectionNumber")
        self.assertEqual("Section 1", str(testSection[1]), "New section creation failed at sectionName")
        self.assertEqual("", response.context["errorMessage"],
                         "Error creating new section, errorMessage should be empty")

    def unit_testCreateSection(self):
        errorMessage = createLabFunctions.createLab(labNumber="1", labName="Section 1")
        self.assertEqual("", errorMessage, "Error creating new section, errorMessage should be empty")


class testDuplicateSection(TestCase):  # testing if sectionNumber already exists
    def setUp(self):
        self.client = Client()
        self.newLab = createLabFunctions.createLab(labNumber="1", labName="Section 1")

    def acceptance_testDuplicateSection(self):
        response = self.client.post("/create-section/", {"sectionNumber": "1", "sectionName": "Section 1"})
        self.assertEqual("Lab Number Already Exists", response.context["errorMessage"],
                         "Error creating new section, labNumber already exists")

    def unit_testDuplicateSection(self):
        errorMessage = createLabFunctions.createLab(labNumber="1", labName="Section 1")
        self.assertEqual("Lab Number Already Exists", errorMessage,
                         "Error creating new section, labNumber already exists")


class testSectionInput(TestCase):  # testing if sectionNumber is a number
    def setUp(self):
        self.client = Client()

    def acceptance_testInput(self):
        response = self.client.post("/create-section/", {"sectionNumber": "one", "sectionName": "Section 1"})
        self.assertEqual("Lab Number Isn't Numeric", response.context["errorMessage"],
                         "Error creating new section, labNumber is not a number")

    def unit_testInput(self):
        errorMessage = createLabFunctions.createLab(labNumber="one", labName="Section 1")
        self.assertNotEqual("Lab Number Isn't Numeric", errorMessage,
                            "Error creating new section, labNumber is not a number")
