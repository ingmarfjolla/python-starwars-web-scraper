from numpy.lib.utils import source
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

class Characters_Scraper():
    PATH = '/usr/local/bin/chromedriver'


    #

    def initialpass(self): 
       
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")

        #driver = webdriver.Chrome(self.PATH,options=chrome_options)
        driver = webdriver.Chrome(self.PATH)
        driver.get("https://www.starwars.com/databank/")
        driver.implicitly_wait(10)
        character_link = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/article/section[6]/div[1]/div[2]/ul/li[2]')
                                                        
        ##clicked on character on the left choices 
        character_link.click()
        ### THIS IS NECESSARY FOR CLICKING ALL SHOW ALL 
        ### COMMENT AND UNCOMMENT FOR DEBUGGING PURPOSES ONLY 
        # while True:

        #     try:
        #         all_chars = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/article/section[4]/div[1]/div[4]/div/a/span[1]')
        #         all_chars.click()
        #         driver.implicitly_wait(10)
        #     except ElementNotInteractableException:
        #         break
        #     except NoSuchElementException:
        #         break

        #### !!!###### END OF CLICKING####
        ## this would be an interesting "Cheap" way to click through if you know exact number of clciks.
        ##bad method tho
        # all_chars.click()
        # all_chars.click()

        page_source = driver.page_source
        # driver.quit()
        # driver.implicitly_wait(10)
        return page_source
        # print(page_source)

        

    def metadata_site(self,page_source):
        soup = BeautifulSoup(page_source, 'lxml')
        # soup = BeautifulSoup(page_source, 'html.parser')



        #### n is 18 because the first 18 are cached from a previous search and kept in page source
        ###so just hardcode this since is always the same , and for wahtever reason 
        ## shares the same exact class name as current search 
        n = 18 
        ####
        ###
        reviews_selector = soup.find_all('div', class_='building-block-config  sixth image-top  ratio-1x1 short  mob-width-half mob-image-top           ')



        ### DATA I AM WORKING WITH
        ### the head div (first line) contained 
        # multiple classes  so using a CSS selector was best.
        ###In this initial search I am only saving the Name, link, thumbnail. and small descripion.
        # <div class="building-block-config databank-content sixth image-top ratio-1x1 short mob-width-half mob-image-top"> 
        # <div class="building-block"> 
        # <div class="building-block-aspect"> 
        # <div class="building-block-padding"> 
        # <div class="building-block-wrapper"> 
        # <div class="image-wrapper"> 
        # <div class="aspect"> 
        # <a data-slug="databank/2br-ntb" href="https://www.starwars.com/databank/2br-ntb" tabindex="-1"> 
        # <img alt="2BR-NTB" class="thumb reserved-ratio" src="https://lumiere-a.akamaihd.net/v1/images/2br-ntb-main_081ce1aa.jpeg?region=618%2C87%2C633%2C633&amp;width=320"/> </a> 
        # </div> </div> <div class="content-wrapper"> <div class="bedazzlement"></div> 
        # <div class="content-bumper"> 
        # <div class="content-info"> 
        # <h3 class="title"> 
        # <a data-slug="databank/2br-ntb" 
        # href="https://www.starwars.com/databank/2br-ntb"> 
        # <span class="long-title">2BR-NTB</span> </a> 
        # </h3> <div class="desc-sizer"> <a data-slug="databank/2br-ntb" href="https://www.starwars.com/databank/2br-ntb" tabindex="-1"> 
        # <p class="desc">Loyal to Norath Kev, the droid 2BR-NTB has a distinct green-and-red paint scheme and sensors attuned to impending danger.</p> </a> </div> </div> </div> 
        # <div class="metadata"> <div class="anchored-text"> <h4 class="category-info"> <span class="content-icon databank-icon"></span> <span class="category-name">databank</span> </h4> 
        # </div> 
        # </div> 
        # <div class="decal"></div> </div> </div> </div> </div> </div> </div>

        unprocessedarray = soup.select('div.building-block-config.sixth.image-top.ratio-1x1.short.mob-width-half.mob-image-top')
        #print(len(reviews_selector))
        #print(unprocessedarray)

        ##skips first n elements (unnecesary) 
        preprocessed_array = unprocessedarray[n:]

        name = []
        starwars_site_link= []
        img = []
        descripion = []

        dictionary_of_star_wars = {}
        biggest_array_ever = []

        for items in preprocessed_array:
            name.append(items.find("span").text)
            starwars_site_link.append(items.find("a").get('href'))
            descripion.append(items.find("p").text)
            img.append(items.find("img").get('src'))
            # print(items.find("a"))
        if(len(name) != len(starwars_site_link) and len(descripion) != len(img) ):
            print("HUGE ERROR IN PROGRAM IM SORRRY")
            exit()
        iterator = len(name)
        for i in range(iterator):
            dictionary_of_star_wars ={
            "Name" : name[i],
            "Character_Image": img[i],
            "Character_Description" : descripion[i],
            "Character_site"  : starwars_site_link[i]
            }
            biggest_array_ever.append(dictionary_of_star_wars) 
        return biggest_array_ever

    def create_frame(self,dictobjects):
        return pd.DataFrame(dictobjects)


    def triggerfunction(self):
        source_ = self.initialpass()
        #print(source_)
        array_of_firstpass = self.metadata_site(source_) 
        #print(array_of_firstpass[0])
        formatted_data = self.create_frame(array_of_firstpass)
        print(len(array_of_firstpass))
        print(formatted_data)
        #print(formatted_data.iloc[0,:])


def main():
    first = Characters_Scraper()
    first.triggerfunction()

main()