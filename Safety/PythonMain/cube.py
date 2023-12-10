from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Firefox()

# Open the website
driver.get("https://www.google.com")

# Find an element by its name attribute and type some text
element = driver.find_element_by_name("g")
element.send_keys("Selenium")

# Click the search button
element.submit()

# Close the browser window
driver.quit()
