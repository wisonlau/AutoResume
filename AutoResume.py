# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys


class AutoResume :
	def __init__(self, account_info) :
		# 需要自动刷新简历的网站
		self.job51_url = 'https://login.51job.com/login.php'
		self.job51_name = account_info['job51_name']
		self.job51_pass = account_info['job51_pass']
		self.zhaopin_url = 'https://www.zhaopin.com/'
		self.zhaopin_name = account_info['zhaopin_name']
		self.zhaopin_pass = account_info['zhaopin_pass']
		self.liepin_url = 'https://m.liepin.com/login/?url=https://m.liepin.com/cq/'
		self.liepin_name = account_info['liepin_name']
		self.liepin_pass = account_info['liepin_pass']

	def job51(self) :
		try :
			# 实例化对象
			driver = webdriver.Firefox()
			# 使用webdriver请求url
			driver.get(self.job51_url)
			# 定位元素，输入用户名和密码，然后进行提交操作
			driver.find_element_by_name("loginname").send_keys(self.job51_name)
			driver.find_element_by_name('password').send_keys(self.job51_pass)
			driver.find_element_by_tag_name('button').submit()
			sleep(3)
			# 定位元素，点击"刷新简历"
			driver.find_element_by_xpath("//div[@class='btnbox']/span[@class='p_but']").click()
			sleep(1)
			# 获取页面变化部分，因为该位置会变化成"刷新成功"
			result = driver.find_element_by_xpath("//div[@class='pannel_con']").text
			if "简历刷新成功！" in result :
				print(sys._getframe().f_code.co_name + "简历刷新成功！\n")
			driver.close()
		except Exception as e :
			print("出现异常，程序将退出！\n")
			print("具体错误信息如下：\n", e)
			sys.exit(1)

	def zhaopin(self) :
		try :
			driver = webdriver.Firefox()
			driver.get(self.zhaopin_url)
			driver.find_element_by_name("loginname").send_keys(self.zhaopin_name)
			driver.find_element_by_name('Password').send_keys(self.zhaopin_pass)
			driver.find_element_by_tag_name('button').submit()
			sleep(3)
			driver.find_element_by_xpath("//div[@class='zp-pfme-funcs']/a[@class='zp-pfme-funcs-link'][2]").click()
			print(sys._getframe().f_code.co_name + "简历刷新成功！\n")
			driver.close()
		except Exception as e :
			print("出现异常，程序将退出！\n")
			print("具体错误信息如下：\n", e)
			sys.exit(1)

	def liepin(self) :
		try :
			driver = webdriver.Firefox()
			driver.get(self.liepin_url)
			driver.find_element_by_name("user_login").send_keys(self.liepin_name)
			driver.find_element_by_css_selector('div.inputzone:nth-child(3) > input:nth-child(2)').send_keys(
				self.liepin_pass)
			driver.find_element_by_tag_name('button').submit()
			sleep(3)
			link = driver.find_element_by_css_selector(
				'div.liepin-channel-list:nth-child(8) > div:nth-child(4) > a:nth-child(1)').get_attribute('href')
			driver.get(link)
			driver.find_element_by_css_selector('a.btn:nth-child(2)').click()
			if driver.get_screenshot_as_file("success.png") :
				print(sys._getframe().f_code.co_name + '简历刷新成功！\n')
			driver.close()
		except Exception as e :
			print("出现异常，程序将退出！\n")
			print("具体错误信息如下：\n", e)
			sys.exit(1)


if __name__ == '__main__' :
	account_info = {
		'job51_name' : '122022066@qq.com', 'job51_pass' : 'pass',
		'zhaopin_name' : '122022066@qq.com', 'zhaopin_pass' : 'pass',
		'liepin_name' : '122022066@qq.com', 'liepin_pass' : 'pass'
	}
	job = AutoResume(account_info)
	job.job51()
	job.zhaopin()
	job.liepin()
