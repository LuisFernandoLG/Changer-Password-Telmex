from telmexbot import  TelmexBot
from data import modem
import time


ip = modem["ip"]
password = modem["password"]

class Wifi(TelmexBot):

    def __init__(self, ip=ip, password=password):
        super().__init__(ip, password)

        self.__typeOfBand = None
        self.__newPassword = None

    def __GotoPageWifi(self):

        self.login()
        print
        if self.__typeOfBand == "5_0":

            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()

            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[7]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[7]").click()


            return "Login con exito"

        else:
            

            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()
            
            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[6]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[6]").click()
            
            return "Login con exito"


    def __SetNewPassword(self):
        self.__GotoPageWifi()

        #Go to a frame
        self.driver.switch_to.frame(self.driver.find_element_by_id("mainFrame"))

        time.sleep(10)
        #Scroll Down
        #esta funcion lleva la vista hasta donde está el elemento
        self.driver.find_element_by_id(
            "wpakey_hidden").location_once_scrolled_into_view

        #clear the field
        self.driver.find_element_by_id("wpakey_hidden").click()
        self.driver.find_element_by_id("wpakey_hidden").clear()
        self.driver.find_element_by_id("wpakey_hidden").click()
        #insert new password
        self.driver.find_element_by_id(
            "wpakey_hidden").send_keys(self.__newPassword)

        self.driver.find_element_by_css_selector("html body div.container form div.row.button-position input.buttonX.button-sm").location_once_scrolled_into_view

        self.driver.find_element_by_css_selector("html body div.container form div.row.button-position input.buttonX.button-sm").submit()

        self.driver.quit()
        return "Contraseña cambiada con exito"

    def changePassword(self, newPassword:str, typeOfBand:str) -> str:
        self.__newPassword = newPassword
        self.__typeOfBand = typeOfBand

        return self.__SetNewPassword()

