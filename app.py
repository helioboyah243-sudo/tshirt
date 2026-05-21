import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Unic Wears | متجر ملابس السباقات", page_icon="🏁", layout="wide")

# ديزاين السباقات بالـ CSS (أحمر، كحل، ومربعات السباق)
st.markdown("""
<style>
    /* الخلفية الحمراء */
    .stApp { background-color: #ff4b4b; }
    
    /* شريط المربعات الكحل والأبيض (Racing Checkered Pattern) الفوق */
    header {
        background-image: repeating-linear-gradient(45deg, #000 25%, transparent 25%, transparent 75%, #000 75%, #000), repeating-linear-gradient(45deg, #000 25%, #fff 25%, #fff 75%, #000 75%, #000) !important;
        background-position: 0 0, 10px 10px !important;
        background-size: 20px 20px !important;
        height: 40px !important;
    }

    h1, h2, h3, p, .stMarkdown { color: white !important; text-align: center; font-family: 'Arial', sans-serif; }
    
    /* تصميم بطاقات السلعة بالكحل */
    .product-card {
        background-color: #111111;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #000000;
        box-shadow: 0 8px 16px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 25px;
        color: white !important;
    }
    
    .price { color: #ffffff; font-size: 26px; font-weight: bold; margin: 10px 0; background-color: #ff0000; padding: 5px; border-radius: 5px;}
    
    /* تنسيق القوائم المنسدلة */
    .stSelectbox div[data-baseweb="select"] { color: black !important; }
</style>
""", unsafe_allow_html=True)

# رأس الصفحة
st.title("🏁 UNIC WEARS - RACING COLLECTION")
st.write("### التشكيلة الحصرية لملابس السباقات - التوصيل لجميع المدن 🇲🇦")
st.write("---")

# معلومات السلعة الحقيقية ديالك (السميات والأثمنة كفما ف التصاور)
# ملاحظة: هادو روابط مؤقتة، خاصك تبدليهم بروابط تصاورك الحقيقيين من بعد
products = [
    {
        "name": "هودي أسود بنقوش شوكية - Tribal Black Hoodie",
        "price": "299 DH",
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?q=80&w=500" # تصويرة مؤقتة
    },
    {
        "name": "تيشرت ميامي F1 2026 - Miami F1 2026 Tee",
        "price": "189 DH",
        "image": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?q=80&w=500" # تصويرة مؤقتة
    },
    {
        "name": "هودي ريد بول ريسينغ - Red Bull Racing Hoodie",
        "price": "319 DH",
        "image": "https://images.unsplash.com/photo-1534961956603-913d99b403c1?q=80&w=500" # تصويرة مؤقتة
    }
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

WHATSAPP_NUMBER = "212612345678" # بدلي هادا برقمك الحقيقي بدون صفر

for idx, prod in enumerate(products):
    with cols[idx]:
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        
        # عرض التصويرة
        st.image(prod["image"], use_container_width=True)
        st.subheader(prod["name"])
        st.markdown(f'<p class="price">{prod["price"]}</p>', unsafe_allow_html=True)
        
        # خيارات المقاس
        size = st.selectbox(f"المقاس (Size) - {idx}", ["S", "M", "L", "XL", "XXL"], key=f"size_{idx}")
        
        # رسالة الواتساب الواجدة
        msg = f"السلام عليكم، بغيت نطلب: {prod['name']}\nالمقاس: {size}\nالثمن: {prod['price']}"
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"
        
        # زر الشراء
        st.link_button("🛒 اطلب الآن عبر الواتساب", whatsapp_url, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.write("<p style='font-size: 14px;'>WORLDWIDE SECURE DELIVERY 🇲🇦</p>", unsafe_allow_html=True)
st.write("<p style='font-size: 14px;'>© 2026 UNIC WEARS. All rights reserved.</p>", unsafe_allow_html=True)
