import pytest
import time
from group import RegGroup, AddressGroup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions


@pytest.fixture
def driver(request):
    path_ff = r"C:\Users\kchumakov.000\Documents\drivers\geckodriver.exe"
    path_g = r"C:\\Users\\kchumakov.000\\Documents\\drivers\\chromedriver.exe"
    binary_ff = r"C:\Users\kchumakov.000\AppData\Local\Mozilla Firefox\firefox.exe"
    binary_g = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    wd = webdriver.Chrome(executable_path=path_g)
    wd.maximize_window()
    print(wd.capabilities)
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):

    # Test user data such as name, last name etc...
    f = open("C:\\Users\\kchumakov.000\\Documents\\GitHub\\automation-testing-practice\\test_data.txt")
    line = f.readlines()
    name = line[0]
    lastName = line[1]
    email = line[2]
    password = line[3]
    city = line[4]
    address = line[5]
    phone = line[6]
    f.close()

    new_user_registration(driver, RegGroup(name, lastName, email, password))
    confirm_letter(driver, email)
    #sign_in_after_confirmation(driver, Group(email, password))
    fill_address(driver, AddressGroup(address, city, phone))
    choose_platform(driver)


def new_user_registration(driver, group):
    driver.get("http://www.app32.appdevstage.com/")
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='http://my.app32.appdevstage.com/open-account']").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//aside")))
    driver.find_element_by_xpath("//input[@name='firstName']").send_keys(group.name)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='lastName']")))
    driver.find_element_by_xpath("//input[@name='lastName']").send_keys(group.lastName)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input").send_keys(group.email)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input").send_keys(group.password)
    time.sleep(0.5)
    try:
        driver.find_element_by_xpath("//button[@data-auto-event-label='Open account']").click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/aside/div/div[3]/div[2]/div[1]")))
    except Exception:
        driver.save_screenshot('screenshot1.png')
    time.sleep(7)


def confirm_letter(driver, email):
    driver.get("http://mailhog.app32.appdevstage.com/")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@ng-model='searchText']").send_keys(email)
    driver.find_element_by_xpath("//input[@ng-model='searchText']").send_keys(u'\ue007')
    time.sleep(1)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Confirm your email address to start trading')]")))
    driver.save_screenshot('screenshot1.png')
    driver.find_element_by_xpath("//span[contains(text(), 'Confirm your email address to start trading')]").click()
    driver.switch_to_frame("preview-html")
    try:
        driver.find_element_by_partial_link_text('Confirm').click()
        WebDriverWait(driver, 10).until(
            EC.title_is(
                ("Open new real account | OctaFX")))
    except Exception:
        driver.save_screenshot('screenshot2.png')


def sign_in_after_confirmation(driver, email, password):
    driver.get("http://www.app32.appdevstage.com/")
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(text(), 'Sign in')]").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//aside")))
    driver.find_element_by_xpath("/html/body/aside/div/div[2]/div/form/div[1]/div/input").send_keys(email)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[2]/div/form/div[2]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[2]/div/form/div[2]/div/input").send_keys(password)
    time.sleep(0.2)
    try:
        driver.find_element_by_xpath("//button[@data-auto-event-label='Sign In']").click()
        WebDriverWait(driver, 10).until(
            EC.title_is(
                ("Open new real account | OctaFX")))
    except Exception:
        driver.save_screenshot('screenshot3.png')


def fill_address(driver, group):
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_id("country_selector_chosen").click()
    element = driver.find_element_by_xpath("//input[@class='chosen-search-input']")
    element.send_keys('Malaysia')
    element.send_keys(u'\ue007')
    element = driver.find_element_by_name("city")
    if element.get_attribute("value") == "":
        element.send_keys(group.city)
    element = driver.find_element_by_name("address")
    if element.get_attribute("value") == "":
        element.send_keys(group.address)
    element = driver.find_element_by_name("phone")
    if element.get_attribute("value") == "":
        element.send_keys(group.phone)
    driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[1]/a/span").click()
    element = driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[1]/div/div/input")
    element.send_keys('22')
    element.send_keys(u'\ue007')
    driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[2]/a/span").click()
    element = driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[2]/div/div/input")
    element.send_keys('April')
    element.send_keys(u'\ue007')
    driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[3]/a/span").click()
    element = driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[5]/div/div/div[3]/div/div/input")
    element.send_keys('1985')
    element.send_keys(u'\ue007')
    driver.find_element_by_xpath("/html/body/div[3]/main/div[1]/form/div[6]/div[2]/div[1]/label/span").click()
    driver.find_element_by_xpath("//button[@data-auto-event-label='Continue']").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class ='reg-dep-form-block js-wizard-step-select-platform']")))
    driver.save_screenshot('screenshot4.png')


def choose_platform(driver):
    time.sleep(0.2)
    driver.find_element_by_xpath("//input[@value='mt5']").send_keys(u'\ue00d')
    time.sleep(0.2)
    #ActionChains(driver).move_to_element(
    #    "/html/body/div[3]/main/div[2]/div/form/div[1]/ul/li[1]/div[2]/div[2]/div/div").send_keys(u'\ue00d').send_keys(u'\ue007')
    #ActionChains(driver).move_to_element(
    #    "/html/body/div[3]/main/div[2]/div/form/div[1]/ul/li[1]/div[2]/div[2]/div/div/div/ul/li[2]").click()
    #time.sleep(3)
    driver.find_element_by_xpath("//button[@data-auto-event-label='Continue to practice']").click()







