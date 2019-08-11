#Install selenium package
#Install webDriver from https://www.seleniumhq.org/download/
from selenium import webdriver

path = "C:\Users\Sid Ali\Downloads\chromedriver\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.get("https://google.com")

