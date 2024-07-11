import time
import allure
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


scenarios('../features/login.feature')


@allure.feature("Login")
@allure.story("Tester Login pour l'application GP4YOU")
@given('l\'utilisateur est sur la page de connexion de GP4YOU')
@allure.step("l'utilisateur est sur la page de connexion de GP4YOU")
def user_on_login_page(driver):
    driver.get('https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/login/')
    time.sleep(7)
    
@when('l\'utilisateur saisit le nom d\'utilisateur "SBCEE"')
@allure.step("l'utilisateur saisit le nom d'utilisateur 'SBCEE'")
def enter_username(driver):
    xpath_login = "//div[@id='root']/div//form/div/div[2]/div[@class='input-fields input-fields-default text-black']/input"
    login_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_login)))
    login_locator.send_keys("SBCEE")
    time.sleep(2)

@when('l\'utilisateur saisit le mot de passe "HRHR"')
@allure.step("l'utilisateur saisit le mot de passe 'HRHR'")
def enter_password(driver):
    xpath_password = "//div[@id='root']/div//form/div/div[3]/div[@class='input-fields input-fields-default text-black']/input"
    password_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_password)))
    password_locator.send_keys("HRHR")
    time.sleep(2)

@when('l\'utilisateur sélectionne la langue "French"')
@allure.step("l'utilisateur sélectionne la langue 'French'")
def select_language(driver):
    xpath_select = "//div[@id='root']/div//form//select[@name='lang']"
    lang_dropdown_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_select)))
    lang_dropdown = Select(lang_dropdown_locator)
    time.sleep(1)
    lang_dropdown.select_by_visible_text("French")
    allure.attach(driver.get_screenshot_as_png(), name="page_login", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@when('l\'utilisateur clique sur le bouton "Connexion"')
@allure.step("l'utilisateur clique sur le bouton 'Connexion'")
def click_login_button(driver):
    xpath_submit_button = "//div[@id='root']//form//button[.='Connexion']"
    submit_button_locator = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath_submit_button)))
    submit_button_locator.click()

@then('l\'utilisateur devrait être redirigé vers la page d\'accueil de GP4YOU')
@allure.step("l'utilisateur devrait être redirigé vers la page d'accueil de GP4YOU")
def verify_redirection(driver):
    WebDriverWait(driver, 60).until(EC.url_to_be("https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/"))
    actual_url = driver.current_url
    assert actual_url == "https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/"

@then('l\'URL devrait être "https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/"')
@allure.step("l'URL devrait être 'https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/'")
def verify_url(driver):
    actual_url = driver.current_url
    assert actual_url == "https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/"
    driver.refresh()
    time.sleep(5)


