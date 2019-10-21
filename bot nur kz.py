from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
import time
import requests
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.support.select import Select

from selenium.webdriver.firefox.options import Options

#i = 10 # Число страниц на сайте Koлеса KZ которые просмаутривает наш бот

#while i >= 0:

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

### переменные (логин, пароль, задание, количество страниц для парсинга)


email = "kazybayeva812@mail.ru"
password = "123456789"
#doljnost = "водитель"
gorod = "Нур-Султан (Астана)"
# сюда добавляем адрес страниц поиска
pagesadd = "https://rabotanur.kz/searchEmployer/Search/query//city_id/26403/salary[salary_from]//salary[salary_to]//birthday[birthday_from]//birthday[birthday_to]//gender[0]/1/26403/availability_id0/1/page/40/birthdaybirthday_to/50/gender0/page/"
pages_num = 104


browser = webdriver.Firefox() # Запускаем локальную сессию FOX


nurkz = "https://rabotanur.kz"
browser.get(nurkz)




#логинимся

loginbutton = browser.find_element_by_link_text('Войти').click()
login = browser.find_element_by_name('Users[email]').send_keys(email)
passw = browser.find_element_by_name('Users[password]').send_keys(password)
enter = browser.find_element_by_name('yt0').click()

#цикл
time.sleep(4)

while pages_num >0:

	try:
		vcn = 15
		time.sleep(4)

		url = str(pagesadd) +str(pages_num)
		
		browser.get(url) # Загружаем страницу
		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")
		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")



		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			
		else:
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + "-------------------------")


		


		time.sleep(2) # Пусть страница загрузится. Вдруг у нас медленный интернет... это задержка в 2 секунды 
		vakaslist1 = browser.find_elements_by_xpath('.//a[@class = "gtn-resume b-one-resume-in-list__info-title"]')[- vcn].click() #начинаем рыть вакансии -15 это кол-во на стр
		time.sleep(1)
		hochet_bit = browser.find_elements_by_xpath('.//span[@class = "b-resume-view__resume-position-name"]')[0].text
		print(hochet_bit)
		auto_check = browser.page_source
		if 'Есть личный автомобиль' in auto_check:
			print(str(vcn) + "с кобылой мужииииииик!!!!!!!!")
			telclick = browser.find_element_by_xpath('.//span[@class = "gtm-resume-add button button--confirm js-show-contacts-resume"]').click()
			time.sleep(1)
			#car = browser.find_elements_by_xpath('.//div[@class = "b-additional-info__description"]')[-1].text
			imya = browser.find_element_by_xpath('.//div[@class = "b-resume-view__user-name"]').text
			telefony = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-2].text
			emails = browser.find_elements_by_xpath('.//div[@class = "b-resume-view__user-cell"]')[-1].text
			zp = browser.find_element_by_xpath('.//span[@class = "status-disabled b-resume-view__resume-salary"]').text
			filecsv = open('telefony_nurkz.csv', 'a', encoding='cp1251', errors='ignore', newline='')
			filecsv.write(hochet_bit + ";" + telefony + ";" + imya + ";" + emails + ";" + zp + ";" + "\n")
			time.sleep(2)
			vcn-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			pages_num-=1
			
		else:
			pages_num-=1
			url = str(pagesadd) +str(pages_num)
			browser.get(url)
			print (str(vcn) + str(pages_num) + "-------------------------")



	except:
		continue
				#2

