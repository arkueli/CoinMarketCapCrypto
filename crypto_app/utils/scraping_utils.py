import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

def scrape_data():
    chrome_driver_path = os.path.join("C:", "Users", "HP 840G5", "Desktop", "chrome_driver", "chromedriver_win32", "chromedriver.exe")
    #chrome_driver_path = r'C:\Users\HP 840G5\Desktop\chrome_driver\chromedriver_win32\chromedriver.exe' 
  
    service = Service(chrome_driver_path)
    chrome_options = Options()
    #options.add_argument("--headless") 
    driver = webdriver.Chrome(service=service, options=chrome_options)
 
    
    url = 'https://coinmarketcap.com/all/views/all/?start=1&limit=200'
    driver.get(url)   

    wait = WebDriverWait(driver, 10) 
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cmc-table-row')))  
    time.sleep(2)  
    page_source = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
   
    crypto_list = soup.find_all('tr', {'class': 'cmc-table-row'})

    data = []  
    for crypto in crypto_list:  
        try: 
            price = crypto.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).get_text(strip=True).replace('$', '')
            one_hour = crypto.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h'}).get_text(strip=True).replace('-', '').replace('%', '').replace('<', '')
            one_hour = re.sub(r'[-%<]', '', one_hour.get_text(strip=True))
            twenty_four_hours = re.sub(r'[-%<]', '', twenty_four_hours.get_text(strip=True))                 
            seven_days = re.sub(r'[-%<]', '', seven_days.get_text(strip=True))
            
            data.append({
                'Rank': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True),
                'Name': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True).replace('Bitcoin', ''),
                'Symbol': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True).replace('BTC', ''),
                'Market_Cap': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True).replace('$', ''),              
                'Price' : round(float(re.sub(r'\.\.\.|[,.]', lambda m: '000' if m.group(0) == '...' else '', price)), 4) if price else None,
                'Circulating_supply': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True).replace('19,400,587 BTC', ''),
                'Volume_24h': crypto.find('td', {'class': 'cmc-table__cell'}).get_text(strip=True).replace('$11,772,175,099', ''),
                'One_hour': round(float(one_hour), 2) if one_hour else None,
                'twenty_four_hours': round(float(twenty_four_hours)) if twenty_four_hours else None,
                'seven_days': round(float(seven_days), 2) if seven_days else None,
            })
        except AttributeError:
            break
    
    driver.quit()  
    return data













































