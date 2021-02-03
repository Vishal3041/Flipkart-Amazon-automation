from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from mechanize import Browser
from tqdm import tqdm
import time
br = Browser()


class Flipkart():

    def __init__(self):
        self.url = 'https://www.flipkart.com'
        self.driver = webdriver.Chrome("/Users/amittripathi/PycharmProjects/selenium_1/Drivers/chromedriver")

    def page_load(self):
        self.driver.get(self.url)
        try:
            if self.driver.find_element_by_class_name("_2QfC02"):
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
        except:
            pass
        #user_input = input()
        self.driver.find_element_by_name("q").send_keys("mobiles")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(2)
        page_html = self.driver.page_source
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):
        row_headers = ["Name", "Price in Rupees", "model", "Category", "Source", "url"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=row_headers)
        self.mycsv.writeheader()

    def data_scrap(self):
        list_of_links = []
        condition = 1
        cat = self.driver.find_elements_by_class_name('TB_InB')[1]
        b = cat.find_element_by_tag_name('a')
        category = b.get_property('title')

        #only considered for 2 pages because of memory and time it takes to process the pages
        while condition <= 2:
            all_products_link = self.driver.find_elements_by_class_name('_2kHMtA')
            print(all_products_link)
            for link in all_products_link:
                a = link.find_element_by_tag_name('a')
                list_of_links.append(a.get_property('href'))

            try:
                class_name = self.driver.find_element_by_class_name("yFHi8N")
                next = class_name.find_elements_by_tag_name('a')[-1]
                h = next.get_property('href')
                self.driver.get(h)
                condition += 1
            except:
                pass

        #if you want to run for all the pages replace above while loop with below
        '''
        condition = True
        while condition:
            all_products_link = self.driver.find_elements_by_class_name('_2kHMtA')
            # all_products_link = (self.soup.find_all('div', class_='_2kHMtA'))
            print(all_products_link)
            for link in all_products_link:
                a = link.find_element_by_tag_name('a')
                list_of_links.append(a.get_property('href'))

            try:
                class_name = self.driver.find_element_by_class_name("yFHi8N")
                next = class_name.find_elements_by_tag_name('a')[-1]
                h = next.get_property('href')
                self.driver.get(h)
            except:
                condition = False
            '''
        all_details = []
        for i in tqdm(list_of_links):
            self.driver.get(i)
            try:
                name_of_product = self.driver.find_element_by_class_name('B_NuCI').text
            except:
                name_of_product = None
            try:
                price = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]').text
            except:
                price = None
            try:
                model = self.driver.find_elements_by_class_name('_21lJbe')[1].text
            except:
                model = None
            try:
                flip_class = self.driver.find_element_by_class_name('_3qX0zy')
                list1 = flip_class.find_elements_by_tag_name('img')[0]
                source = list1.get_property('alt')
            except:
                source = None
            url = i
            temp = [name_of_product,price,model,category, source,url]
            all_details.append(temp)

        with open('Flipkart_output.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(all_details)
        print(list_of_links)
        print(len(list_of_links))

    def tearDown(self):
        self.driver.quit()
        self.file_csv.close()


if __name__ == "__main__":
    Flipkart = Flipkart()
    Flipkart.page_load()
    Flipkart.create_csv_file()
    Flipkart.data_scrap()
    Flipkart.tearDown()