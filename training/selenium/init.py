from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your ChromeDriver executable
driver_path = '/usr/local/bin/chromedriver'

# Replace with your Instagram username and password
username = 'dmmechatbot'
password = 'ortabayir123'

# Launch Chrome and navigate to the Instagram login page
driver = webdriver.Chrome(driver_path)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

# Enter your login details and submit the form
username_field = driver.find_element_by_name('username')
username_field.send_keys(username)
password_field = driver.find_element_by_name('password')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete and navigate to the DMs
time.sleep(5) # Wait for the login to complete
driver.get('https://www.instagram.com/direct/inbox/')

# Wait for the DMs to load and click on the first conversation
time.sleep(5) # Wait for the DMs to load
for x in driver.find_elements_by_tag_name("button"):
    if x.text == 'Şimdi Değil':
        x.click()

# conversation = driver.find_element_by_css_selector('div._7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv')
conversation_name = "Görkem Koç"
conversation = driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(conversation_name))
conversation.click()

# Wait for the conversation to load and send a message
time.sleep(5) # Wait for the conversation to load
message_field = driver.find_element_by_tag_name("textarea")
message_field.send_keys('Hello, this is an automated message!')
message_field.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
