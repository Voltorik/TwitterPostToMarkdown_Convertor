# import a bunch of junk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import sys, os, re

def getInvalidChars():
    if os.name == 'nt': # windows
        return r'<>:"/\|?*'
    else:
        return r'/'

if len(sys.argv) > 1:
    target_url = sys.argv[1]
else:
    print("Not url was passed")
    exit()
    
# yes i use firefox
FFoptions = webdriver.FirefoxOptions()
FFoptions.add_argument("--headless")
driver = webdriver.Firefox(options=FFoptions)
driver.get(target_url)

try:
    element = WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetText']")))
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Tweet content is stored in the div with data-testid="tweetText" 
    tweet_content = driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetText']").text
    nameData = driver.find_element(By.CSS_SELECTOR, "div[data-testid='User-Name']").text.split("\n")
    timestamp = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")

    display_name = nameData[0]
    user_name = nameData[1]

    UTC_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_time = UTC_time.strftime("(%A) %B %d, %Y - %I:%M %p")

    # Set file title
    tweet_text = tweet_content.split(".")
    tweet_title = tweet_text[0]
    if len(tweet_title) > 40:
        tweet_title = tweet_title[:40]

    invalidChars = getInvalidChars()
    regex = re.compile(f'[{re.escape(invalidChars)}]')

    if regex.search(tweet_title):
        tweet_title = regex.sub('%', tweet_title)

    with open(f"{tweet_title}.md", "w") as file:
        file.write(f"{display_name} ({user_name})\n")
        file.write(f"{formatted_time}\n\n{tweet_content}\n\nURL: {target_url}")

except Exception as e:
    print(f"An error occured: {e}")

driver.quit()