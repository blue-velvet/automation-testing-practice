import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



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
    name = "testName"
    lastName = "testLastName"
    email = "testEmail@mail.com"
    password = "123456"
    city = "Tokyo"
    address = "Baker street, 10"
    phone = "+15551234567"
    """


    # First step of registration, till confirmation letter is sent
    driver.get("http://www.app32.appdevstage.com/")
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='http://my.app32.appdevstage.com/open-account']").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//aside")))
    driver.find_element_by_xpath("//input[@name='firstName']").send_keys(name)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='lastName']")))
    driver.find_element_by_xpath("//input[@name='lastName']").send_keys(lastName)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input").send_keys(email)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input").send_keys(password)
    try:
        driver.find_element_by_xpath("//button[@data-auto-event-label='Open account']").click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/aside/div/div[3]/div[2]/div[1]")))
    except Exception:
        driver.save_screenshot('screenshot1.png')
    time.sleep(10)


    # Second step of registration (confirmation of the letter)
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


    """
    # Third step of registration (sign in after confirmation) (NOT NECCESSARY)
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


    # Forth step (registration itself)
    # Address window
    # driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_id("country_selector_chosen").click()
    element = driver.find_element_by_xpath("//input[@class='chosen-search-input']")
    element.send_keys('Malaysia')
    element.send_keys(u'\ue007')
    element = driver.find_element_by_name("city")
    if element.get_attribute("value") == None:
        element.send_keys(city)
    element = driver.find_element_by_name("address")
    if element.get_attribute("value") == None:
        element.send_keys(address)
    if element.get_attribute("value") == None:
        element.send_keys(phone)
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


    # Platform window
    time.sleep(0.2)
    driver.find_element_by_xpath("//input[@value='mt5']").send_keys(u'\ue00d')
    driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/form/div[1]/ul/li[1]/div[2]/div[2]/div/div/a").send_keys(u'\ue00d')
    driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/form/div[1]/ul/li[1]/div[2]/div[2]/div/div/div/ul/li[2]").clicl()
    driver.find_element_by_xpath("//button[@data-auto-event-label='Continue to deposit'][2]").click()





