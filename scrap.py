import pandas as pd
other2 = pd.read_csv("trend\\trend_2020_2.csv", sep=",", index_col='Unnamed: 0', encoding='cp949')
list(other2['제목'])

from selenium import webdriver
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("headless")


driver = webdriver.Chrome("chromedriver.exe", options=options)

def naver_movie(name):

    #네이버 영화로 이동
    driver.get("https://movie.naver.com/")

    #영화 이름 검색
    sel = "#ipt_tx_srch"
    ui = driver.find_element_by_css_selector(sel)
    ui.send_keys(name)
    ui.send_keys(Keys.RETURN)

        #영화를 클릭해서 정보 보기
    sel = "#old_content > ul:nth-child(4) > li:nth-child(1) > p"
    ui = driver.find_element_by_css_selector(sel)
    ui.click()

        #평점 가져오기
    sel = "#pointNetizenPersentBasic > em"
    ui = driver.find_elements_by_css_selector(sel)
    netizen_rate = ""
    for item in ui:
        netizen_rate += item.text

    sel = "#content > div.article > div.mv_info_area > div.mv_info > div.main_score > div:nth-child(2) > div > a > div"
    ui = driver.find_elements_by_css_selector(sel)
    press_rate = ""
    for item in ui:
        press_rate += item.text

        #평점 탭 클릭하기
    sel ="#movieEndTabMenu > li:nth-child(5) > a"
    ui = driver.find_element_by_css_selector(sel)
    ui.click()

    try:
        #네티즌 리뷰 쓸어오기
        review_1 = [ ]
        driver.switch_to.frame("pointAfterListIframe")
        sel = "body > div > div > div.score_result > ul > li > div.score_reple > p > span:last-child"
        ui = driver.find_elements_by_css_selector(sel)
        for item in ui:
            review_1.append(item.text)
        driver.switch_to.default_content()

    except:
        riveiw_1= []

        #평론가 리뷰 쓸어오기
    review_2 = [ ]
    sel = "#content > div.article > div.section_group.section_group_frst > div:nth-child(6) > div > div.reporter > ul > li"
    ui = driver.find_elements_by_css_selector(sel)
    for item in ui:
        review_2.append(item.text)


    return netizen_rate, press_rate, review_1, review_2

data = [ ]
for i in list(other2['제목']):
    netizen_rate, press_rate, review_1 , review_2 = naver_movie(i)
    data.append([i,netizen_rate, press_rate, review_1 , review_2])
df = DataFrame(data)
df.columns = ['제목','네티즌평점','평론가평점','네티즌리뷰','평론가리뷰']
df.to_csv('평점2020.csv',encoding="cp949")




