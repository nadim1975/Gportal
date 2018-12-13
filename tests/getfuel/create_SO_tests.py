from pages.getfuel.create_SO_page import CreateSalesOrderPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import Status
import unittest
import pytest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RequestFuelTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.so = CreateSalesOrderPage(self.driver)
        self.ts = Status(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateHome()

    @pytest.mark.run(order=1)
    #@data(("JavaScript for beginners","4143202652384595","1220","101"),("Learn Python 3 from scratch","41426543764387900","1221","303"))
    #you can provide with only with the file name without the path since it is saved under the project
    @data(*getCSVData("/Users/nhussein/PycharmProjects/Gportal/testdata.csv"))
    @unpack
    def test_validateSoCreation(self,icao,airportName,tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDay,arrivalHour,arrivalMin,departureDay,departureHour,departureMin):
        self.so.enterTripInformation(icao,airportName,tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDay,arrivalHour,arrivalMin,departureDay,departureHour,departureMin)
        self.so.clickRequestFuel()
        # self.so.getQuoteNumber()
        # self.so.getSoNumber()
        result = self.so.verifySOcreated()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

        self.so.clickCloseRequest()
        