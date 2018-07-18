import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    path_ff = r"C:\Users\kchumakov.000\Documents\drivers\geckodriver.exe"
    path_g = r"C:\\Users\\kchumakov.000\\Documents\\drivers\\chromedriver.exe"
    binary_ff = r"C:\Users\kchumakov.000\AppData\Local\Mozilla Firefox\firefox.exe"
    binary_g = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    wd = webdriver.Firefox(executable_path=path_ff, firefox_binary=binary_ff)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.octafx.com/")
    WebDriverWait(driver, 2000)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[1]/div/div[1]/div[2]/a").click()
    driver.find_element_by_name("firstName").send_keys("testName")
    driver.find_element_by_name("lastName").send_keys("testLastName")
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[2]/div/input").send_keys("testEmail@mail.com")
    driver.find_element_by_xpath("/html/body/aside/div/div[3]/div[1]/form/div[1]/div[2]/div/input").send_keys("testPassword")
    driver.find_element_by_class_name("/html/body/aside/div/div[3]/div[1]/form/div[4]/button/span").click()
    WebDriverWait(driver, 1000)
