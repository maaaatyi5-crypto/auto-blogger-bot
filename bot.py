import os
import smtplib
import random
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات العلوية ---
GEMINI_KEY = os.getenv("GEMINI_KEY")
MY_EMAIL = "oedn305@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

# إعداد نموذج Gemini 2.0 Flash الجديد
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-2.0-flash') 

def run_bot():
    try:
        # اختيار موضوع ترند 2026
        topic = random.choice([
            "مستقبل العملات الرقمية في 2026",
            "أحدث تقنيات الذكاء الاصطناعي 2.0",
            "تطورات مدينة نيوم والمشاريع السعودية",
            "Future of AI and Robotics 2026"
        ])
        
        print(f"🚀 البدء في توليد مقال عبر Gemini 2.0 عن: {topic}")
        
        # طلب المحتوى بتنسيق HTML احترافي
        prompt = f"Write a professional HTML blog post about {topic} in Arabic and English. Use <h2> and <b> tags."
        response = model.generate_content(prompt)
        
        # تجهيز رسالة الإيميل لنظام النشر التلقائي (trand2)
        msg = MIMEMultipart()
        msg['Subject'] = f"حصري ترند 2026: {topic}"
        msg['From'] = MY_EMAIL
        msg['To'] = BLOGGER_EMAIL
        msg.attach(MIMEText(response.text, 'html'))

        # الاتصال بسيرفر Gmail والإرسال
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(MY_EMAIL, EMAIL_PASS)
            server.send_message(msg)
            
        print(f"✅ تم النشر بنجاح في بلوجر باستخدام Gemini 2.0!")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")
        if "429" in str(e):
            print("💡 تنبيه: الحساب وصل للحد الأقصى (Quota)، انتظر قليلاً أو غير المفتاح.")

if __name__ == "__main__":
    run_bot()
