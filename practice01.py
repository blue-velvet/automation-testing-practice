import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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
    name = "testNameccc"
    lastName = "testLastNameccc"
    email = "testEmailccc@mail.com"
    password = "123456"
    city = "Tokyo"
    address = "Baker street, 10"
    tel = "+15551234567"


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
    try:
        driver.find_element_by_xpath("//button[@data-auto-event-label='Sign In']").click()
        WebDriverWait(driver, 10).until(
            EC.title_is(
                ("Open new real account | OctaFX")))
    except Exception:
        driver.save_screenshot('screenshot3.png')
    """


    # Forth step (registration itself)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath("//select[@name='country']/option[text()='Malaysia']")
    driver.find_element_by_name("city").send_keys(city)
    driver.find_element_by_name("address").send_keys(address)
    driver.find_element_by_name("tel").send_keys(tel)
    driver.find_element_by_xpath("//select[@name='birthday-day']/option[text()='03']")
    driver.find_element_by_xpath("//select[@name='birthday-month']/option[text()='April']")
    driver.find_element_by_xpath("//select[@name='birthday-year']/option[text()='1985']")
    driver.find_element_by_xpath("//form-t01__radio-input-elem[contains(text(), 'Yes')]")



