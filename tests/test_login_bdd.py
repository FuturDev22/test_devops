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
@allure.story("Tester Login")
@given("L\'utilisateur ouvre la page de connexion")
@allure.step("L'utilisateur ouvre la page de connexion")
def user_open_login_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

@when("L\'utilisateur saisit le nom d'utilisateur et le mot de passe")
@allure.step("L'utilisateur saisit le nom d'utilisateur et le mot de passe")
def enter_credentials(driver):
    username_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "username")))
    username_locator.send_keys("student")
    time.sleep(2)
    password_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "password")))
    password_locator.send_keys("Password123")
    time.sleep(2)

@when("L\'utilisateur clique sur submit")
@allure.step("L'utilisateur clique sur submit")
def submit_click(driver):
    submit_button_locator = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn']")))
    submit_button_locator.click()
    time.sleep(2)
@then("L\'utilisateur doit voir URL https://practicetestautomation.com/logged-in-successfully/")
@allure.step("l'utilisateur doit voir URL https://practicetestautomation.com/logged-in-successfully/")
def voir_url(driver):
    actual_url = driver.current_url
    assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
    
@then("L\'utilisateur doit voir le message Logged In Successfully")
@allure.step("L'utilisateur doit voir le message Logged In Successfully")
def voir_message(driver):
    text_locator = driver.find_element(By.TAG_NAME, "h1")
    actual_text = text_locator.text
    assert actual_text == "Logged In Successfully"
    
@then("L\'utilisateur doit voir le bouton de déconnexion")
@allure.step("L'utilisateur doit voir le bouton de déconnexion")
def voir_bouton(driver):
    log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
    assert log_out_button_locator.is_displayed()
    time.sleep(5)

