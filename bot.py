import os
import smtplib
import time
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# الإعدادات
GEMINI_KEY = os.getenv("GEMINI_KEY")
MY_EMAIL = "oedn305@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

def run_bot():
    genai.configure(api_key=GEMINI_KEY)
    # استخدام موديل أقدم قليلاً لتجاوز زحام الموديل الجديد
    model = genai.GenerativeModel('gemini-1.5-flash')

    print(f"🚀 محاولة طوارئ لتجاوز حظر 429...")
    
    for attempt in range(2):
        try:
            # طلب مقال قصير جداً لضمان المرور من السيرفر
            response = model.generate_content("Write a 100-word blog about Tech 2026 in Arabic and English HTML.")
            
            msg = MIMEMultipart()
            msg['Subject'] = "Trand2 Emergency Post"
            msg['From'] = MY_EMAIL
            msg['To'] = BLOGGER_EMAIL
            msg.attach(MIMEText(response.text, 'html'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(MY_EMAIL, EMAIL_PASS)
                server.send_message(msg)
            
            print("✅ أخييييراً! نجحت العملية.")
            return

        except Exception as e:
            print(f"⚠️ المحاولة {attempt+1} فشلت: {e}")
            time.sleep(120) # انتظر دقيقتين كاملتين بين المحاولات

if __name__ == "__main__":
    run_bot()
