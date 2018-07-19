import pytest
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
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):

    # Test user data such as name, last name etc...
    name = "testNamea"
    lastName = "testLastNamea"
    email = "testEmaila@mail.com"
    password = "123456"

    # First step of registration, till confirmation letter is sent
    driver.implicitly_wait(50)
    driver.get("http://www.app32.appdevstage.com/")
    driver.implicitly_wait(50)
    driver.find_element_by_xpath("//a[@href='http://my.app32.appdevstage.com/open-account']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//aside")))
    driver.find_element_by_xpath("//input[@name='firstName']").send_keys(name)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='lastName']")))
    driver.find_element_by_xpath("//input[@name='lastName']").send_keys(lastName)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input").send_keys(email)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input")))
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[3]/div/input").send_keys(password)
    driver.save_screenshot('screenie.png')
    driver.find_element_by_xpath("//button[@data-auto-event-label='Open account']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/aside/div/div[3]/div[2]/div[1]")))

    # Second step of registration (confirmation of the letter)
    driver.implicitly_wait(50)
    driver.get("http://mailhog.app32.appdevstage.com/")
    driver.find_element_by_xpath("//input[@ng-model='searchText']").send_keys(email)
    driver.find_element_by_xpath("//span[contains(text(), 'Confirm your email address to start trading')]").click()
    driver.switch_to_frame("preview-html")
    driver.find_element_by_partial_link_text('Confirm').click()


