#Librerias necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from data import ip, passwordModem




class ChangerPasswordTelmex():
    def __init__(self, ip = ip, passwordModem = passwordModem):
        self.__newPassword = ""
        self.__ip = ip
        self.__passwordModem = passwordModem
        self.__driver = None
    
    def __getPage(self):
        try:
            self.__driver = webdriver.Firefox()
            self.__driver.get(self.__ip)
            self.__driver.implicitly_wait(20)


            print("Pagina obtenida con éxito . . . ")
            return  "Ok"

        except Exception as e:
            print("Error al obtener la pagina ")
            return e

    def __login(self):
        try:

            self.__getPage()

            #introducir contraseña
            self.__driver.find_element_by_id("password").click()
            self.__driver.find_element_by_id("password").send_keys(self.__passwordModem)

            #click en el "acceso"
            self.__driver.find_element_by_name("loginBT").click()


            print("Login éxitoso . . . ")
            return "Ok"
        
        except Exception as e:
            print("Error Login . . . ")
            return e

    def __goToLinkWifi(self):
        try:
            self.__login()
            
            self.__driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()
            self.__driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]").click()


            self.__driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[6]").click()
            self.__driver.find_element_by_xpath(
                "/html/body/div/section/div[1]/div/div[1]/ul[2]/li[6]").click()
              

            

            
            print("Ir a la pagin para cambiar password exitoso ")
            return "Ok"

        except Exception as e:
            print("Error al navegar a la pagina de change password ")
            return e

    def ChangeToNewPassword(self, newPassword):
        try:
            self.__goToLinkWifi()

            #Go to a frame
            self.__driver.switch_to.frame(self.__driver.find_element_by_id("mainFrame"))


            time.sleep(15)
            #Scroll Down
            #esta funcion lleva la vista hasta donde está el elemento
            self.__driver.find_element_by_id("wpakey_hidden").location_once_scrolled_into_view

            #clear the field
            self.__driver.find_element_by_id("wpakey_hidden").click()
            self.__driver.find_element_by_id("wpakey_hidden").clear()
            self.__driver.find_element_by_id("wpakey_hidden").click()
            #insert new password
            self.__driver.find_element_by_id("wpakey_hidden").send_keys(newPassword)

            
            
            self.__driver.find_element_by_css_selector("html body div.container form div.row.button-position input.buttonX.button-sm").location_once_scrolled_into_view

            #self.__driver.find_element_by_css_selector("html body div.container form div.row.button-position input.buttonX.button-sm").submit()

            #self.__driver.quit()

            print("COntraseña cambiada")
            return "Password updated successfuly"

        except Exception as e:
            print("error al cambiar la contraseña")
            return e
