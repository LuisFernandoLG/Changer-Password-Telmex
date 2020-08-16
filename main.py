from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#new
import time

password_modem = "4992070890"

driver = webdriver.Firefox()

driver.get("http://192.168.1.254")


#element = driver.find_element_by_id("js-link-box-en")

#print(element.text)
#print(element.get_attribute("href"))
#element.click()

#introducir contraseña
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").send_keys(password_modem)


#click en el "acceso"
driver.find_element_by_name("loginBT").click()


red = driver.find_element_by_css_selector(
    "ul.x_main_menu:nth-child(2) > li:nth-child(1)")
print(red.text)
red.click()
red.click()

wifi = driver.find_element_by_css_selector("ul.x_main_menu:nth-child(2) > li:nth-child(6)")
wifi.click()

nameIframe = "mainFrame"
"""
try:
    vote = driver.find_element_by_xpath("wpakey_hidden")
    vote.click()
except Exception as e:
    print(e)
"""


#Seleccinamos el iframe

time.sleep(7)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))


#Ahora estamos dentro del iframe
fieldNewPassword = driver.find_element_by_id("wpakey_hidden")

fieldNewPassword.click()
fieldNewPassword.clear()
fieldNewPassword.click()

newPassword = "nomelase.com"
#newPassword = "01123581321"

fieldNewPassword.send_keys(newPassword)

guardar = driver.find_element_by_css_selector("html body div.container form div.row.button-position input.buttonX.button-sm")
#guardar.submit()



#volver a la selección principal
#driver.switch_to.default_content()
