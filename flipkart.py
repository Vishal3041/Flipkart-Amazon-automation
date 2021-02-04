from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from selenium.common import exceptions
from tqdm import tqdm
import time


class Flipkart():

    def __init__(self):
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.binary_location = GOOGLE_CHROME_PATH
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
        self.url = 'https://www.flipkart.com'
        #self.driver = webdriver.Chrome("C:\Users\anupamtripathi\Downloads\Vishal\Flipkart-Amazon-automation\chromedriver.exe")

    def page_load(self, user_search):
        self.driver.get(self.url)
        try:
            if self.driver.find_element_by_class_name("_2QfC02"):
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
        except:
            pass
        self.driver.find_element_by_name("q").send_keys(user_search)
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
        description_of_all = []
        price_of_all = []
        condition = 1
        cat = self.driver.find_elements_by_class_name('TB_InB')[1]
        b = cat.find_element_by_tag_name('a')
        category = b.get_property('title')

        #only considered for 2 pages because of memory and time it takes to process the pages
        while condition <= 2:
            all_products_link = self.driver.find_elements_by_class_name('_2kHMtA')
            print(all_products_link)
            for link in all_products_link:
                description_of_all.append(link.find_element_by_class_name('_4rR01T').text)
                list_of_links.append(link.find_element_by_tag_name('a').get_property('href'))
                try:
                    price_of_all.append(link.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]').text)
                except exceptions.NoSuchElementException:
                    price_of_all.append("")

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
        for i in tqdm(range(len(list_of_links))):
            name_of_product = description_of_all[i]
            price = price_of_all[i]
            try:
                self.driver.get(list_of_links[i])
                model = self.driver.find_elements_by_class_name('_21lJbe')[1].text
            except:
                model = None
            flip_class = self.driver.find_element_by_class_name('_3qX0zy')
            list1 = flip_class.find_elements_by_tag_name('img')[0]
            source = list1.get_property('alt')
            url = list_of_links[i]
            temp = [name_of_product, price, model, category, source, url]
            all_details.append(temp)

        with open('Flipkart_output.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(all_details)
        print(list_of_links)
        print(len(list_of_links))

    def tearDown(self):
        self.driver.quit()
        self.file_csv.close()


class Amazon():

    def __init__(self):
        self.url = 'https://www.amazon.in/'
        self.driver = webdriver.Chrome("/Users/amittripathi/PycharmProjects/selenium_1/Drivers/chromedriver")

    def page_load(self, user_input):
        self.driver.get(self.url)
        try:
            if self.driver.find_element_by_class_name("_2QfC02"):
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
        except:
            pass
        self.driver.find_element_by_name("field-keywords").send_keys(user_input)
        self.driver.find_element_by_name("field-keywords").send_keys(Keys.ENTER)
        page_html = self.driver.page_source
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):
        row_headers = ["Name", "Price in Rupees", "Model", "Category", "Source", "url"]
        self.file_csv = open('Amazon_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=row_headers)
        self.mycsv.writeheader()

    def data_scrap(self, user_search):
        list_of_links = []
        description_of_all = []
        price_of_all = []
        condition = 1
        while condition <= 2:
            all_products_link = self.driver.find_elements_by_xpath('//div[@data-component-type="s-search-result"]')
            print(all_products_link)
            for link in all_products_link:
                description_of_all.append(link.find_element_by_xpath('.//h2/a').text.strip())
                list_of_links.append(link.find_element_by_xpath('.//h2/a').get_property('href'))
                try:
                    price_of_all.append(link.find_element_by_xpath('.//span[@class="a-price-whole"]').text)
                except exceptions.NoSuchElementException:
                    price_of_all.append("")
            try:
                url = "https://www.amazon.in/s?k={}&page={}&qid=1612348730&ref=sr_pg_1".format(user_search, condition)
                self.driver.get(url)
                condition += 1
            except:
                pass

        all_details = []
        source = "Amazon"
        for i in tqdm(range(len(list_of_links))):
            name_of_product = description_of_all[i]
            price = price_of_all[i]
            category = user_search
            url = list_of_links[i]
            try:
                self.driver.get(list_of_links[i])
                model = self.driver.find_element_by_xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr[5]/td').text
            except:
                model = None
            temp = [name_of_product,price,model,category, source, url]
            all_details.append(temp)

        with open('Amazon_output.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(all_details)
        print(list_of_links)
        print(len(list_of_links))

    def tearDown(self):
        self.driver.quit()
        self.file_csv.close()


if __name__ == "__main__":
    #print("please enter what you want to search:")
    #user_input = input()

    Flipkart = Flipkart()
    Flipkart.page_load("mobiles")
    Flipkart.create_csv_file()
    Flipkart.data_scrap()
    Flipkart.tearDown()
    time.sleep(2)
    Amazon = Amazon()
    Amazon.page_load("mobiles")
    Amazon.create_csv_file()
    Amazon.data_scrap("mobiles")
    Amazon.tearDown()

    reader = csv.reader(open("Flipkart_output.csv"))
    reader1 = csv.reader(open("Amazon_output.csv"))
    f = open("Flipkart_amazon.csv", "w")
    writer = csv.writer(f)

    for row in reader:
        writer.writerow(row)
    for row in reader1:
        writer.writerow(row)
    f.close()