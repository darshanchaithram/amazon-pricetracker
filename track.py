import smtplib
from selenium import webdriver

coptions = webdriver.ChromeOptions()
coptions.add_argument('headless')
browser = webdriver.Chrome(options = coptions)
browser.get("https://www.amazon.in/Sony-Extra-Bass-MDR-XB450AP-Headphones/dp/B00SISQAX2/ref=sr_1_1?dchild=1&keywords=Sony+MDR-XB450AP&qid=1624419350&sr=8-1")
price = browser.find_element_by_id('priceblock_ourprice').text
price = price[2:]
price = price[0]+price[2:5]
price = int(price)
print(price)

receiver = 'ENTER YOUR MAIL ID'   #enter your mail id here
subject = 'Sony MDRXB-450AP price drop!'
body = 'Rs.' + str(price) + '\n Sony MDRXB 450AP is now under your budget. \n\n https://www.amazon.in/Sony-Extra-Bass-MDR-XB450AP-Headphones/dp/B00SISQAX2/ref=sr_1_1?dchild=1&keywords=Sony+MDR-XB450AP&qid=1624419350&sr=8-1'

message = f'subject: {subject}\n\n{body}'
def sendmail(receiver, message):
    server = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login('ENTER BOT MAIL ID','ENTER BOT MAIL PASSWORD')   #enter bot email and password here
    server.sendmail('BOT MAIL ID', receiver, message)
    server.quit()

if(price < 2000):  #enter your budget amount here
    sendmail(receiver, message)
else:
    print("Still above your budget")
