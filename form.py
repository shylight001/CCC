from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello Kevin')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()