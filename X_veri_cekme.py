import selenium
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

subject = "deprem until:2023-02-26 since:2023-02-07"


# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("kullanici adi")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'İleri')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('sifre')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Giriş yap')]")
log_in.click()

# Search item and fetch it
sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)


sleep(3)
latest = driver.find_element(By.XPATH,"//span[contains(text(),'En Son')]")
latest.click()

TweetSayisi = 3000
ekle = []

for i in range(TweetSayisi + 7):
    body = driver.find_element(By.TAG_NAME, 'body')  # body öğesini her döngüde yeniden bul
    body.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(10)  # Sayfanın tamamen yüklenmesini beklemek için 10 saniye bekle
    sleep(1)
    try:
        dex = driver.find_element(By.XPATH,"//article[@data-testid='tweet']").text
        if dex not in ekle:
            ekle.append(dex)
        sleep(1)
    except:
        pass

driver.implicitly_wait(10)  # Sayfanın tamamen yüklenmesini beklemek için 10 saniye bekle
sleep(1)
print(str(len(ekle)), "tane tweet, tweet.txt dosyasına kaydedildi.")
adet=1
yaz = open('deprem.txt', 'w', encoding="utf-8")
for i in ekle:
    yaz.write(f"{adet}-{i} + \n")
    yaz.write("-----------------------------------------" + "\n")
    adet+=1
yaz.close()

# WebDriver'ı kapat
driver.quit()

