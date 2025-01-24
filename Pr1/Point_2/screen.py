class Screen:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from datetime import datetime
    from scrolls import Scrolls
    from selenium.webdriver.common.action_chains import ActionChains

    options = Options()
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    action = ActionChains
    scrolls = Scrolls(driver, action)

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def screen_element_to_be_clickable(self, x):
            self.driver.wait.until(EC.element_to_be_clickable(x)).click()