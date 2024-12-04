from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
import re

load_dotenv()


practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


headers = {
    "Accept-Language": "en-US,en-IN;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "upgrade-insecure-requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "priority": "u=0, i",
}

response = requests.get(live_url, headers=headers)
html_code = response.text
# print(html_code)

soup = BeautifulSoup(html_code, "html.parser")

item_title = soup.find(id="productTitle").getText()
item_title = re.sub(r'\s+', ' ', item_title).strip()
# print(item_title)

price = soup.find(class_="aok-offscreen").getText()[4:-2]
float_price = float(price)
print(float_price)


target_value = 100

with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587) as connection:
    connection.starttls()
    connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("EMAIL_APP_PASSWORD"))
    if float_price <= target_value:
        msg = MIMEMultipart()
        msg["From"] = os.getenv("EMAIL_ADDRESS")
        msg["To"] = os.getenv("RECEIVER_EMAIL_ADDRESS")
        msg["Subject"] = "Amazon Price Alert!!"  # Add the subject

        # Add the body text
        body = f"{item_title} is {float_price} \n {live_url}"
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # Send the email
        connection.sendmail(
            from_addr=msg["From"],
            to_addrs=msg["To"],
            msg=msg.as_string()
        )





