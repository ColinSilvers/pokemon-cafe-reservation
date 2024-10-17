from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to ChromeDriver
chrome_driver_path = r"C:\Users\13018\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object for ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Optional, remove if you want to see the browser window

# Start the service
service.start()

# Initialize WebDriver with the Service object
driver = webdriver.Chrome(service=service, options=options)

# Open Google and print the title
driver.get('http://www.google.com')
print(driver.title)

# Quit the driver and stop the service
driver.quit()
service.stop()
