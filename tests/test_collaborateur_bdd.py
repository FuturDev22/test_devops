import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then
from test_login_bdd import user_on_login_page, enter_username, enter_password, select_language, click_login_button, verify_redirection

scenarios('../features/collaborateur.feature')

@given('le collaborateur est connecté')
def login(driver):
    user_on_login_page(driver)
    enter_username(driver)
    enter_password(driver)
    select_language(driver)
    click_login_button(driver)
    verify_redirection(driver)
##########etat civil #######
@when('le collaborateur navigue vers "Mes données individuelles"')
@allure.step('le collaborateur navigue vers "Mes données individuelles"')
def navigate_to_donnees_indiv(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/li[1]/div[.='Mes données individuelles']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@when('le collaborateur clique sur "Mon état civil"')
@allure.step('le collaborateur clique sur "Mon état civil"')
def click_etat_civil(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW018E0']//span[.='Mon état civil']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@when('le collaborateur modifie la date d\'effet de son état civil "Mariée" du "05/10/2014" à "06/10/2014"')
@allure.step('le collaborateur modifie la date d\'effet de son état civil "Mariée" du "05/10/2014" à "06/10/2014"')
def modify_marital_status(driver):
    # Select "Mariée"
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='flex-column-start full-width table-body']/div/div[1]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

    # Change effective date
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']/div/div[@class='full-height full-width']/div[2]/div/div/div/button[@type='button']"
    calendar_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    calendar_locator.click()
    time.sleep(3)

    xpath = "//div[@role='dialog']/div[2]//div[@role='grid']/div[2]/div[1]/button[@type='button']"
    date_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    date_locator.click()
    allure.attach(driver.get_screenshot_as_png(), name="etat_civil_form", attachment_type=allure.attachment_type.PNG)
    time.sleep(3)

    # Click modify button
    xpath = "//button[@id='button-edit']"
    modify_button_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    modify_button_locator.click()
    time.sleep(3)


##### annuler modification etat civil ######
@when('le collaborateur navigue vers "Mes demandes"')
@allure.step('le collaborateur navigue vers "Mes demandes"')
def navigate_to_mes_demandes(driver):
    # mes demandes button
    xpath_mes_demandes_button = "[href='\/GP4You\/requests']"
    mes_demandes_button_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, xpath_mes_demandes_button)))
    mes_demandes_button_locator.click()
    allure.attach(driver.get_screenshot_as_png(), name="mes_demandes", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@when('le collaborateur sélectionne la demande de modification à annuler')
@allure.step('le collaborateur sélectionne la demande de modification à annuler')
def select_request_to_cancel(driver):
    # checkbox button annuler
    xpath_checkbox_annuler = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='flex-column-start full-width table-body']/div[1]/div[1]//i"
    checkbox_annuler_button_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_checkbox_annuler)))
    checkbox_annuler_button_locator.click()
    time.sleep(2)

@then('le collaborateur clique sur "Annuler"')
@allure.step('le collaborateur clique sur "Annuler"')
def click_annuler(driver):
    # button annuler
    xpath_button_annuler = "//div[@id='root']/div/div[3]//button[.='Annuler']"
    annuler_button_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_button_annuler)))
    annuler_button_locator.click()
    time.sleep(3)

######## adresse et telephone #######
@when('le collaborateur navigue vers "Mon adresse et mon téléphone"')
@allure.step('le collaborateur navigue vers "Mon adresse et mon téléphone"')
def navigate_to_adresse_telephone(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/li[1]/div[.='Mes données individuelles']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW00FE0']//span[.='Mon adresse et mon téléphone']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@then('le collaborateur ajoute une nouvelle adresse de résidence')
@allure.step('le collaborateur ajoute une nouvelle adresse de résidence')
def add_address(driver):
    # ajouter adresse(plus) button
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='tooltip tooltip-align-bottom']/div/i"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # adresse Type input
    xpath = "//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(1)

    # choix type adresse de résidence
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[2]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # pays input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']/div/div[@class='full-height full-width']/div[3]/div[@class='full-width']/div/div/div/div[@class='css-60hgb7']/div[@role='combobox']//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(1)
    locator.send_keys("came")
    time.sleep(2)

    # choix pays cameroun
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[1]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # date debut input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[4]/div/div/input"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("08/11/2022")
    time.sleep(2)

    # adresse input
    xpath = "//input[@id='ZONADA']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("Abidjan. Immeuble de l'Indust")
    time.sleep(2)

    # ville input
    xpath = "//input[@id='ZONADC']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("Abidjan")
    allure.attach(driver.get_screenshot_as_png(), name="adresse_telephone_form", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

    # button ajouter
    xpath = "//button[@id='button-add']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="adresse_telephone_page", attachment_type=allure.attachment_type.PNG)
    time.sleep(1)

@then('le collaborateur ajoute une nouvelle adresse émail "adélaide.ouattara@soprahr.com"')
@allure.step('le collaborateur ajoute une nouvelle adresse émail "adélaide.ouattara@soprahr.com"')
def add_email(driver):
    # email input
    xpath = "//input[@id='EMAILS']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("adélaide.ouattara@soprahr.com")
    time.sleep(3)
    # button envoyer
    # xpath = "//button[@id='button-submit']"
    # locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # locator.click()
    # time.sleep(4)

######## personnes à charge #######
@when('le collaborateur navigue vers "Personnes à charge"')
@allure.step('le collaborateur navigue vers "Personnes à charge"')
def navigate_to_personnes_a_charge(driver):
    # xpath = "//div[@id='root']/div//ul[@class='full-width']/li[1]/div[.='Mes données individuelles']"
    # locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # locator.click()
    # time.sleep(2)

    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW0E5E0']//span[.='Personnes à charge']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@then('le collaborateur ajoute une nouvelle personne à charge')
@allure.step('le collaborateur ajoute une nouvelle personne à charge')
def add_dependant(driver):
    # ajouter (plus) button
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='card-body']/div[2]/div[@class='tooltip tooltip-align-bottom']/div/i"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # nom input
    xpath = "//input[@id='NOMPAR']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("Ouattara")
    time.sleep(2)

    # prenom input
    xpath = "//input[@id='PREENF']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("Mamadou")
    time.sleep(2)

    # genre input
    xpath = "//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # choix genre masculin
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[2]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # date naissance input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[4]/div/div/input"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("12/06/2020")
    time.sleep(2)

    # parenté input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']/div//select[@name='TYPPAR']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # choix parenté enfant
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//select[@name='TYPPAR']/option[@value='2']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    locator.click()
    time.sleep(2)

    # button ajouter
    xpath = "//button[@id='button-add']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="personne_a_charge_page", attachment_type=allure.attachment_type.PNG)
    time.sleep(1)

### contacts d'urgence #####
@when('le collaborateur navigue vers "Personnes à contacter"')
@allure.step('le collaborateur navigue vers "Personnes à contacter"')
def navigate_to_personnes_a_contacter(driver):
    # xpath = "//div[@id='root']/div//ul[@class='full-width']/li[1]/div[.='Mes données individuelles']"
    # locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # locator.click()
    # time.sleep(2)

    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW0PPE0']//span[.='Personnes à contacter']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@then('le collaborateur modifie les informations du contact d\'urgence')
@allure.step('le collaborateur modifie les informations du contact d\'urgence')
def modify_contact_urgence(driver):
    # ligne à modifier button
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='flex-column-start full-width table-body']/div/div[1]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

    # ordre input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']/div//select[@name='NUMORD']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(1)

    # choix ordre '1'
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//select[@name='NUMORD']/option[@value='1']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # numero input
    xpath = "//input[@id='TELPHO']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("0614345978")
    time.sleep(2)

    # modifier button
    xpath = "//button[@id='button-edit']"
    locator = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="contacts_urgence_page", attachment_type=allure.attachment_type.PNG)
    time.sleep(1)

    # bouton envoyer
    # xpath = "//button[@id='button-submit']"
    # locator = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # locator.click()
    # time.sleep(3)

### coordonnées bancaires ####
@when('le collaborateur navigue vers "Mes coordonnées bancaires"')
@allure.step('le collaborateur navigue vers "Mes coordonnées bancaires"')
def navigate_to_coordonnees_bancaires(driver):
    # xpath = "//div[@id='root']/div//ul[@class='full-width']/li[1]/div[.='Mes données individuelles']"
    # locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # locator.click()
    # time.sleep(2)

    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW00IE0']/div"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@then('le collaborateur modifie ses coordonnées bancaires')
@allure.step('le collaborateur modifie ses coordonnées bancaires')
def modify_coordonnees_bancaires(driver):
    # ligne à modifier button
    xpath = "//div[@id='root']/div/div[3]//div[@class='flex-column-start full-width table-body']/div/div[1]/div[.='Adélaïde OUATTARA']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # pays input
    xpath = "//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()  # Ensure the input is focused
    locator.send_keys(Keys.CONTROL + "a")
    locator.send_keys(Keys.DELETE)
    locator.send_keys("came")
    time.sleep(1)

    # choix pays cameroun
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[1]"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # date debut input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[3]/div/div/input"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("17/02/2022")
    time.sleep(2)

    # date fin input
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[4]/div/div/input"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("17/02/2025")
    time.sleep(2)

    # libellé banque input
    xpath = "//input[@id='LIBBAN']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("IBAN Banque")
    time.sleep(2)

    # modifier button
    xpath = "//button[@id='button-edit']"
    locator = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="coordonnees_bancaires_page", attachment_type=allure.attachment_type.PNG)
    time.sleep(1)


####### absences ########
@when('le collaborateur navigue vers "Mes absences"')
@allure.step('le collaborateur navigue vers "Mes absences"')
def navigate_to_mes_absences(driver):
    xpath = "//div[@id='root']/div/div[3]//ul[@class='full-width']//div[.='Mes absences']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

@when('le collaborateur navigue vers "Demande d\'absence"')
@allure.step('le collaborateur navigue vers "Demande d\'absence"')
def navigate_to_request_absence(driver):
    # demande absence button
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW0AGE0']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="demande_absence_page", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

@then('le collaborateur ajoute une demande une absence')
@allure.step('le collaborateur ajoute une demande une absence')
def request_absence(driver):
    # ajouter absence(plus) button
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='tooltip tooltip-align-bottom']/div/i"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

    # absence Type input
    xpath = "//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(1)

    # choix type absence congés de mariage
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[7]"
    mariage_locator = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    mariage_locator.click()
    time.sleep(2)

    # champ date debut
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[2]/div/div/input"
    debut_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    debut_locator.send_keys("30/06/2024")
    time.sleep(2)

    # champ date fin
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']//div[@class='full-height full-width']/div[3]/div/div/input"
    fin_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    fin_locator.send_keys("15/07/2024")
    allure.attach(driver.get_screenshot_as_png(), name="demande_absence_form", attachment_type=allure.attachment_type.PNG)
    time.sleep(2)

    # button ajouter
    xpath = "//button[@id='button-add']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(4)

@when('le collaborateur navigue vers "mon planning des absences"')
@allure.step('le collaborateur navigue vers "mon planning des absences"')
def navigate_to_absence_planning(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASCSALE5']//span[.='Mon planning des absences']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="planning_absences_mensuelle", attachment_type=allure.attachment_type.PNG)


@then('le collaborateur voit son planning des absences en vue annuelle')
@allure.step('le collaborateur voit son planning des absences en vue annuelle')
def annuel_absence_planning(driver):
    xpath = "//div[@id='year']/i"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="planning_absences_annuelle", attachment_type=allure.attachment_type.PNG)


@when('le collaborateur navigue vers "calendrier d\'équipe"')
@allure.step('le collaborateur navigue vers "calendrier d\'équipe"')
def view_team_calendar(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASCSALM5']/div"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="calendrier_equipe", attachment_type=allure.attachment_type.PNG)


@then('le collaborateur navigue vers "historique des absences"')
@allure.step('le collaborateur navigue vers "historique des absences"')
def view_absence_history(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASCSALE6']//span[.='Historique des absences']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="historique_absences", attachment_type=allure.attachment_type.PNG)


######## compétences #####
@when('le collaborateur navigue vers "Mes compétences"')
@allure.step('le collaborateur navigue vers "Mes compétences"')
def navigate_to_mes_competences(driver):
    xpath = "//div[@id='root']/div/div[3]//ul[@class='full-width']//div[.='Mes compétences']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

@when('le collaborateur ajoute une nouvelle compétence "Adaptabilité"')
@allure.step('le collaborateur ajoute une nouvelle compétence "Adaptabilité"')
def add_competence(driver):
    # update competence button
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASW03DE0']//span[.='Mettre à jour mes compétences']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

    # add competence button
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='card-body']/div[2]/div[@class='tooltip tooltip-align-bottom']/div/i"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # competence button
    xpath = "//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # choix compétence Adaptabilité
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[4]"
    adaptabilite_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    adaptabilite_locator.click()
    time.sleep(2)

    # niveau button
    xpath = "//div[@id='root']/div/div[@class='modal modal-default']/div/div[@class='full-height full-width']/div[2]/div[@class='full-width']/div/div/div/div[@class='css-60hgb7']/div[@role='combobox']//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

    # choix niveau intermédiaire
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[4]"
    intermediare_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    intermediare_locator.click()
    time.sleep(2)

    # champ commentaire
    xpath = "//textarea[@id='TXLVDE']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("s'adapter facilement")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="ajouter_competence_form", attachment_type=allure.attachment_type.PNG)


    # bouton ajouter competence
    xpath = "//button[@id='button-add']"
    ajouter_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    ajouter_locator.click()
    time.sleep(3)

    # bouton envoi demande update competence
    # xpath = "//button[@id='button-submit']"
    # envoyer_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # envoyer_locator.click()
    # time.sleep(4)

@then('le collaborateur navigue vers "Graphe des compétences"')
@allure.step('le collaborateur navigue vers "Graphe des compétences"')
def view_competence_history(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ASCSALE2']/div"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="graphe_competences", attachment_type=allure.attachment_type.PNG)

##### voir documents ####
@when('le collaborateur navigue vers "Mes documents"')
@allure.step('le collaborateur navigue vers "Mes documents"')
def navigate_to_mes_documents(driver):
    xpath = "//div[@id='root']/div/div[3]/div[@class='header']//a[@href='/GP4You/DocumentsIndex']//div[@class='tooltip tooltip-align-bottom']/div"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

@when('le collaborateur voit document "Bulletin de Paie"')
@allure.step('le collaborateur voit document "Bulletin de Paie"')
def view_bulletin_de_paie(driver):
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']/div[2]//div[@class='flex-column-start full-width table-body']/div[1]/div[.='Mon Bulletin de Paie']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(2)

@then('le collaborateur clique sur bouton "Télécharger"')
@allure.step('le collaborateur clique sur bouton "Télécharger"')
def click_telecharger(driver):
    xpath = "Télécharger"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.LINK_TEXT, xpath)))
    locator.click()
    time.sleep(3)

############# formations ######
@when('le collaborateur navigue vers "Ma formation"')
@allure.step('le collaborateur navigue vers "Ma formation"')
def navigate_to_ma_formation(driver):
    xpath = "//div[@id='root']/div/div[3]//ul[@class='full-width']//div[.='Ma formation']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

@when('le collaborateur recherche une  formation avec le domaine "Langues étrangères", un nom de stage "Anglais débutants", et un id de stage "ATS001"')
@allure.step('le collaborateur recherche une  formation avec le domaine "Langues étrangères", un nom de stage "Anglais débutants", et un id de stage "ATS001"')
def search_formation(driver):
    xpath = "//div[@id='root']/div//ul[@class='full-width']/ul//a[@href='/GP4You/ATC700E1']//span[.='Offre de formation']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)

    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']/div[2]/div/div[@class='card-body']/div[4]/div[@class='full-width']/div/div/div/div[@class='css-60hgb7']/div[@role='combobox']//input[@id='disable-close-on-select']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(1)

    # choix domaine langues etrangeres
    xpath = "//ul[@id='disable-close-on-select-listbox']/li[7]"
    langues_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    langues_locator.click()
    time.sleep(2)

    # champ nom du stage
    xpath = "//input[@id='LBCRLG']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("Anglais débutants")
    time.sleep(2)

    # champ id du stage
    xpath = "//div[@id='root']/div/div[3]/div[@class='content-grid content-grid-doble']//div[@class='card-body']/div[9]/div[@class='input-fields input-fields-default text-black']/input"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.send_keys("ATS001")
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="rechercher_formation", attachment_type=allure.attachment_type.PNG)

    #bouton rechercher
    xpath = "//button[@id='button.search']"
    rechercher_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    rechercher_locator.click()
    time.sleep(3)

@then('le collaborateur voit les détails de la résultat')
@allure.step('le collaborateur voit les détails de la résultat')
def view_result_anglais_debutants(driver):
    xpath = "//div[@id='root']/div/div[3]//div[@class='flex-column-start full-width table-body']/div/div[1]/div[.='Anglais débutants']"
    locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="voir_resultat", attachment_type=allure.attachment_type.PNG)

@then('le collaborateur ferme modal résultat')
@allure.step('le collaborateur ferme modal résultat')
def close_formation_result(driver):
    xpath = "//div[@id='root']/div//div[@class='modal-close-btn']/div/i"
    locator = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    locator.click()
    time.sleep(4)



#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Modifier état civil")
#def test_modifier_etat_civil(driver):
def modifier_etat_civil(driver):
    # Scénario: Modifier Etat Civil
    #login(driver)
    navigate_to_donnees_indiv(driver)
    click_etat_civil(driver)
    modify_marital_status(driver)
    #verify_marital_status(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Annuler demande de modification d'état civil")
#def test_annuler_demande_modification_etat_civil(driver):
def annuler_demande_modification_etat_civil(driver):
    # Scénario: Annuler Demande modification Etat civil
    #login(driver)
    navigate_to_mes_demandes(driver)
    select_request_to_cancel(driver)
    click_annuler(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("ajouter une nouvelle personne à charge")
#def test_ajout_personne_a_charge(driver):
def ajout_personne_a_charge(driver):
    #login(driver)
    navigate_to_personnes_a_charge(driver)
    add_dependant(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Modifier les informations du contact d'urgence")
#def test_modifier_contacts_urgence(driver):
def modifier_contacts_urgence(driver):
    #login(driver)
    navigate_to_personnes_a_contacter(driver)
    modify_contact_urgence(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Modifier les coordonnées bancaires")
#def test_modifier_coordonnees_bancaires(driver):
def modifier_coordonnees_bancaires(driver):
    #login(driver)
    navigate_to_coordonnees_bancaires(driver)
    modify_coordonnees_bancaires(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("demande d'absence et vérification")
#def test_absences(driver):
def absences(driver):
    #login(driver)
    navigate_to_mes_absences(driver)
    navigate_to_request_absence(driver)
    request_absence(driver)
    navigate_to_absence_planning(driver)
    annuel_absence_planning(driver)
    view_team_calendar(driver)
    view_absence_history(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Modifier compétences")
#def test_modifier_competences(driver):
def modifier_competences(driver):
    #login(driver)
    navigate_to_mes_competences(driver)
    add_competence(driver)
    view_competence_history(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Voir documents")
#def test_voir_documents(driver):
def voir_documents(driver):
    #login(driver)
    navigate_to_mes_documents(driver)
    view_bulletin_de_paie(driver)
    click_telecharger(driver)

#@allure.feature("Fonctionnalités de collaborateur")
@allure.story("Rechercher formation")
#def test_recherche_formation(driver):
def recherche_formation(driver):
    #login(driver)
    navigate_to_ma_formation(driver)
    search_formation(driver)
    view_result_anglais_debutants(driver)
    close_formation_result(driver)


### test unitaire
@allure.feature("Fonctionnalités de collaborateur")
def test_fonctionnalites_collaborateur(driver):
    login(driver)
    modifier_etat_civil(driver)
    #annuler_demande_modification_etat_civil(driver)
    ajout_personne_a_charge(driver)
    modifier_contacts_urgence(driver)
    modifier_coordonnees_bancaires(driver)
    absences(driver)
    modifier_competences(driver)
    recherche_formation(driver)
