from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import csv
from tqdm import tqdm
import time


class Flipkart():

    def __init__(self):
        self.url = 'https://www.flipkart.com'
        self.driver = webdriver.Chrome("/Users/amittripathi/PycharmProjects/selenium_1/Drivers/chromedriver")

    def page_load(self, user_input):
        self.driver.get(self.url)
        try:
            if self.driver.find_element_by_class_name("_2QfC02"):
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
        except:
            pass
        self.driver.find_element_by_name("q").send_keys(user_input)
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(2)
        page_html = self.driver.page_source
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):
        row_headers = ["Name", "Price in Rupees", "model", "Category", "Source", "url"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=row_headers)
        self.mycsv.writeheader()

    def data_scrap(self, user_search, min_no, max_no, sort_type, exclude, num, pincode):
        list_of_links = []
        condition = 1

        if max_no is None:
            max_no = 999999999
        if max_no <= min_no:
            return
        time.sleep(3)
        self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ').click()
        if -99999 <= min_no < 1999:
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"Min")
        elif 2000 <= min_no < 4000:
            min_no = 2000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 4000 <= min_no < 6999:
            min_no = 4000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 7000 <= min_no < 9999:
            min_no = 7000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 10000 <= min_no < 12999:
            min_no = 10000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹"+str(min_no))
        elif 13000 <= min_no < 15999:
            min_no = 13000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 16000 <= min_no < 19999:
            min_no = 16000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 20000 <= min_no < 24999:
            min_no = 20000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 25000 <= min_no < 29999:
            min_no = 25000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif 30000 <= min_no < 50000:
            min_no = 30000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        elif min_no > 50000:
            min_no = 50000
            Select(self.driver.find_element_by_class_name('_1YAKP4').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(min_no))
        time.sleep(1)

        self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ').click()
        if 0 > max_no >= 2000:
            max_no = 4000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 4000 > max_no >= 2000:
            max_no = 4000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 7000 > max_no >= 4000:
            max_no = 7000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 10000 > max_no >= 7000:
            max_no = 10000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 13000 > max_no >= 10000:
            max_no = 13000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 16000 > max_no >= 13000:
            max_no = 16000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹"+str(max_no))
        elif 20000 > max_no >= 16000:
            max_no = 20000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 25000 > max_no >= 20000:
            max_no = 25000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 30000 > max_no >= 25000:
            max_no = 30000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 50000 > max_no >= 30000:
            max_no = 50000
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        elif 9999999 > max_no >= 50000:
            max_no = "50000+"
            Select(self.driver.find_element_by_class_name('_3uDYxP').find_element_by_class_name('_2YxCDZ')).select_by_visible_text(
                u"₹" + str(max_no))
        time.sleep(1)

        if sort_type == 'Relevance':
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div").click()
            except:
                pass
        elif sort_type == 'Popularity':
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[2]").click()
            except:
                pass
        elif sort_type == 'Price -- Low to High':
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[3]").click()
            except:
                pass
        elif sort_type == 'Price -- High to low':
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[4]").click()
            except:
                pass
        elif sort_type == 'Newest First':
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[5]").click()
            except:
                pass
        time.sleep(1)
        if exclude in ["Yes", "yes", "YES"]:
            try:
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div/div/div/div/section[21]/div/div").click()
                self.driver.find_element_by_xpath("//div[@id='container']/div/div[3]/div[2]/div/div/div/div/div/section[21]/div[2]/div/div/div/div/label/div").click()
            except:
                pass


        else:
            pass
        time.sleep(1)

        if num is "":
            num = 10
        elif int(num) > 50:
            print("no. of products cannot be more than 50, hence considering 50 products")
            num = 50

        category = user_search
        price_of_all = []
        description_of_all = []
        while condition <= 1:
            all_products_link = self.driver.find_elements_by_class_name('_2kHMtA')
            print(all_products_link)
            for link in all_products_link:
                description_of_all.append(link.find_element_by_class_name('_4rR01T').text)
                list_of_links.append(link.find_element_by_tag_name('a').get_property('href'))
                try:
                    price_of_all.append(link.find_element_by_xpath(
                        "//body/div[@id='container']/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]/div[2]/div[2]/div[1]/div[1]/div[1]").text)
                except:
                    price_of_all.append("")

            try:
                class_name = self.driver.find_element_by_class_name("yFHi8N")
                next = class_name.find_elements_by_tag_name('a')[-1]
                h = next.get_property('href')
                self.driver.get(h)
                condition += 1
            except:
                pass

        # if you want to run for all the pages replace above while loop with below
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
        list_of_num_links = list_of_links[0:int(num)]
        for i in tqdm(range(len(list_of_num_links))):
            name_of_product = description_of_all[i]
            price = price_of_all[i]
            try:
                self.driver.get(list_of_num_links[i])
                model = self.driver.find_elements_by_class_name('_21lJbe')[1].text
            except:
                model = None
            flip_class = self.driver.find_element_by_class_name('_3qX0zy')
            list1 = flip_class.find_elements_by_tag_name('img')[0]
            source = list1.get_property('alt')
            url = list_of_num_links[i]
            if self.driver.find_element_by_class_name('_36yFo0'):
                self.driver.find_element_by_class_name('_36yFo0').clear()
                self.driver.find_element_by_class_name('_36yFo0').click()
                self.driver.find_element_by_class_name("_36yFo0").send_keys(pincode)
                self.driver.find_element_by_class_name("_36yFo0").send_keys(Keys.ENTER)
                # time.sleep(1)
            try:
                if self.driver.find_element_by_class_name('_3XINqE'):
                    temp = [name_of_product, price, model, category, source, url]
                    all_details.append(temp)
            except:
                print('\n')
                print("Currently not available at this pincode: ", name_of_product)
        print("{} rows updated".format(len(all_details)))

        with open('Flipkart_output.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(all_details)
        print(list_of_links)
        print(len(list_of_links))

    def tearDown(self):
        self.driver.quit()
        self.file_csv.close()


if __name__ == "__main__":
    print("please enter what you want to search:")
    user_input = input()
    print("Please enter minimum price range:")
    min_no = int(input())
    print("Please enter maximum price range:")
    max_no = int(input())
    print("Select one Sort by type from list given below")
    print("[Relevance, Popularity, Price -- Low to High, Price -- High to low, Newest First]")
    sort_type = input()
    if sort_type not in ['Relevance', 'Popularity', 'Price -- Low to High', 'Price -- High to low', 'Newest First']:
        print("Entered wrong Sort by type considering Relevance as a default")
        sort_type = 'Relevance'
    print("Type yes or no to exclude out of stock elements")
    exclude = input()
    print("List no. of products required:")
    num = input()
    print("Please enter your pincode of length 6 digit")
    pincode = input()
    if pincode is "" or len(pincode) < 6 or len(pincode) > 6:
        print("Entered a wrong pincode considering 400072 as a default pincode")
        pincode = "400072"

    Flipkart = Flipkart()
    Flipkart.page_load(user_input)
    Flipkart.create_csv_file()
    Flipkart.data_scrap(user_input, min_no, max_no, sort_type, exclude, num, pincode)
    Flipkart.tearDown()
