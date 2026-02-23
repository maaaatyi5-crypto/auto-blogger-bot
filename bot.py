import os
import smtplib
import random
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# الإعدادات
GEMINI_KEY = os.getenv("GEMINI_KEY")
MY_EMAIL = "oedn305@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

genai.configure(api_key=GEMINI_KEY)
# استخدم نسخة flash لأنها أسرع وأقل استهلاكاً للكوتا
model = genai.GenerativeModel('gemini-2.0-flash')

def run_bot():
    topic = random.choice(["AI Trends 2026", "Crypto Future", "NEOM Tech"])
    print(f"🚀 محاولة توليد مقال عن: {topic}")
    
    try:
        # تقليل طول الطلب لتوفير الكوتا
        response = model.generate_content(f"Write a short HTML blog post about {topic} in Arabic and English.")
        
        # إعداد الإيميل
        msg = MIMEMultipart()
        msg['Subject'] = f"New Trend: {topic}"
        msg['From'] = MY_EMAIL
        msg['To'] = BLOGGER_EMAIL
        msg.attach(MIMEText(response.text, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(MY_EMAIL, EMAIL_PASS)
            server.send_message(msg)
        print("✅ تم النشر!")

    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    run_bot()
