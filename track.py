from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.amazon.in/Sony-Extra-Bass-MDR-XB450AP-Headphones/dp/B00SISQAX2/ref=sr_1_1?dchild=1&keywords=Sony+MDR-XB450AP&qid=1624419350&sr=8-1")

price2 = browser.find_element_by_id('priceblock_ourprice').text
print(price2)
