from selenium import webdriver
import selenium.common.exceptions
import time
import datetime
import os


browser = webdriver.Chrome()
time.sleep(2)

class MainPage:
    def __init__(self):
        self.path_log = r'd:/syslog.txt'
        self.link = 'http://prom.ua/p45257130-velo-pokryshka-kenda.html'
        self.xpath_buy = "id('shopping-cart-add-element-text-45257130')"
        self.xpath_add_fav = "id('var')/div[2]/div[3]/div[4]/div[1]/div[3]/span/span[2]/span/span/span[2]"
        self.go_to_start_link()


    def go_to_start_link(self):
        browser.get(self.link)

    def add_fav(self):
        try:
            browser.find_element_by_xpath(self.xpath_add_fav).click()
        except selenium.common.exceptions.NoSuchElementException:
            self.log = open(self.path_log, 'a')
            self.log.write('Failed add to favorite - {0} [{1}]\n'.format(m.get_id_product(), datetime.datetime.now()))
            self.log.close()

    def buy(self):
        try:
            browser.find_element_by_xpath(self.xpath_buy).click()
        except selenium.common.exceptions.NoSuchElementException:
            self.log = open(self.path_log, 'a')
            self.log.write('Failed to buy item - {0} [{1}]\n'.format(m.get_id_product(), datetime.datetime.now()))
            self.log.close()

    def screenshot(self):
        name = self.link.replace('/','_').replace('.','-').replace(':','')
        if not os.path.exists(r'd:/screenshots_test'):
            os.mkdir(r'd:/screenshots_test')
        if not os.path.exists(os.path.join(r'd:/screenshots_test',name)):
            os.mkdir(os.path.join(r'd:\screenshots_test',name))
        count = len(os.listdir(os.path.join(r'd:/screenshots_test',name)))
        filename = os.path.join(r'd:/screenshots_test',name,'{0} - {1}.jpg'.format(name,count+1))
        browser.get_screenshot_as_file(filename)

    def get_id_product(self):
        return browser.title.split()[-1]


m = MainPage()
m.add_fav()
m.screenshot()
m.buy()





