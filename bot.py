import os
import time
import random
import google.generativeai as genai

# جلب المفتاح من GitHub Secrets
GEMINI_KEY = os.getenv("GEMINI_KEY")

if not GEMINI_KEY:
    print("❌ Error: GEMINI_KEY is missing!")
    exit(1)

# إعداد الجيمني 2.0 فلاش
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_article():
    # كلمات بحث ترند لعام 2026
    keywords = [
        "أحدث تقنيات الذكاء الاصطناعي 2026",
        "Future of AI and Green Energy",
        "مستقبل الهيدروجين الأخضر في السعودية",
        "Top Tech Trends 2026"
    ]
    topic = random.choice(keywords)
    print(f"🚀 البدء في توليد موضوع: {topic}")

    prompt = (
        f"Write a professional SEO article about {topic}.\n"
        "Instructions:\n"
        "1. Arabic section first (dir='rtl') with h1 and h2 tags.\n"
        "2. Then English section (dir='ltr') with professional translation.\n"
        "3. Use HTML format and include emojis."
    )

    try:
        # تأخير بسيط لتجنب الزحام في البداية
        time.sleep(10) 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")
        return None

# تنفيذ الكود
content = generate_article()
if content:
    print("✅ تم توليد المقال بنجاح!")
    print(content[:500]) # طباعة جزء للتأكد من النتائج
else:
    print("❌ فشل في التوليد.")
    exit(1)
