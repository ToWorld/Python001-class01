from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=options)
def weibo_login(username, password): 
	// step1: 登录首页
	browser.get('https://shimo.im/login?from=home') 
	browser.implicitly_wait(5) 
	time.sleep(1) 
	// step2: 找到用户名input
	browser.find_element_by_name("mobileOrEmail").send_keys(mobile) 
	// step3: 找到密码input
	browser.find_element_by_name("password").send_keys(password) 
	time.sleep(5)
	// step4: 找到登陆button
	browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div/div[1]/button").click()
	time.sleep(1)
mobile = 'xx'
password = 'xx'
weibo_login(mobile, password)
