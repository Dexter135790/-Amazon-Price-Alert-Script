# 🛒 Amazon Price Alert Script 

A Python-based project that tracks product prices on Amazon and sends an email alert when the price drops below a specified target value. Perfect for staying ahead of sales and ensuring you never miss a great deal!

##  🚀 Features

- Scrape Product Information: Automatically fetch product details, including the title and current price.
- Price Tracking: Compare the current price with a target value.
- Email Notifications: Receive an email alert if the product price drops below your desired target.
- Configurable: Easily set your target price and email settings via a .env file.

## 🛠️ Technologies Used 

- Python 🐍
- Beautiful Soup: For web scraping.
- Requests: To fetch web pages.
- smtplib: For sending emails.
- dotenv: For managing environment variables securely.

## 📋 Prerequisites
Before running this script, ensure you have the following:
- Python 3.7 or above installed.
- An email account for sending alerts (e.g., Gmail).
- Required Python libraries installed (see below).

## ⚙️ Setup Instructions

1. Clone the Repository
```
git clone https://github.com/yourusername/amazon-price-alert.git
cd amazon-price-alert
```

2. Install Dependencies
```
pip install -r requirements.txt
```

3. Configure Environment Variables

Create a .env file in the root directory with the following content:
```
EMAIL_ADDRESS=your-email@example.com
EMAIL_APP_PASSWORD=your-email-app-password
SMTP_ADDRESS=smtp.example.com
RECEIVER_EMAIL_ADDRESS=receiver-email@example.com
```
Replace the placeholder values with: 
- EMAIL_ADDRESS: Your sender email address.
- EMAIL_APP_PASSWORD: Your email app password (not your actual email password; use an app-specific password for security).
- SMTP_ADDRESS: SMTP server for your email provider (e.g., Gmail’s is smtp.gmail.com).
- RECEIVER_EMAIL_ADDRESS: The recipient email address for price alerts.

4. Run the Script
```
python main.py
```

## 📝 How It Works 

- The script fetches the HTML of the Amazon product page using Requests.
- Beautiful Soup parses the HTML to extract the product title and price.
- The extracted price is compared with your specified target price.
- If the current price is lower or equal to the target price:
	•	An email is sent to the recipient with the product details and a link to the Amazon product page.

## 🎉 Demo 

[Demonstration](https://drive.google.com/file/d/17fCqWfaMcrvH6r6YGqcZtL8yg0H0VaTS/view?usp=sharing)





