import streamlit as st
from PIL import Image
from moon_timeline import show_moon_timeline
from mars_timeline import show_mars_timeline
from archive_timeline import show_archive_timeline
from training_game import show_training_game

favicon = Image.open("assets/favicon.png")

st.set_page_config(
    page_title="SPACE LEGACY | NASA5-VT7",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "language" not in st.session_state:
    st.session_state.language = "VI"

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected" not in st.session_state:
    st.session_state.selected = ""

if "lang" in st.query_params:
    st.session_state.language = st.query_params["lang"]

if "page" in st.query_params and "selected" in st.query_params:
    st.session_state.page = st.query_params["page"]
    st.session_state.selected = st.query_params["selected"]

translations = {
    "VI": {
        "language": "Ngôn ngữ",
        "brand": "DI SẢN VŨ TRỤ",
        "subtitle": "KHÁM PHÁ DI SẢN CÔNG NGHỆ VŨ TRỤ",
        "description": "Những cỗ máy từng chạm đến Mặt Trăng và Sao Hỏa. Dù nhiệm vụ đã kết thúc, câu chuyện của chúng vẫn còn được lưu giữ.",
        "section": "HÀNH TRÌNH KHÁM PHÁ",
        "moon_title": "MẶT TRĂNG",
        "moon_desc": "Khám phá những thiết bị NASA từng gửi lên Mặt Trăng và những dấu tích chúng để lại.",
        "archive_title": "KHO TRỮ",
        "archive_desc": "Tìm hiểu những cỗ máy, công nghệ và thiết bị đã giúp nhân loại chinh phục những giới hạn của vũ trụ.",
        "mars_title": "SAO HỎA",
        "mars_desc": "Khám phá những robot thám hiểm và dấu tích công nghệ trên hành tinh đỏ.",
        "back": "← QUAY LẠI TRANG CHỦ",
        "moon_detail": "NHỮNG DẤU TÍCH TRÊN MẶT TRĂNG",
        "moon_text": "Mặt Trăng lưu giữ nhiều dấu tích của những sứ mệnh không gian. Từ các tàu thăm dò va chạm xuống bề mặt đến những thiết bị hạ cánh, mỗi thiết bị đều kể một câu chuyện về hành trình khám phá của nhân loại.",
        "archive_detail": "KHO TRỮ CÔNG NGHỆ VŨ TRỤ",
        "archive_text": "Kho Trữ là nơi lưu giữ kiến thức về công nghệ khám phá không gian, bổ sung cho hai phần Mặt Trăng và Sao Hỏa.",
        "mars_detail": "NHỮNG DẤU TÍCH TRÊN SAO HỎA",
        "mars_text": "Sao Hỏa đã trở thành nơi hoạt động của nhiều robot thám hiểm. Những thiết bị này giúp con người nghiên cứu địa hình, khí hậu và lịch sử của hành tinh đỏ.",
        "footer": "DI SẢN VŨ TRỤ · KHÁM PHÁ QUÁ KHỨ · TRUYỀN CẢM HỨNG TƯƠNG LAI"
    },

    "EN": {
        "language": "Language",
        "brand": "SPACE HERITAGE",
        "subtitle": "EXPLORE THE LEGACY OF SPACE TECHNOLOGY",
        "description": "Machines that once reached the Moon and Mars. Their missions may have ended, but their stories remain.",
        "section": "EXPLORE THE UNKNOWN",
        "moon_title": "THE MOON",
        "moon_desc": "Explore NASA hardware sent to the Moon and discover the traces they left behind.",
        "archive_title": "THE ARCHIVES",
        "archive_desc": "Discover machines, technologies, and equipment that helped humanity conquer the limits of the universe.",
        "mars_title": "MARS",
        "mars_desc": "Explore robotic explorers and the traces of technology on the Red Planet.",
        "back": "← BACK TO HOME",
        "moon_detail": "LEGACY ON THE MOON",
        "moon_text": "The Moon preserves traces of many space missions. From impact probes to lunar landers, every piece of hardware tells a story about humanity's exploration.",
        "archive_detail": "SPACE TECHNOLOGY ARCHIVES",
        "archive_text": "The Archives preserve knowledge about space exploration technology, complementing the Moon and Mars sections.",
        "mars_detail": "LEGACY ON MARS",
        "mars_text": "Mars has become the working ground for many robotic explorers. These machines help humanity study the terrain, climate and history of the Red Planet.",
        "footer": "SPACE HERITAGE · EXPLORING THE PAST · INSPIRING THE FUTURE"
    }
}

t = translations[st.session_state.language]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Roboto:wght@300;400;500;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 50% -15%, rgba(36, 91, 164, .48), transparent 48%),
        radial-gradient(ellipse at 12% 38%, rgba(27, 68, 125, .20), transparent 34%),
        radial-gradient(ellipse at 88% 72%, rgba(71, 39, 116, .16), transparent 36%),
        linear-gradient(180deg, #071326 0%, #050b18 48%, #02050c 100%);
    background-attachment: fixed;
    color: white;
    font-family: 'Roboto', sans-serif;
}

/* Animated deep-space background */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    opacity: .72;
    background-image:
        radial-gradient(1.5px 1.5px at 8% 17%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 18% 72%, #9bcaff 98%, transparent),
        radial-gradient(2px 2px at 31% 28%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 44% 83%, #c6ddff 98%, transparent),
        radial-gradient(1.5px 1.5px at 57% 13%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 69% 57%, #9bcaff 98%, transparent),
        radial-gradient(2px 2px at 82% 24%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 94% 76%, #c6ddff 98%, transparent),
        radial-gradient(1px 1px at 74% 91%, #ffffff 98%, transparent);
    background-size: 430px 360px;
    animation: star-drift 85s linear infinite, star-twinkle 5s ease-in-out infinite alternate;
}

.stApp::after {
    content: "";
    position: fixed;
    top: -15%;
    left: -30%;
    width: 190px;
    height: 2px;
    z-index: 0;
    pointer-events: none;
    opacity: 0;
    border-radius: 50%;
    background: linear-gradient(90deg, transparent, rgba(130, 195, 255, .95), #fff, transparent);
    box-shadow: 0 0 12px 2px rgba(92, 165, 255, .5);
    transform: rotate(-24deg);
    animation: shooting-star 13s ease-in-out infinite;
}

@keyframes star-drift {
    from { background-position: 0 0; }
    to { background-position: 430px 360px; }
}
@keyframes star-twinkle {
    from { opacity: .38; }
    to { opacity: .9; }
}
@keyframes shooting-star {
    0%, 72% { opacity: 0; transform: translate3d(0,0,0) rotate(-24deg); }
    74% { opacity: 1; }
    84% { opacity: .9; transform: translate3d(145vw,75vh,0) rotate(-24deg); }
    85%, 100% { opacity: 0; transform: translate3d(145vw,75vh,0) rotate(-24deg); }
}

/* Keep the app content above the animated background */
.stApp > header, .stApp [data-testid="stAppViewContainer"],
.stApp [data-testid="stMain"] {
    position: relative;
    z-index: 1;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.brand {
    font-family: 'Orbitron', sans-serif;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: 4px;
    color: white;
}

.top-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, #4d8dff, transparent);
    margin-top: 15px;
    margin-bottom: 65px;
}

.hero {
    text-align: center;
    padding: 30px 10px 65px;
    position: relative;
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(38px, 7vw, 75px);
    font-weight: 800;
    letter-spacing: 8px;
    color: white;
    text-shadow: 0 0 25px rgba(60, 145, 255, 0.65);
    margin-bottom: 15px;
}

.hero-subtitle {
    color: #65aaff;
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    letter-spacing: 3px;
    margin-bottom: 22px;
}

.hero-description {
    color: #aab8d0;
    font-size: 16px;
    max-width: 750px;
    line-height: 1.8;
    margin: auto;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 19px;
    letter-spacing: 3px;
    color: white;
    margin-bottom: 25px;
}

.card-link {
    display: block;
    text-decoration: none !important;
    color: white !important;
}

.explore-card {
    height: 420px;
    border: 1px solid rgba(100, 160, 255, 0.3);
    border-radius: 13px;
    overflow: hidden;
    background: linear-gradient(155deg, rgba(20, 39, 67, .94), rgba(7, 15, 30, .96));
    backdrop-filter: blur(8px);
    transition: all 0.35s ease;
    box-shadow: 0 12px 34px rgba(0, 0, 0, .22);
    cursor: pointer;
}

.explore-card:hover {
    transform: translateY(-9px) scale(1.012);
    border-color: #55a5ff;
    box-shadow: 0 10px 35px rgba(40, 130, 255, 0.25);
}

.card-image {
    width: 100%;
    height: 235px;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
}

.explore-card:hover .card-image {
    transform: scale(1.05);
}

.card-content {
    padding: 22px;
}

.card-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 2px;
    color: white;
    margin-bottom: 13px;
}

.card-description {
    color: #aab8d0;
    font-size: 13px;
    line-height: 1.7;
}

.detail-heading {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(25px, 4vw, 42px);
    color: white;
    letter-spacing: 3px;
    margin-top: 30px;
    margin-bottom: 20px;
}

.detail-text {
    color: #b8c7df;
    font-size: 16px;
    line-height: 1.9;
    max-width: 900px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 11px;
    letter-spacing: 2px;
    margin-top: 90px;
    padding-top: 25px;
    border-top: 1px solid rgba(100, 160, 255, 0.2);
}

.stButton > button {
    background: transparent;
    color: #8dbfff;
    border: 1px solid #397ac7;
    border-radius: 7px;
    padding: 8px 20px;
}

.stButton > button:hover {
    background: #17365d;
    border-color: #76b5ff;
    color: white;
}

div[data-testid="stSelectbox"] {
    max-width: 150px;
    margin-left: auto;
}
</style>
""", unsafe_allow_html=True)

header_left, header_right = st.columns([5, 1])

with header_left:
    st.markdown(
        f'<div class="brand">✦ SPACE LEGACY | {t["brand"]}</div>',
        unsafe_allow_html=True
    )

with header_right:
    language = st.selectbox(
        t["language"],
        ["VI", "EN"],
        index=0 if st.session_state.language == "VI" else 1,
        label_visibility="collapsed"
    )

    if language != st.session_state.language:
        st.session_state.language = language
        st.query_params["lang"] = language
        st.rerun()

st.markdown('<div class="top-line"></div>', unsafe_allow_html=True)

if st.session_state.page == "home":

    st.markdown(f"""
    <div class="hero">
        <div class="hero-title">SPACE LEGACY</div>
        <div class="hero-subtitle">{t["subtitle"]}</div>
        <div class="hero-description">{t["description"]}</div>
    </div>
    <div class="section-title">{t["section"]}</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(f"""
        <a class="card-link" href="?page=detail&selected=moon&lang={st.session_state.language}">
            <div class="explore-card">
                <img class="card-image" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=900">
                <div class="card-content">
                    <div class="card-title">{t["moon_title"]}</div>
                    <div class="card-description">{t["moon_desc"]}</div>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <a class="card-link" href="?page=detail&selected=archive&lang={st.session_state.language}">
            <div class="explore-card">
                <img class="card-image" src="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=900">
                <div class="card-content">
                    <div class="card-title">{t["archive_title"]}</div>
                    <div class="card-description">{t["archive_desc"]}</div>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <a class="card-link" href="?page=detail&selected=mars&lang={st.session_state.language}">
            <div class="explore-card">
                <img class="card-image" src="https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=900">
                <div class="card-content">
                    <div class="card-title">{t["mars_title"]}</div>
                    <div class="card-description">{t["mars_desc"]}</div>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

    # TRAINING MODE - placed below the three exploration cards and above the footer
    st.markdown("""
    <style>
    .training-home {
        margin-top: 58px;
        padding: 28px 24px;
        border: 1px solid rgba(91, 164, 255, .42);
        border-radius: 16px;
        background: linear-gradient(120deg, rgba(18, 42, 76, .92), rgba(5, 12, 27, .96));
        box-shadow: 0 0 28px rgba(48, 128, 230, .12);
        text-align: center;
    }
    .training-home-kicker {
        color: #75baff;
        font-family: 'Orbitron', sans-serif;
        font-size: 11px;
        letter-spacing: 4px;
        margin-bottom: 9px;
    }
    .training-home-title {
        color: #f4f8ff;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(24px, 4vw, 36px);
        font-weight: 800;
        letter-spacing: 3px;
        text-shadow: 0 0 18px rgba(78, 158, 255, .45);
    }
    .training-home-desc {
        color: #aabbd4;
        font-size: 14px;
        line-height: 1.8;
        margin: 10px auto 18px;
        max-width: 720px;
    }
    </style>
    """, unsafe_allow_html=True)

    training_title = "TRUNG TÂM HUẤN LUYỆN" if st.session_state.language == "VI" else "TRAINING CENTER"
    training_desc = (
        "Thử thách trí nhớ với robot thám hiểm và tư duy chiến thuật qua các nhiệm vụ mô phỏng."
        if st.session_state.language == "VI"
        else "Test your rover knowledge and tactical thinking through quick mission simulations."
    )
    training_button = "⚡ BẮT ĐẦU HUẤN LUYỆN" if st.session_state.language == "VI" else "⚡ ENTER TRAINING MODE"

    st.markdown(f"""
    <div class="training-home">
        <div class="training-home-kicker">SPACE LEGACY · SPECIAL MISSION</div>
        <div class="training-home-title">{training_title}</div>
        <div class="training-home-desc">{training_desc}</div>
    </div>
    """, unsafe_allow_html=True)

    _, training_col, _ = st.columns([1, 1.5, 1])
    with training_col:
        if st.button(training_button, key="open_training_mode", use_container_width=True):
            st.session_state.page = "training"
            st.rerun()

    st.markdown(
        f'<div class="footer">{t["footer"]}</div>',
        unsafe_allow_html=True
    )

elif st.session_state.page == "detail":

    if st.button(t["back"]):
        st.query_params.clear()
        st.session_state.page = "home"
        st.session_state.selected = ""
        st.rerun()

    selected = st.session_state.selected

    if selected == "moon":
        st.markdown(f"""
        <div class="detail-heading">{t["moon_detail"]}</div>
        <div class="detail-text">{t["moon_text"]}</div>
        """, unsafe_allow_html=True)

        show_moon_timeline(st.session_state.language)

    elif selected == "archive":
        st.markdown(f"""
        <div class="detail-heading">{t["archive_detail"]}</div>
        <div class="detail-text">{t["archive_text"]}</div>
        """, unsafe_allow_html=True)

        show_archive_timeline(st.session_state.language)

    elif selected == "mars":
        st.markdown(f"""
        <div class="detail-heading">{t["mars_detail"]}</div>
        <div class="detail-text">{t["mars_text"]}</div>
        """, unsafe_allow_html=True)
        
        show_mars_timeline(st.session_state.language)
    
    else:
        st.session_state.page = "home"
        st.rerun()

    st.markdown(
        f'<div class="footer">{t["footer"]}</div>',
        unsafe_allow_html=True
    )

elif st.session_state.page == "training":
    show_training_game(st.session_state.language)
