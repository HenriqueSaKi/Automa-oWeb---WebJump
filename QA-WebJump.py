# Exercício para Automação Web - WebJump

# Bibliotecas
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://wejump-automation-test.github.io/qa-test/")
driver.maximize_window()


# Clica e verifica existência dos botões do Box Buttons
class ClickButtons():
    # Função de inicialização da classe
    def __init__(self):
        pass

    # Procura e clica nos botões selecionados
    def ClicaBotao(self):
        botaoOne = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'One')]")
        botaoOne.click()
        botaoTwo = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Two')]")
        botaoTwo.click()
        botaoFour = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Four')]")
        botaoFour.click()

    # Verifica a existência dos botões
    def VerificaBox(self):
        pass

    # Executa todas as tarefas da classe
    def run(self):
        self.ClicaBotao()

    # Clica e verifica existência dos botões no iframe


class ClickIFrameButtons():
    # Função de inicialização da classe
    def __init__(self):
        pass

    # Acessa o iframe, para realizar modificações nele
    def iFrameAccess(self):
        iframe = driver.find_element_by_xpath("//iframe[@src='buttons.html']")
        driver.switch_to_frame(iframe)

    # Procura e clica nos botões selecionados
    def ClicaBotao(self):
        botaoOneiframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'One')]")
        botaoOneiframe.click()
        botaoTwoiframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'Two')]")
        botaoTwoiframe.click()
        botaoFouriframe = driver.find_element_by_xpath("//div[@class='col-sm-12']//button[contains(text(),'Four')]")
        botaoFouriframe.click()
        driver.switch_to_default_content()

    # Verifica a existência dos botões no iframe
    def VerificaIframe(self):
        pass

        # Executa todas as tarefas da classe

    def run(self):
        self.iFrameAccess()
        self.ClicaBotao()


class LastScene():
    # Função de inicialização da classe
    def __init__(self):
        pass

    # Preencher o campo "YourFirstName" com um texto qualquer
    def nameField(self):
        nameField = driver.find_element_by_xpath("//div[@class='form-group']//input[@placeholder='YourFirstName']")
        nameField.send_keys("Henrique")

    # Clique no botão "One"
    def ClickBotOne(self):
        botaoOne = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'One')]")
        botaoOne.click()

    # Cheque a opção "OptionThree"
    def CheckBox(self):
        checkOption = driver.find_element_by_xpath("//div[@class='checkbox']//input[@id='opt_three']")
        time.sleep(0.5)
        checkOption.click()

    # Selecione a opção "ExampleTwo" dentro da select box
    def SelectFromList(self):
        FromListOption = driver.find_element_by_xpath("//select[@id='select_box']//option[@value='option_two']")
        FromListOption.click()

    # Verifica a existência da imagem com o logo do "selenium"
    def VisibilityOfSeleniumImg(self):  # valide a presença da imagem do logo do "Selenium Webdriver"
        try:
            ImgPresence = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='panel_body_three']//img[@alt='selenium']")))
            # print ("It's visible!")
            if ImgPresence.is_displayed():
                pyautogui.alert(text="Selenium logo is visible!", title="Alert!", button="Ok")
        except:
            # print ("Sorry, We couldn't find anything!")
            pyautogui.alert(text="Sorry, We couldn't find anything!", title="Alert!", button="Ok")

    # Executa todas as tarefas da classe
    def run(self):
        self.nameField()
        self.ClickBotOne()
        self.CheckBox()
        self.SelectFromList()
        self.VisibilityOfSeleniumImg()

    # Para a realização dos testes, deve-se descomentar a classe e seu respectivo "executa cenário"


# CB = ClickButtons() #CLASSE DO CENÁRIO 1
# CIF = ClickIFrameButtons() #CLASSE DO CENÁRIO 2
LS = LastScene()  # CLASSE DO CENÁRIO 3
# CB.run() #EXERCUTA CENÁRIO 1
# CIF.run() #EXECUTA CENÁRIO 2
LS.run()  # EXECUTA CENÁRIO 3
