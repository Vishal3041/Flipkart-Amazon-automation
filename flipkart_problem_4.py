from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from selenium.common import exceptions
from tqdm import tqdm
import time
import pandas as pd


class Flipkart():

    def __init__(self):
        self.url = 'https://www.flipkart.com'
        self.driver = webdriver.Chrome("/Users/amittripathi/PycharmProjects/selenium_1/Drivers/chromedriver")

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

    def create_csv_file(self):
        row_headers = ["Name", "Price in Rupees", "Model", "Category", "Source", "url"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=row_headers)
        self.mycsv.writeheader()

    def data_scrap(self, user_search):
        list_of_links = []
        description_of_all = []
        price_of_all = []
        condition = 1
        category = user_search

        #only considered for 2 pages because of memory and time it takes to process the pages
        while condition <= 2:
            all_products_link = self.driver.find_elements_by_class_name('_2kHMtA')
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
        time.sleep(1)

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

    def tearDown(self):
        self.driver.quit()
        self.file_csv.close()


if __name__ == "__main__":
    print("please enter what you want to search:")
    user_input = input()

    Flipkart = Flipkart()
    Flipkart.page_load(user_input)
    Flipkart.create_csv_file()
    Flipkart.data_scrap(user_input)
    Flipkart.tearDown()
    time.sleep(2)
    Amazon = Amazon()
    Amazon.page_load(user_input)
    Amazon.create_csv_file()
    Amazon.data_scrap(user_input)
    Amazon.tearDown()

    reader = csv.reader(open("Flipkart_output.csv"))
    reader1 = csv.reader(open("Amazon_output.csv"))

    df1 = pd.read_csv('Amazon_output.csv')
    df2 = pd.read_csv('Flipkart_output.csv')
    df1.set_index("Model", inplace=True)
    df2.set_index("Model", inplace=True)
    index1 = df1.index
    index2 = df2.index
    list1 = []
    for i in index1:
        for j in index2:
            if i == j:
                if i not in list1 and i != "Bluetooth;WiFi Hotspot":
                    list1.append(i)
            elif i not in index2 and i not in list1 and i != "Bluetooth;WiFi Hotspot":
                list1.append(i)
            if j not in index1 and j not in list1 and j != "Flipkart":
                list1.append(j)
    list_of_price = []
    for i in list1:
        if i in df1.index and i in df2.index:
            if df1['Price in Rupees'][i] < df2['Price in Rupees'][i]:
                price = df1['Price in Rupees'][i]
                name = df1['Name'][i]
                source = df1['Source'][i]
                url = df1['url'][i]
                cat = df1['Category'][i]
                temp = [name, price, i, cat, source, url]
                list_of_price.append(temp)
            else:
                price = df2['Price in Rupees'][i]
                name = df2['Name'][i]
                source = df2['Source'][i]
                url = df2['url'][i]
                cat = df2['Category'][i]
                temp = [name, price, i, cat, source, url]
                list_of_price.append(temp)

        elif i in df1.index and i not in df2.index:
            price = df1['Price in Rupees'][i]
            name = df1['Name'][i]
            source = df1['Source'][i]
            url = df1['url'][i]
            cat = df1['Category'][i]
            temp = [name, price, i, cat, source, url]
            list_of_price.append(temp)
        elif i not in df1.index and i in df2.index:
            price = df2['Price in Rupees'][i]
            name = df2['Name'][i]
            source = df2['Source'][i]
            url = df2['url'][i]
            cat = df2['Category'][i]
            temp = [name, price, i, cat, source, url]
            list_of_price.append(temp)

    with open('Lowest_model_price.csv', 'w', newline='') as file:
        row_headers = ["Name", "Min Price in Rupees", "Model", "Category", "Source", "url"]
        mycsv = csv.DictWriter(file, fieldnames=row_headers)
        mycsv.writeheader()
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(list_of_price)