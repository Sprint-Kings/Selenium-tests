from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser=webdriver.Chrome()
browser.get('https://4lapy.ru/')
button_vxod=browser.find_element(by=By.CLASS_NAME, value='b-link')
button_vxod.click()
# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.ID, value='tel-email-authorization')
username.send_keys('manasow.iw@yandex.ru')
# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.ID, value='password-authorization')
password.send_keys('bBh-6YC-cF9-4cj')
#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button_auth=browser.find_element(by=By.ID, value='websiteElement-authorization-loginButton')
#Нажимаем на кнопку входа
button_auth.click()
# Проверка результата
name = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "b-header-info__inner"), 'Иван')
    )
browser.get('https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/Hills_suhoy_korm_dlya_kastrirovannyh_kotov_6_mes_6et.html?offer=46720')
time.sleep(3)
like=browser.find_element(by=By.CSS_SELECTOR, value='.b-product-slider__favorites')
browser.execute_script("arguments[0].click();", like)
time.sleep(3)
browser.get('https://4lapy.ru/favorites/')
time.sleep(3)

product_like = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "b-item-name"), 'Science Plan Sterilised Cat сухой корм для кошек и котят, с курицей, 1,5кг')
    )
try:
# Проверка что пользователь находится на главной странице сайта
    assert 'Избранные товары' in browser.title
# Проверка что на странице присутствует полное имя пользователя
    assert name == True
    assert product_like == True
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()