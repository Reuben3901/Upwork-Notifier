from selenium import webdriver
import time, os, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pygame import mixer

driver = webdriver.Firefox()

postingIds = []


driver.get("https://www.upwork.com/")

def play_music():
    mixer.init()
    mixer.music.load('sms-alert.mp3')
    mixer.music.play()

def main():
    try:
        driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div[5]/div[2]/div/button').click()
        search()
    except:
        pass
    
def search():
    time.sleep(2)
    posts = driver.find_elements_by_class_name('job-title-link')
    times = driver.find_elements_by_tag_name('time')
    for i,post in enumerate(posts):
        if post.text in postingIds: continue
        if 'day' in times[i].text: continue
        print("Job Title => '" + post.text + "'   " + times[i].text)
        postingIds.append(post.text)
    play_music()

input('Input your login information and navigate to jobs page, wait for page to load, then hit enter to continue')

search()

while True:
    main()
    rand = random.randint(100, 300)
    print("Refreshing at: " + time.asctime( time.localtime(time.time() + rand) ) )
    time.sleep(rand)

