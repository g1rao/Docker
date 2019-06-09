#https://github-production-release-asset-2e65be.s3.amazonaws.com/25354393/29ab6e00-234f-11e9-84e0-fe6763b256e6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20190609%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190609T154034Z&X-Amz-Expires=300&X-Amz-Signature=5579bfbffd035ee28c936907875718cba62838b7b6f80057a9661d9fe0fe870b&X-Amz-SignedHeaders=host&actor_id=23398697&response-content-disposition=attachment%3B%20filename%3Dgeckodriver-v0.24.0-win64.zip&response-content-type=application%2Foctet-stream

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def start_streaming():
	browser = webdriver.Firefox(executable_path=r"C:\Users\G1\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe")
	browser.get("https://www.hotstar.com/sports/cricket/icc-cricket-world-cup-england-and-wales-2019/india-vs-australia-m190726/live-streaming/1440000692?lang=eng")
	wait = WebDriverWait(browser, 10)
	play = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/button[1]")))
	actions = ActionChains(browser)
	actions.move_to_element(play)
	actions.click()
	actions.perform()
	#play.click()
	time.sleep(5)
	wait = WebDriverWait(browser, 10)
	fullscreen = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/button[2]")))
	actions = ActionChains(browser)
	actions.move_to_element(fullscreen)
	actions.click()
	actions.perform()
	wait = WebDriverWait(browser, 350)
	session_expire = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div")))
	browser.quit()
for i in range(10):
	start_streaming()
