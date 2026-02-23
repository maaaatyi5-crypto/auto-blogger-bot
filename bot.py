import os
import smtplib
import time
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# جلب الإعدادات من GitHub Secrets (تأكد من تسميتها هكذا في جيت هب)
GEMINI_KEY = os.getenv("GEMINI_KEY")
MY_EMAIL = "oedn305@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

def run_bot_v2():
    # إعداد جمانيا 2 بالمفتاح اللي أخذته
    genai.configure(api_key=GEMINI_KEY)
    
    # هنا التحديث: استخدام موديل جمانيا 2 (gemini-2.0-flash)
    model = genai.GenerativeModel('gemini-2.0-flash')

    print(f"🚀 جاري العمل باستخدام محرك جمانيا 2...")
    
    for attempt in range(3):
        try:
            # طلب محتوى ذكي من جمانيا 2
            response = model.generate_content("اكتب مقالاً تقنياً قصيراً عن مستقبل الذكاء الاصطناعي في 2026 بتنسيق HTML.")
            
            msg = MIMEMultipart()
            msg['Subject'] = "🌟 مقال جديد بواسطة جمانيا 2"
            msg['From'] = MY_EMAIL
            msg['To'] = BLOGGER_EMAIL
            msg.attach(MIMEText(response.text, 'html'))

            # إرسال الإيميل
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(MY_EMAIL, EMAIL_PASS)
                server.send_message(msg)
            
            print("✅ تم التشغيل بنجاح! جمانيا 2 قام بالمهمة.")
            return

        except Exception as e:
            print(f"⚠️ المحاولة {attempt+1} فشلت: {e}")
            time.sleep(60) # انتظر دقيقة في حال وجود زحام

if __name__ == "__main__":
    run_bot_v2()
