from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your ChromeDriver executable
driver_path = '/path/to/chromedriver'

# Replace with your Instagram username and password
username = 'your_username'
password = 'your_password'

# Launch Chrome and navigate to the Instagram login page
driver = webdriver.Chrome(driver_path)
driver.get('https://www.instagram.com/accounts/login/')

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
conversation = driver.find_element_by_css_selector('div._7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv')
conversation.click()

# Wait for the conversation to load and send a message
time.sleep(5) # Wait for the conversation to load
message_field = driver.find_element_by_css_selector('textarea.IpSxo')
message_field.send_keys('Hello, this is an automated message!')
message_field.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
