from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome('./chromedriver')
browser.get('https://tech.sina.com.cn/')
browser.maximize_window()

data = {
    'title': [],
    'link': [],
    'image': [],
    'date': [],
    'keyword': []
}

def getSlides():
    return browser.find_elements_by_class_name('slider-item')

def getLeftBox():
    return browser.find_elements_by_class_name('tech-left').find_elements_by_tag_name('a')

def getSlideInfo(slides):

    for slider in slides:
        link = slider.find_element_by_tag_name('a').get_attribute('href')
        img = slider.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('src')
        page = requests.get(link)
        html = BeautifulSoup(page.content)
        title = html.find('h1').text
        date = html.find('span', {'class': 'date'})[0]
        

        data['title'].append(title)
        data['link'].append(link)
        data['image'].append(img)
        data['date'].append(date)
        data['keyword'].append('')

def getTechNews():
    return browser.find_element_by_class_name('tech-news').find_elements_by_tag_name('a')

def getTechNewsInfo(news):
    for n in news:
        data['title'].append(n.text)
        data['link'].append(n.get_attribute('href'))
        data['image'].append('')
        data['date'].append('')
        data['keyword'].append('')

leftBox = getLeftBox()
getTechNewsInfo(leftBox)

print(pd.DataFrame(data))


# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# menu = browser.find_elements_by_class_name('tyfeed-tab-i')
# menus = menu[1:].append()

# load = browser.find_element_by_class_name('cardlist-a__more')
# time.sleep(1)
# browser.find_element_by_class_name('f_app_close').click()

# for m in menu[1:3]:
#     time.sleep(0.5)
    # browser.execute_script('window.scrollTo(0, -200)')
    # m.click()

    # while load.text != '已经到底啦~':
    #     browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            
    #     time.sleep(0.5)
    #     load = browser.find_element_by_class_name('cardlist-a__more')
        
    #     if load.text == '点击查看更多':
    #         browser.execute_script('window.scrollTo(0, -100)')
    #         # browser.find_element_by_class_name('f_app_close').click()
    #         load.click()
        