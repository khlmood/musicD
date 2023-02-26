from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.html5.application_cache import ApplicationCache
from selenium.webdriver.common.keys import Keys
from time import sleep

class Download:
    def __init__(self):
        self.songs = []

    def download_song(self, song_name):
        driver = webdriver.Chrome()

        website = "https://www.mp3juices.cc/2d0851"
        driver.get(website)
        sleep(3)
        form = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form")
        input_field = form.find_element(By.XPATH, "//input[@id='query']")
        self.del_input(input_field)
        input_field.send_keys(song_name)
        sleep(3)
        button = form.find_element(By.XPATH, "//button[@id='button']")
        button.click()
        sleep(5)
        download_div = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[3]")
        sleep(5)
        download_button = download_div.find_element(By.CLASS_NAME, "download")
        download_button.click()
        sleep(5)
        down = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/a[1]")
        down.click()
        sleep(10)
        if driver.current_url != website:
            driver.close()
        sleep(15)

        self.wait_for_downloads(driver)
        driver.quit()

    def wait_for_downloads(driver):
        cache = driver.application_cache
        status = cache.status
        if status == driver.application_cache.DOWNLOADING:
            print("Downloads in progress...")
        while status != driver.application_cache.IDLE:
            status = cache.status

    def del_input(self, input_field):
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)

    def add_song(self, song):
        self.songs.append(song)

    def download(self):
        for song in self.songs:
            self.download_song(song)
        self.songs.clear()

music = Download()
music.add_song("the weeknd starboy")
music.download()