# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)

# navigate to login page
driver.get("https://medium.com/search?q=xgboost")

# -----------------------------------------------------------------------------
# 1. Check for popups
try:    
    element = driver.find_element_by_id("popup_no")
    element.send_keys(Keys.RETURN)
    print("popup closed")
except:
    print("no popup")

# check page loaded correctly
assert "Login required" in driver.page_source

# -----------------------------------------------------------------------------
# 1. Login

# email
element = driver.find_element_by_name("user_email")
element.clear()
element.send_keys("fast_trap@hotmail.com")

# password
element = driver.find_element_by_name("user_password")
element.clear()
element.send_keys("41255410")

element.send_keys(Keys.RETURN)

# -----------------------------------------------------------------------------
# 2. Search for race
driver.get("http://www.greyhound-data.com/race.htm")



# country
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('country'))
select.select_by_visible_text("UK United Kingdom")

# statium
select = Select(driver.find_element_by_name('stadium'))
select.select_by_visible_text("Henlow")

# start month
select = Select(driver.find_element_by_name('startmonth'))
select.select_by_visible_text("Jan")

# start date
select = Select(driver.find_element_by_name('startdate'))
select.select_by_visible_text("2019")

# end month
select = Select(driver.find_element_by_name('endmonth'))
select.select_by_visible_text("Jan")

# end date
select = Select(driver.find_element_by_name('enddate'))
select.select_by_visible_text("2019")

# click show races
element = driver.find_element_by_name("go")
element.send_keys(Keys.RETURN)

# -----------------------------------------------------------------------------
# 3. Get links for all races

def de_dupe(x):
    return list(dict.fromkeys(x))

# get a list of all pages that contain links (1,2,3,4,5,....)     
race_pages = []
for elem in elems:
    link = elem.get_attribute("href")
    if '&x=' in link:
        race_pages.append(link)

race_pages = de_dupe(race_pages)

# visit each of the pages, and grab links of individual races
races = []

for race_page in race_pages:
    time.sleep(2)
    print(race_page)
    # navigate to page
    driver.get(race_page)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        link = elem.get_attribute("href")
        if 'http://www.greyhound-data.com/d?r=' in link:
            races.append(link)

len(races)

# -----------------------------------------------------------------------------
# 4. Make sure we only keep race links that are new
# check against database

# -----------------------------------------------------------------------------
# 5. Get race results for all new races and store in database

current_race = races[0]
driver.get(current_race)

bigtable = driver.find_element_by_xpath('html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td') 

for i in bigtable.find_elements_by_xpath('.//tr'):
    print(i.get_attribute('innerHTML'))
    
subtable = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td') 

rows_of_table = subtable.find_elements_by_xpath('.//tr')
print(rows_of_table[0].get_attribute('innerHTML'))
print(rows_of_table[1].get_attribute('outerHTML'))


greentable = driver.find_element_by_xpath("//table[@id='green']")



for i in subtable.find_elements_by_xpath('.//tr'):
    print(i.get_attribute('innerHTML'))
  
# race details
race_name =     '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[6]/b'
race_no_time =  '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[3]'
going =         '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[6]/b'
grade =         '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[6]/b'
date =          '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/b'
distance =      '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]/b'
stadium =       '/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[4]/b/a'

# positions
name_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[2]"
name_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[2]"
name_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[2]"
name_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[2]"
name_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[2]"
name_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[2]"
time_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[8]"
time_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[8]"
time_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[8]"
time_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[8]"
time_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[8]"
time_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[8]"
dist_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[9]"
dist_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[9]"
dist_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[9]"
dist_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[9]"
dist_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[9]"
dist_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[9]"
stime_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[10]"
stime_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[10]"
stime_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[10]"
stime_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[10]"
stime_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[10]"
stime_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[10]"
trap_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[11]"
trap_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[11]"
trap_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[11]"
trap_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[11]"
trap_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[11]"
trap_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[11]"
sp_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[13]"
sp_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[13]"
sp_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[13]"
sp_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[13]"
sp_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[13]"
sp_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[13]"
weight_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[14]"
weight_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[14]"
weight_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[14]"
weight_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[14]"
weight_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[14]"
weight_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[14]"
comment_1 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[2]/td[15]"
comment_2 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[3]/td[15]"
comment_3 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[4]/td[15]"
comment_4 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[5]/td[15]"
comment_5 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[6]/td[15]"
comment_6 = "/html/body/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[@id='green']/tbody/tr[7]/td[15]"





dog_link = driver.find_element_by_link_text('Gascoigne')
dog_link.get_attribute('href')

element = driver.find_element_by_xpath(sp_1)
element.get_attribute('innerHTML')
element.get_attribute('href')



print(date_of_meet.get_attribute('innerHTML'))


