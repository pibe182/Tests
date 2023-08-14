from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()  

# Open the URL
driver.get("https://demo.evershop.io/")

# Click Sign in button
sign_in_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[2]/a/svg')
sign_in_button.click()

# Esperar a que se cargue la página de productos
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Create an account")))

# Click Create an account
create_account_button = driver.find_element(By.LINK_TEXT, "Create an account")
create_account_button.click()

# Esperar a que se cargue la página de productos
element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button")))

# Fill in "Full Name", "Email" and "Password" fields
full_name_field = driver.find_element(By.NAME, "full_name")
email_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")

full_name_field.send_keys("John Doe")
email_field.send_keys("johndoe@example.com")
password_field.send_keys("securepassword")

# Click "SIGN UP"
sign_up_button = driver.find_element(By.CLASS_NAME, "button")
sign_up_button.click()

# Locate the element by its text content using XPath
shop_kids_button = driver.find_element(By.XPATH, "//a[contains(@class, 'button primary') and span[text()='Shop kids']]")

# Perform actions with the located element
shop_kids_button.click()

shoesbutton1 = driver.find_element(By.XPATH, "//a[@class='font-bold hover:underline h5' and span[text()='Canvas platform chuck taylor all star']]")
shoesbutton1.click()

element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "outline")))

# Locate the input element by its name attribute
qty_input = driver.find_element(By.NAME, "qty")

# Clear the current value and set it to "2"
qty_input.clear()
qty_input.send_keys("2")

size1 = driver.find_element(By.LINK_TEXT, "S")
size1.click()

color1 = driver.find_element(By.LINK_TEXT, "White")
color1.click()

addtocart = driver.find_element(By.CLASS_NAME, "outline")
addtocart.click()

element31 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "VIEW CART")))

goback = driver.find_element(By.LINK_TEXT, "Kids")
goback.click()

# Esperar a que se cargue la página de productos
element4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='font-bold hover:underline h5' and span[text()='Canvas platform chuck taylor all star']]")))

shoesbutton2 = driver.find_element(By.XPATH, "//a[@class='font-bold hover:underline h5' and span[text()='Chuck taylor all sar move']]")
shoesbutton2.click()

element5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "outline")))

# Locate the input element by its name attribute
qty_input2 = driver.find_element(By.NAME, "qty")

# Clear the current value and set it to "3"
qty_input2.clear()
qty_input.send_keys("3")

size2 = driver.find_element(By.LINK_TEXT, "L")
size2.click()

color2 = driver.find_element(By.LINK_TEXT, "Brown")
color2.click()

addtocart = driver.find_element(By.CLASS_NAME, "outline")
addtocart.click()

element51 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "VIEW CART")))

goback = driver.find_element(By.LINK_TEXT, "Kids")
goback.click()

# Esperar a que se cargue la página de productos para hacer 3ra compra
element6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='font-bold hover:underline h5' and span[text()='Canvas platform chuck taylor all star']]")))

shoesbutton3 = driver.find_element(By.XPATH, "//a[@class='font-bold hover:underline h5' and span[text()='Mix nad match all taylor all star']]")
shoesbutton3.click()

element7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "outline")))

size3 = driver.find_element(By.LINK_TEXT, "L")
size3.click()

color3 = driver.find_element(By.LINK_TEXT, "Brown")
color3.click()

addtocart = driver.find_element(By.CLASS_NAME, "outline")
addtocart.click()

element71 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "VIEW CART")))

viewcart = driver.find_element(By.LINK_TEXT, "VIEW CART")
viewcart.click()

# Go to Checkout page and click on Checkout
element8 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "CHECKOUT")))
checkout_button = driver.find_element(By.LINK_TEXT, "CHECKOUT")
checkout_button.click()

# Fill the shipping address and submit
# Locate the input element by its name attribute
full_name_input = driver.find_element(By.NAME, "address[full_name]")

# Clear the current value and write a new value
full_name_input.clear()
full_name_input.send_keys("John Doe")

# Locate the input element by its name attribute
telephone_input = driver.find_element(By.NAME, "address[telephone]")

# Clear the current value and write a new value
telephone_input.clear()
telephone_input.send_keys("5119999999")  

# Locate the input element by its name attribute
address_input = driver.find_element(By.NAME, "address[address_1]")

# Clear the current value and write a new value
address_input.clear()
address_input.send_keys("Miami Beach")  

# Locate the input element by its name attribute
city = driver.find_element(By.NAME, "address[city]")

# Clear the current value and write a new value
city.clear()
city.send_keys("Miami")  

# Locate the dropdown country by its ID
dropdown = Select(driver.find_element(By.ID, "address[country]"))

# Select the option by visible text
dropdown.select_by_visible_text("United States")

# Wait for the province dropdown options to appear
try:
    province_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address[province]")))
except:
    print("Province dropdown did not appear after selecting the country.")
    driver.quit()
else:
    # Select the province
    province_select = Select(province_dropdown)
    province_select.select_by_visible_text("Florida")

# Locate the input element by its name attribute
postcode_input = driver.find_element(By.NAME, "address[postcode]")

# Clear the current value and write a new value
postcode_input.clear()
postcode_input.send_keys("1070")  

# Wait for the radio buttons to appear
try:
    radio_buttons = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[type='radio']")))
except:
    print("Radio buttons did not appear after filling the fields.")
    driver.quit()
else:
    radio_buttons[0].click()

continuebutton = driver.find_element(By.CLASS_NAME, "primary")
continuebutton.click()

waitradiobutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "primary")))

# Locate the SVG radio button element by its attributes using XPath
svg_radio_button = driver.find_element(By.XPATH, "//svg[circle[@cx='12' and @cy='12']]")

# Perform actions with the located SVG radio button element
svg_radio_button.click()

orderbutton = driver.find_element(By.CLASS_NAME, "primary")
orderbutton.click()

  # Wait for the Order Confirmation page to load
try:
    order_confirmation_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='CONTINUE SHOPPING']")))
except:
    print("Order Confirmation page did not load.")
    driver.quit()
else:
    # Assertion: Verify Contact Information
    contact_info = driver.find_element(By.XPATH, "//div[@class='text-textSubdued' and preceding-sibling::div[text()='Shipping Address']]")
    assert contact_info.text == "johndoe@example.com", "Contact information is incorrect"

# Assertion: Verify Shipping Address
nameinfo = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]')
assert nameinfo.text == "John Doe", f'Error: el nombre no coincide. Actual name: {nameinfo.text}'

addressshippinginfo = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]')
assert addressshippinginfo.text == "Miami Beach", f'Error: la shipping address no coincide. Actual address: {addressshippinginfo.text}'

city_postalcode_info = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[1]')
assert city_postalcode_info.text == "1070, Miami", f'Error: la ciudad o codigo postal no coinciden. Actual City and Postal Code: {city_postalcode_info.text}'

province_country_info = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]')
assert province_country_info.text == "Florida, United States", f'Error: el estado o país no coinciden. Actual province and country: {province_country_info.text}'

telephoneinfo = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[4]')
assert telephoneinfo.text == "5119999999", f'Error: el telefono no coincide. Actual telephone: {telephoneinfo.text}'

  
# Assertion: Verify Billing Address
nameinfo2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]')
assert nameinfo2.text == "John Doe", f'Error: el nombre no coincide. Actual name: {nameinfo2.text}'

addressbillinginfo = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]')
assert addressbillinginfo.text == "Miami Beach", f'Error: la shipping address no coincide. Actual address: {addressbillinginfo.text}'

city_postalcode_info2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div[1]')
assert city_postalcode_info2.text == "1070, Miami", f'Error: la ciudad o código postal no coinciden. Actual City and Postal Code: {city_postalcode_info2.text}'

province_country_info2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div[2]')
assert province_country_info2.text == "Florida, United States", f'Error: el estado o país no coinciden. Actual province and country: {province_country_info2.text}'

telephoneinfo2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[4]')
assert telephoneinfo2.text == "5119999999", f'Error: el telefono no coincide. Actual telephone: {telephoneinfo2.text}'

# Assertion: Verify Payment Information
payment_method = driver.find_element(By.XPATH, "//div[@class='text-textSubdued' and preceding-sibling::div[text()='Payment Method']]")
assert payment_method.text == "Cash On Delivery", "Payment information is incorrect"

# Assertion: Verify Ordered Items 
ordered_items1 = driver.find_element(By.XPATH, '//*[@id="summary-items"]/table/tbody/tr[1]/td[2]/div/div[1]/span')
assert ordered_items1.text == "Your ordered items", "Ordered items are incorrect"

ordered_items2 = driver.find_element(By.XPATH, '//*[@id="summary-items"]/table/tbody/tr[2]/td[2]/div/div[1]/span')
assert ordered_items2.text == "Your ordered items", "Ordered items are incorrect"

ordered_items3 = driver.find_element(By.XPATH, '//*[@id="summary-items"]/table/tbody/tr[3]/td[2]/div/div[1]/span')
assert ordered_items3.text == "Your ordered items", "Ordered items are incorrect"

print("All assertions passed. Order was created successfully.")

# Close the browser
driver.quit()

