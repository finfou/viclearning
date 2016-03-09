from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SmzdmTasks:
	def DailyCheckin(self):
		dr = webdriver.Firefox()
		# dr.implicitly_wait(30)
		dr.get("http://www.smzdm.com")

		ele = dr.find_element_by_id("login_window")
		ele.click()

		dr.switch_to_frame("zhiyou_login_window_iframe")
		dr.find_element_by_id("username")
		username_i = dr.find_element_by_id("username")
		username_i.send_keys('13661813699')
		password_i = dr.find_element_by_id("password")
		password_i.send_keys('smzdm060703')
		login_b = dr.find_element_by_id('login_submit')
		login_b.click()
		#sleep(5)
		check_in = WebDriverWait(dr, 10).until(
			EC.presence_of_element_located((By.ID, "user_info_tosign"))
		)
		# check_in = dr.find_element_by_id('user_info_tosign')
		check_in.click()
		dr.close()


if __name__ == "__main__":
	tasks = SmzdmTasks()
	tasks.DailyCheckin()