#coding: utf-8

import time
from selenium import webdriver
import pandas as pd

def get_top10_list(name, href):
    print(name, href)
    driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')
    driver.get(href)

    js = 'var q=document.documentElement.scrollTop=200'
    driver.execute_script(js)
    time.sleep(5)

    driver.find_element_by_xpath('//a[@data-taid="tzzh"]').click()
    time.sleep(5)

    js = 'var q=document.documentElement.scrollTop=1000'
    driver.execute_script(js)
    time.sleep(5)

    year =  driver.find_element_by_xpath('//div[@id="zcgDate"]/div[1]/p').text
    month = driver.find_element_by_xpath('//div[@id="zcgDate"]/div[2]/p').text

    print(year, month)
    top10 = driver.find_elements_by_xpath('//div[@id="zcgList"]/div[3]/ul')
    title = top10[0].text.split('\n')

    buffer = []
    for x in top10[1:]:
        buffer.append(x.text.split('\n'))

    data = pd.DataFrame(data=buffer, columns=title)
 
    filename = 'raw_data/基金/' + name + '.xlsx'
    sheet_name = year + '年' + month + '季度'

    with pd.ExcelWriter(filename) as writer:
        data.to_excel(writer, sheet_name=sheet_name, header=True, index=False)
 
    driver.quit()

def read_top10(name, sheet_name):
    try:
        filename = 'raw_data/基金/'+ name + '.xlsx'
        df = pd.read_excel(filename, sheet_name)
    except Exception:
        print(name, 'does not exist')
        df = None
    return df