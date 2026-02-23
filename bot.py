import os
import smtplib
import random
import time
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# الإعدادات من Secrets
GEMINI_KEY = os.getenv("GEMINI_KEY")
MY_EMAIL = "oedn305@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

def run_bot():
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash') # الفلاش أخف على الكوتا

    topic = random.choice(["نيوم وذا لاين 2026", "مستقبل العملات الرقمية", "الذكاء الاصطناعي في حياتنا"])
    print(f"🚀 محاولة توليد مقال عن: {topic}")
    
    try:
        # طلب المحتوى
        response = model.generate_content(f"كتب مقال قصير واحترافي لمدونة بلوجر عن {topic} بالعربي والانجليزي بتنسيق HTML.")
        
        # إرسال الإيميل
        msg = MIMEMultipart()
        msg['Subject'] = f"حصري: {topic}"
        msg['From'] = MY_EMAIL
        msg['To'] = BLOGGER_EMAIL
        msg.attach(MIMEText(response.text, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(MY_EMAIL, EMAIL_PASS)
            server.send_message(msg)
        print("✅ تم الإرسال والنشر في بلوجر بنجاح!")

    except Exception as e:
        if "429" in str(e):
            print("⚠️ تنبيه: الكوتا انتهت. انتظر 10 دقائق أو استبدل المفتاح.")
        else:
            print(f"❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    run_bot()
