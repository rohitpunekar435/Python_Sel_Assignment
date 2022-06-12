from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class Test_Demo():
    def test_playback_speed(self):
           #Browser invoke
           driver_service = Service(executable_path=ChromeDriverManager().install())

           driver = webdriver.Chrome(service=driver_service)

           driver.implicitly_wait(10)

           #Window maximize
           driver.maximize_window()

           #Hit the URL
           driver.get("https://youtube.com")

           #Type desired video name in the search box
           search_box=driver.find_element("xpath","(//*[@id='search'])[3]")
           search_box.send_keys("Sciffer Reflexion Video")

           #Click on search button
           search_button = driver.find_element("xpath","//*[@id='search-icon-legacy']")
           search_button.click()

           #Click on required video in the search result
           req_video = driver.find_element("xpath","//*[text()='Sciffer Reflexion Video']")
           req_video.click()

           sleep(1)

           #Click on Settings button
           settings_btn = driver.find_element("xpath","//*[@class='ytp-button ytp-settings-button']")
           settings_btn.click()

           #Click on Playback speed button
           playback_speed = driver.find_element("xpath","(//*[@class='ytp-menuitem'])[1]")
           playback_speed.click()

           #Click on 0.25x speed
           lowest_speed = driver.find_element("xpath","//*[text()='0.25']")
           lowest_speed.click()

           #Verify that 0.25 speed is displayed on Playback speed menu
           validate_lowest_speed = driver.find_element("xpath","//*[@class='ytp-menuitem-content' and text()='0.25']").is_displayed()
           print(validate_lowest_speed)

           sleep(1)

           # Click on Playback speed button
           playback_speed = driver.find_element("xpath","(//*[@class='ytp-menuitem'])[1]")
           playback_speed.click()

           # Click on Normal speed
           normal_speed = driver.find_element("xpath","//*[text()='Normal']")
           normal_speed.click()

           # Verify that Normal speed is displayed on Playback speed menu
           validate_normal_speed = driver.find_element("xpath","//*[@class='ytp-menuitem-content' and text()='Normal']").is_displayed()
           print(validate_normal_speed)

           sleep(1)

           # Click on Playback speed button
           playback_speed = driver.find_element("xpath","(//*[@class='ytp-menuitem'])[1]")
           playback_speed.click()

           # Click on 2x speed
           max_speed = driver.find_element("xpath","//*[text()='2']")
           max_speed.click()

           # Verify that 2x speed is displayed on Playback speed menu
           validate_max_speed = driver.find_element("xpath","//*[@class='ytp-menuitem-content' and text()='2']").is_displayed()
           print(validate_max_speed)

           driver.close()
           driver.quit()

           print('User is able to increase & decrease the playback speed of video successfully')


demo_test=Test_Demo()
demo_test.test_playback_speed()


