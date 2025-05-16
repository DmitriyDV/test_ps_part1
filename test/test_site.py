import time
from pages.product import ProductPage
from pages.homepage import HomePage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is('Samsung galaxy s6')

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    # driver.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    # monitor_link = driver.find_element(By.CSS_SELECTOR,'''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(2) # very bad idea, never use this
    homepage.check_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR,'.card')
    # assert len(monitors) == 2