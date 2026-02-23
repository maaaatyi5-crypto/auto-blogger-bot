import os
import smtplib
import random
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
    model = genai.GenerativeModel('gemini-2.0-flash')

    topic = random.choice(["Crypto 2026", "AI Trends", "Future Tech"])
    
    # محاولة التوليد مع خاصية الانتظار الذكي
    for attempt in range(3): # سيحاول 3 مرات قبل أن يستسلم
        try:
            print(f"🚀 محاولة رقم {attempt + 1}: توليد مقال عن {topic}...")
            response = model.generate_content(f"Write a professional blog post about {topic} in Arabic and English with HTML tags.")
            
            # إذا نجح التوليد، ننتقل للإرسال
            msg = MIMEMultipart()
            msg['Subject'] = f"Trand2 Update: {topic}"
            msg['From'] = MY_EMAIL
            msg['To'] = BLOGGER_EMAIL
            msg.attach(MIMEText(response.text, 'html'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(MY_EMAIL, EMAIL_PASS)
                server.send_message(msg)
            
            print("✅ مبروك! نجحت العملية وتم النشر.")
            return # إنهاء البرنامج بنجاح

        except Exception as e:
            if "429" in str(e):
                print(f"⚠️ زحام في السيرفر (429). سأنتظر 60 ثانية ثم أحاول مجدداً...")
                time.sleep(60) # انتظر دقيقة كاملة ليرتاح السيرفر
            else:
                print(f"❌ خطأ غير متوقع: {e}")
                break

if __name__ == "__main__":
    run_bot()
