from telmexbot import TelmexBot
from selenium.webdriver.common.keys import Keys

from data import modem
import  time


ip = modem["ip"]
password = modem["password"]


class AdressMac(TelmexBot):

    def __init__(self, ip=ip, password=password):
        super().__init__(ip, password)

        self.__adressMacToBlock = None

    
    def __GoToSecurityPage(self):

        self.login()

        self.driver.find_element_by_xpath(
            "/html/body/div/section/div[1]/div/div[1]/ul[3]").click()
        self.driver.find_element_by_xpath(
            "/html/body/div/section/div[1]/div/div[1]/ul[3]").click()
        

        self.driver.find_element_by_xpath(
            "/html/body/div/section/div[1]/div/div[1]/ul[3]/li[3]").click()

        self.driver.find_element_by_xpath(
            "/html/body/div/section/div[1]/div/div[1]/ul[3]/li[3]").click()

        return "ok"
    

    def __getIframe(self):
        self.__GoToSecurityPage()
        self.driver.switch_to.frame(
            self.driver.find_element_by_id("mainFrame"))
        time.sleep(4)
    
    def __SetMacToField(self):
        self.__getIframe()

        self.driver.find_element_by_xpath(
            "/html/body/div/div/form[2]/div[4]/div[2]/div/input").location_once_scrolled_into_view

        self.driver.find_element_by_xpath(
            "/html/body/div/div/form[2]/div[4]/div[2]/div/input").click()
            
        self.driver.find_element_by_xpath(
            "/html/body/div/div/form[2]/div[4]/div[2]/div/input").send_keys(self.__adressMacToBlock)


    def __save(self):

        self.__SetMacToField()

        self.driver.find_element_by_xpath(
            "/html/body/div/div/form[2]/div[4]/div[2]/div/input").send_keys(Keys.ENTER)

        return "Dispositivo blioqueado con exito"

    def block(self, adressMac: str) -> str:
        self.__adressMacToBlock = adressMac

        self.__save()
        return "yes listo"
