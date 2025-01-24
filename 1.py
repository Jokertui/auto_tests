import os.path
import time

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
options.page_load_strategy = "eager"
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.3")

screenshot_dir= "C:\\Users\\User\\Desktop\\Screen"

a=1

def get_screenshot_path():
    """Формирует путь для нового скриншота."""
    # c=get_a()
    name_screen = datetime.now().strftime(f"Screen{a}.png")
    return os.path.join(screenshot_dir, name_screen)


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains
scrolls = Scrolls(driver,action)

driver.get("https://gosuslugi.primorsky.ru/auth/testesia.htm")
time.sleep(10)

'''Локаторы'''
main_button_log = ("xpath", "//a[text()='Перейти на главную страницу']")
main_button = ("xpath", "//strong[@class='b-header-logo-glob-outer']")
main_catalog = ("xpath", "//span[text()='Каталог услуг']")
more_catalog = ("xpath", "//button[text()='Загрузить еще']")
one_catalog = ("xpath","//h2[text()='Социальное обеспечение']")
usluga = ("xpath", "(//h3[@class='g-tile-title'])[1]")
back_news = ("xpath","//a[@class='btn btn-default back-link']")
all_news = ("xpath", "//a[@class='btn btn-default b-news-button b-news-button__news_list']")
error_footer = ("xpath", "//span[text()='Сообщить об ошибке']")
banner_button_1 = ("xpath", "(//span[@class='btn-text'])[3]")
submit_search = ("xpath", "//button[@type='submit']")
tag_search = ("xpath", "(//a[@data-behavior='setFormSearchVal'])[4]")



'''5/1'''
wait.until(EC.element_to_be_clickable(main_button_log)).click()
time.sleep(7)
path_file = get_screenshot_path()
a=a+1
# a = get_a()
driver.save_screenshot(path_file)
print(path_file)

'''6/2'''
wait.until(EC.element_to_be_clickable(main_catalog)).click()
scrolls.scroll_to_bottom()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''7/3'''
wait.until(EC.element_to_be_clickable(more_catalog)).click()
scrolls.scroll_to_bottom()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''8/4'''
scrolls.scroll_to_top()
wait.until(EC.element_to_be_clickable(one_catalog)).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable(usluga)).click()
time.sleep(4)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''10/5'''
wait.until(EC.element_to_be_clickable(main_button)).click()
time.sleep(2)
title_news_locator = ("xpath", "(//span[@class='b-news-item-title'])[1]")
title_news = driver.find_element(*title_news_locator)
scrolls.scroll_to_element(title_news)
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''11/6'''
wait.until(EC.element_to_be_clickable(title_news)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''12/7'''
wait.until(EC.element_to_be_clickable(back_news)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''14/8'''
wait.until(EC.element_to_be_clickable(main_button)).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable(all_news)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''17/9'''
wait.until(EC.element_to_be_clickable(error_footer)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''18/10'''
wait.until(EC.element_to_be_clickable(main_button)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''19/11'''
wait.until(EC.visibility_of_element_located(banner_button_1)).click()
time.sleep(3)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''30/12'''
wait.until(EC.element_to_be_clickable(main_button)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)
time.sleep(3)

'''31/13'''
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''32/14'''
wait.until(EC.element_to_be_clickable(submit_search)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)

'''33/15'''
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)
time.sleep(2)

'''34/16'''
wait.until(EC.element_to_be_clickable(tag_search)).click()
time.sleep(2)
path_file = get_screenshot_path()
a = a+1
driver.save_screenshot(path_file)
print(path_file)




# # path_file = get_screenshot_path()
# # a = get_a()
# # driver.save_screenshot(path_file)
# print(path_file)