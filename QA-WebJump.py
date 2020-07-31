#Exercício para Automação Web - WebJump

#Bibliotecas
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://wejump-automation-test.github.io/qa-test/")
driver.maximize_window()

#Clica e verifica existência dos botões do Box Buttons
class ClickButtons ():
    def __init__(self):
        pass

    def ClicaBotao (self):
        botaoOne = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'One')]")
        botaoOne.click()
        botaoTwo = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Two')]")
        botaoTwo.click()
        botaoFour = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Four')]")
        botaoFour.click()

    def Verifica (self):
        pass

    def run (self):
        self.ClicaBotao()  

class LastScene ():
    def __init__(self):
        pass

    def nameField(self): #preencher o campo "YourFirstName" com um texto qualquer
        nameField = driver.find_element_by_xpath("//div[@class='form-group']//input[@placeholder='YourFirstName']")
        nameField.send_keys("Henrique")

    def ClickBotOne (self): #Clique no botão "One"
        botaoOne = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'One')]")
        botaoOne.click()

    def CheckBox(self): #cheque a opção "OptionThree"
        checkOption = driver.find_element_by_xpath("//div[@class='checkbox']//input[@id='opt_three']")
        checkOption.click()

    def SelectFromList (self): #selecione a opção "ExampleTwo" dentro da select box
        FromListOption = driver.find_element_by_xpath("//select[@id='select_box']//option[@value='option_two']")
        FromListOption.click()

    def VisibilityOfSeleniumImg (self): #valide a presença da imagem do logo do "Selenium Webdriver"
        try:
            ImgPresence = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='panel_body_three']//img[@alt='selenium']")))
            print ("It's visible!")
        except: 
            print ("Sorry, We couldn't find anything!")
    
    def run (self):
        self.nameField()
        self.ClickBotOne()      
        self.CheckBox()
        self.SelectFromList()
        self.VisibilityOfSeleniumImg()  

class ClickIFrameButtons ():
    def __init__(self):
        pass

    def iFrameAccess (self):
        iframe = driver.find_element_by_xpath("//iframe[@src='buttons.html']")
        driver.switch_to_frame(iframe)

    def ClicaBotao (self):
        botaoOneiframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'One')]")
        botaoOneiframe.click()
        botaoTwoiframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'Two')]")
        botaoTwoiframe.click()
        botaoFouriframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'Four')]")
        botaoFouriframe.click()
        driver.switch_to_default_content()

    def Verifica (self):
        pass    

    def run (self):
        self.iFrameAccess()
        self.ClicaBotao()

#CB = ClickButtons() #CLASSE DO CENÁRIO 1 
#CIF = ClickIFrameButtons() #CLASSE DO CENÁRIO 2
LS = LastScene() #CLASSE DO CENÁRIO 3
#CB.run() #EXERCUTA CENÁRIO 1
#CIF.run() #EXECUTA CENÁRIO 2
LS.run() #EXECUTA CENÁRIO 3
