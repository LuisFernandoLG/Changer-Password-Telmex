from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from data import modem

class TelmexBot():

    def __init__(self, ip, passwordOfRouter):

        self.ip = ip
        self.passwordOfRouter = passwordOfRouter

        self.driver = None
        
    #First Steps
    def getPage(self):
        try:
            self.driver = webdriver.Firefox()

            self.driver.get(self.ip)
                

            print("Pagina obtenida con éxito . . . ")
            return "Ok"

        except Exception as e:
            raise e

    def login(self):
        try:

            self.getPage()

            #introducir contraseña
            self.driver.find_element_by_id("password").click()
            self.driver.find_element_by_id("password").send_keys(self.passwordOfRouter)
            #click en el "acceso"
            self.driver.find_element_by_name("loginBT").click()

            print("Login éxitoso . . . ")
            return "Ok"

        except Exception as e:
            print("Error Login . . . ")
            return e
