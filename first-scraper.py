from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
from pprint import pprint


PATH = '/usr/local/bin/chromedriver'
#webdriver is located in path 
driver = webdriver.Chrome(PATH)
driver.get("https://www.starwars.com/databank/")
driver.implicitly_wait(10)
character_link = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/article/section[4]/div[1]/div[2]/ul/li[2]')
character_link.click()

#print(character_link.text)
#print("ye")
#all_chars = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/article/section[4]/div[1]/div[4]/div/a/span[1]')



### THIS IS NECESSARY FOR CLICKING ALL SHOW ALL 
### COMMENT AND UNCOMMENT FOR DEBUGGING PURPOSES ONLY 
while True:

    try:
        all_chars = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/article/section[4]/div[1]/div[4]/div/a/span[1]')
        all_chars.click()
        driver.implicitly_wait(10)
    except ElementNotInteractableException:
        break
    except NoSuchElementException:
        break

#### !!!###### END OF CLICKING####

                                                # //*[@id="ref-1-3"]/div[1]/div[3]/div/ul/div[1]
# list = driver.find_elements_by_xpath("//*[starts-with(@id,'ref-1-3')]/div[1]/div[3]/div/ul")
# for items in list:
#     print(len(list))
#print(charssss[1].text)

#print(len(all_characters_in_sw))
# all_chars.click()
# all_chars.click()
# all_chars.click()
# all_chars.click()
# all_chars.click()


page_source = driver.page_source

# print(page_source)

soup = BeautifulSoup(page_source, 'lxml')
# soup = BeautifulSoup(page_source, 'html.parser')

reviews = []

#### n is 18 because the first 18 are cached from a previous search and kept in page source
###so just hardcode this since is always the same , and for wahtever reason 
## shares the same exact class name as current search 
n = 18 
####




####

###
reviews_selector = soup.find_all('div', class_='building-block-config  sixth image-top  ratio-1x1 short  mob-width-half mob-image-top           ')



### DATA I AM WORKING WITH
### the head div (first line) contained multiple classes  so using a CSS selector was best.
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

trythisbro = soup.select('div.building-block-config.sixth.image-top.ratio-1x1.short.mob-width-half.mob-image-top')
#print(len(reviews_selector))

newestarray = trythisbro[n:]

name = []
starwars_site_link= []
img = []
descripion = []

dictionary_of_star_wars = {}
biggest_array_ever = []
for items in newestarray:
    name.append(items.find("span").text)
    starwars_site_link.append(items.find("a").get('href'))
    descripion.append(items.find("p").text)
    img.append(items.find("img").get('src'))
    # print(items.find("a"))
#print(name)
# print(len(name))
# print(len(descripion))
# print(len(starwars_site_link))
# print(len(img))

# dictionary_of_star_wars ={
#     "Name" : name[0],
#     "Character_Image": img[0],
#     "Character_Description" : descripion[0],
#     "Character_site"  : starwars_site_link[0]
# }
# pprint(dictionary_of_star_wars)
# print(dictionary_of_star_wars)
iterator = len(name)
for i in range(iterator):
    dictionary_of_star_wars ={
    "Name" : name[i],
    "Character_Image": img[i],
    "Character_Description" : descripion[i],
    "Character_site"  : starwars_site_link[i]
    }
    biggest_array_ever.append(dictionary_of_star_wars) 
# print(starwars_site_link)

print(len(biggest_array_ever))
for items in biggest_array_ever:
    pprint(items)
# driver.implicitly_wait(10)
driver.quit()
