import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select




class MyTestCase(unittest.TestCase):
    userName = "demotesting"
    pwd = "demo@123"
    groupDesc="HelloTest"
    startDate="2019-11-24"
    endDate="2019-11-24"

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='E:\PythonProjects\SeleniumPythonProject\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://saya.incois.gov.in/")

    def login(self):
        self.driver.find_element_by_name('txtActorUserName').send_keys(MyTestCase.userName)
        self.driver.find_element_by_id("txtActorPassword").send_keys(MyTestCase.pwd)
        self.driver.find_element_by_id("btnLogin").click()

    def goToMySignage(self):
        self.actions = ActionChains(self.driver)
        self.mySignage = self.driver.find_element_by_xpath("(//*[@data-toggle='dropdown'])[2]")
        self.actions.move_to_element(self.mySignage).perform()

    def goToMyDisplays(self):
        self.driver.find_element_by_xpath("//span[@class='fa fa-object-group']").click()

    def creategroup(self,value):
        groupName=self.driver.find_element_by_id("txtGroupName")
        groupName.send_keys(value)
        groupName1 = groupName.get_attribute("value")
        print("Attribute is " +groupName1)
        self.driver.find_element_by_id("txtDesc").send_keys(MyTestCase.groupDesc)
        self.driver.find_element_by_id("txtStartDate").send_keys(MyTestCase.startDate)
        time.sleep(1)
        startTime = self.driver.find_element_by_id("txtStartTime")
        self.driver.execute_script("arguments[0].value='00:01:01';", startTime)
        time.sleep(1)
        self.driver.find_element_by_id("txtEndDate").send_keys(MyTestCase.endDate)
        time.sleep(1)
        endTime = self.driver.find_element_by_id("txtEndTime")
        self.driver.execute_script("arguments[0].value='20:59:59';", endTime)
        self.driver.find_element_by_name("btnSave").click()
        return groupName1

    def goToIncoisApps(self,value):
        #self.selectGroupName=self.creategroup()
        print("Created Group Name" +value)
       # time.sleep(2)
        self.goToMySignage()
        self.mySignageIncoisApps = self.mySignage.find_element_by_xpath("//*[contains(text(),' IncoisApps')]").click()
        self.select = Select(self.driver.find_element_by_name("ctl00$ContentPlaceHolder1$ddlGroup"))
        self.select.select_by_visible_text('SG: ' +value)
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSearch").click()
        time.sleep(10)
        self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_chkAOIPfz").click()
        time.sleep(5)

    def select_multipleStates(self):
       self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlPfzStates").click()
       time.sleep(3)
       clickMultipleStates = self.addMultipleStates()
       print(clickMultipleStates.__len__())
       for i in clickMultipleStates:
         self.driver.find_element_by_xpath("//span[text()='"+i+"']/../ input[@ type='checkbox']").click()

         # span[text() = '"+i+"'] /../ input[ @ type = 'checkbox']
    def addMultipleStates(self):
           a=[]
           a.append("NORTH TAMILNADU")
           a.append("NICOBAR")
           for states in a:
            print("States are"+states)
           return a

    def test_testCase(self):
        self.login()
        self.goToMySignage()
        self.goToMyDisplays()
        createdGroupName = self.creategroup('HelloTest')
        self.goToIncoisApps(createdGroupName)
        self.select_multipleStates()


if __name__ == '__main__':
     unittest.main()


