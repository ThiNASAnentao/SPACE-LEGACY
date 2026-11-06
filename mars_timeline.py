import streamlit as st
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

MISSIONS = [
    {
        "id": "sojourner",
        "year": 1997,
        "name": "Sojourner",
        "image": "PIA01122",
        "type": "Mars Pathfinder rover",
        "vi_mission": "Robot tự hành đầu tiên hoạt động thành công trên Sao Hỏa. Nhiệm vụ thuộc chương trình Mars Pathfinder của NASA.",
        "en_mission": "The first successful rover to operate on Mars. It was part of NASA's Mars Pathfinder mission.",
        "vi_discovery": "Khảo sát đá và đất Sao Hỏa, cung cấp dữ liệu về thành phần và đặc điểm địa chất của bề mặt hành tinh.",
        "en_discovery": "Studied Martian rocks and soil, providing data about the composition and geology of the surface.",
        "vi_fate": "Nhiệm vụ kết thúc sau khi liên lạc bị mất vào tháng 9 năm 1997.",
        "en_fate": "The mission ended after contact was lost in September 1997.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/mars-pathfinder/"
    },
    {
        "id": "spirit",
        "year": 2004,
        "name": "Spirit",
        "image": "PIA04983",
        "type": "Mars Exploration Rover",
        "vi_mission": "Khám phá địa chất Sao Hỏa và tìm kiếm bằng chứng về sự tồn tại của nước trong quá khứ.",
        "en_mission": "Explored Martian geology and searched for evidence of past water.",
        "vi_discovery": "Tìm thấy nhiều bằng chứng về môi trường cổ đại có sự tham gia của nước.",
        "en_discovery": "Found evidence of ancient environments shaped by water.",
        "vi_fate": "NASA mất liên lạc với Spirit vào năm 2010 sau khi robot bị mắc kẹt trong cát.",
        "en_fate": "NASA lost contact with Spirit in 2010 after the rover became stuck in sand.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/mer-spirit/"
    },
    {
        "id": "opportunity",
        "year": 2004,
        "name": "Opportunity",
        "image": "PIA05578",
        "type": "Mars Exploration Rover",
        "vi_mission": "Nghiên cứu đá, đất và lịch sử nước trên Sao Hỏa.",
        "en_mission": "Studied rocks, soil, and the history of water on Mars.",
        "vi_discovery": "Phát hiện bằng chứng cho thấy nước lỏng từng tồn tại trên bề mặt Sao Hỏa.",
        "en_discovery": "Found evidence that liquid water once existed on the Martian surface.",
        "vi_fate": "NASA tuyên bố kết thúc nhiệm vụ vào tháng 2 năm 2019 sau khi không thể khôi phục liên lạc.",
        "en_fate": "NASA declared the mission complete in February 2019 after contact could not be restored.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/mer-opportunity/"
    },
    {
        "id": "phoenix",
        "year": 2008,
        "name": "Phoenix",
        "image": "PIA11068",
        "type": "Mars Lander",
        "vi_mission": "Tàu đổ bộ nghiên cứu vùng cực Bắc Sao Hỏa, tìm hiểu môi trường và khả năng tồn tại của nước.",
        "en_mission": "A lander that studied the Martian northern polar region and investigated water-related conditions.",
        "vi_discovery": "Xác nhận sự tồn tại của băng nước trong lớp đất bên dưới bề mặt Sao Hỏa.",
        "en_discovery": "Confirmed the presence of water ice beneath the Martian surface.",
        "vi_fate": "Nhiệm vụ kết thúc sau khi tàu không thể tiếp tục hoạt động trong mùa đông Sao Hỏa.",
        "en_fate": "The mission ended after the lander could no longer operate through the Martian winter.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/phoenix/"
    },
    {
        "id": "curiosity",
        "year": 2012,
        "name": "Curiosity",
        "image": "PIA16064",
        "type": "Mars Science Laboratory rover",
        "vi_mission": "Nghiên cứu xem môi trường cổ đại trên Sao Hỏa có từng phù hợp cho sự sống vi sinh vật hay không.",
        "en_mission": "Investigates whether ancient environments on Mars could have supported microbial life.",
        "vi_discovery": "Tìm thấy bằng chứng về môi trường cổ đại từng có nước lỏng và các thành phần hóa học quan trọng.",
        "en_discovery": "Found evidence of ancient environments with liquid water and important chemical ingredients.",
        "vi_fate": "Tiếp tục khám phá miệng núi lửa Gale trên Sao Hỏa.",
        "en_fate": "Continues exploring Gale Crater on Mars.",
        "status_vi": "ĐANG HOẠT ĐỘNG",
        "status_en": "ACTIVE MISSION",
        "status": "active",
        "source": "https://science.nasa.gov/mission/msl-curiosity/"
    },
    {
        "id": "insight",
        "year": 2018,
        "name": "InSight",
        "image": "PIA22876",
        "type": "Mars Lander",
        "vi_mission": "Nghiên cứu cấu trúc bên trong Sao Hỏa và đo hoạt động địa chấn của hành tinh.",
        "en_mission": "Studied the interior structure of Mars and measured its seismic activity.",
        "vi_discovery": "Ghi nhận các trận động đất Sao Hỏa và cung cấp dữ liệu về lớp vỏ, lớp phủ và lõi hành tinh.",
        "en_discovery": "Recorded marsquakes and provided data about the crust, mantle, and core.",
        "vi_fate": "NASA kết thúc nhiệm vụ vào tháng 12 năm 2022 sau khi bụi làm giảm khả năng cung cấp năng lượng.",
        "en_fate": "NASA ended the mission in December 2022 after dust reduced the lander's power supply.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/insight/"
    },
    {
        "id": "perseverance",
        "year": 2021,
        "name": "Perseverance",
        "image": "PIA24342",
        "type": "Mars 2020 rover",
        "vi_mission": "Tìm kiếm dấu hiệu sự sống vi sinh vật cổ đại, nghiên cứu địa chất và thu thập mẫu vật Sao Hỏa.",
        "en_mission": "Searches for signs of ancient microbial life, studies geology, and collects Martian samples.",
        "vi_discovery": "Thu thập mẫu đá và đất tại miệng núi lửa Jezero để phục vụ nghiên cứu khoa học.",
        "en_discovery": "Collects rock and soil samples at Jezero Crater for scientific research.",
        "vi_fate": "Tiếp tục thực hiện nhiệm vụ khám phá và nghiên cứu trên Sao Hỏa.",
        "en_fate": "Continues its exploration and scientific research on Mars.",
        "status_vi": "ĐANG HOẠT ĐỘNG",
        "status_en": "ACTIVE MISSION",
        "status": "active",
        "source": "https://science.nasa.gov/mission/mars-2020-perseverance/"
    },
    {
        "id": "ingenuity",
        "year": 2021,
        "name": "Ingenuity",
        "image": "PIA24642",
        "type": "Mars Helicopter Technology Demonstrator",
        "vi_mission": "Trực thăng công nghệ thử nghiệm khả năng bay có điều khiển trong bầu khí quyển Sao Hỏa.",
        "en_mission": "A technology demonstrator that tested powered, controlled flight in the Martian atmosphere.",
        "vi_discovery": "Chứng minh khả năng thực hiện chuyến bay có động cơ trên một hành tinh khác.",
        "en_discovery": "Demonstrated powered flight on another planet.",
        "vi_fate": "NASA kết thúc nhiệm vụ vào tháng 1 năm 2024 sau khi trực thăng bị hư hại cánh quạt.",
        "en_fate": "NASA ended the mission in January 2024 after rotor damage.",
        "status_vi": "ĐÃ KẾT THÚC",
        "status_en": "MISSION ENDED",
        "status": "ended",
        "source": "https://science.nasa.gov/mission/ingenuity/"
    }
]


@st.cache_data(ttl=86400, show_spinner=False)
def nasa_image(image_id):
    """Lấy URL ảnh từ NASA Image and Video Library; có URL dự phòng."""
    api_url = f"https://images-api.nasa.gov/asset/{image_id}"
    request = Request(api_url, headers={"User-Agent": "SPACE-LEGACY/1.0"})

    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))

        items = payload.get("collection", {}).get("items", [])
        candidates = [item.get("href", "") for item in items]

        # Ưu tiên ảnh JPEG; loại bỏ video, thumbnail và tệp không phải ảnh.
        image_files = [
            url for url in candidates
            if url.lower().split("?")[0].endswith((".jpg", ".jpeg", ".png"))
        ]
        if image_files:
            # Ưu tiên bản medium nếu NASA cung cấp, nếu không dùng ảnh đầu tiên.
            for url in image_files:
                if "~medium" in url.lower() or "~large" in url.lower():
                    return url
            return image_files[0]
    except (URLError, HTTPError, TimeoutError, ValueError, KeyError, TypeError):
        pass

    # Dự phòng khi API tạm thời không truy cập được.
    return f"https://images-assets.nasa.gov/image/{image_id}/{image_id}~medium.jpg"


def mars_css():
    st.markdown("""
    <style>
    /* Typography: clean, readable, and comfortable for Vietnamese text. */
    .mars-title, .mars-subtitle, .section-heading,
    .mission-name, .mission-year, .window-tag, .window-title,
    .window-year, .window-label, .window-text, .window-status,
    .window-source, .mars-caption {
        font-family: "Segoe UI", Arial, sans-serif;
        text-transform: none;
        letter-spacing: normal;
    }

    .mars-title {
        text-align: center;
        font-size: clamp(30px, 4vw, 42px);
        font-weight: 800;
        color: #ffb184;
        text-shadow: 0 3px 24px rgba(255, 111, 60, 0.28);
        margin: 12px 0 8px;
        line-height: 1.2;
    }

    .mars-subtitle {
        text-align: center;
        color: #c8b8b1;
        font-size: 14px;
        line-height: 1.6;
        margin: 0 0 26px;
    }

    .mars-stage {
        position: relative;
        width: 100%;
        height: 390px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border-radius: 20px;
        background: radial-gradient(ellipse at center, #32160f 0%, #160e12 48%, #080b14 100%);
        border: 1px solid rgba(255, 139, 91, 0.2);
    }

    .mars-orbit {
        position: absolute;
        width: 340px;
        height: 340px;
        border: 1px solid rgba(255, 160, 110, 0.25);
        border-radius: 50%;
    }

    .mars-orbit-two {
        position: absolute;
        width: 430px;
        height: 240px;
        border: 1px solid rgba(255, 160, 110, 0.15);
        border-radius: 50%;
        transform: rotate(-25deg);
    }

    .mars-planet {
        position: relative;
        width: 245px;
        height: 245px;
        border-radius: 50%;
        background-image: linear-gradient(100deg, rgba(0,0,0,0.85), rgba(0,0,0,0.08)),
            url("https://photojournal.jpl.nasa.gov/jpeg/PIA00407.jpg");
        background-size: cover;
        background-position: center;
        box-shadow: inset -35px -15px 55px rgba(0,0,0,0.9), 0 0 35px rgba(255,95,45,0.35);
        animation: mars-float 6s ease-in-out infinite;
        z-index: 2;
    }

    @keyframes mars-float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    .mars-caption {
        position: absolute;
        bottom: 18px;
        color: #d4bdb2;
        font-size: 12px;
        font-weight: 600;
    }

    .mission-card {
        background: linear-gradient(145deg, rgba(75, 37, 27, 0.65), rgba(15, 19, 30, 0.85));
        border: 1px solid rgba(255, 147, 100, 0.22);
        border-radius: 14px;
        padding: 10px;
        text-align: center;
        transition: all 0.25s ease;
    }

    .mission-card:hover {
        transform: translateY(-5px);
        border-color: #ff9b67;
        box-shadow: 0 0 22px rgba(255, 111, 60, 0.25);
    }

    .mission-image-wrap {
        position: relative;
        height: 130px;
        overflow: hidden;
        border-radius: 9px;
        background: radial-gradient(circle, #63301e, #17121a);
    }

    .mission-image-wrap img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    /* The rover image itself is a real Streamlit button. */
    .mission-image-button button {
        height: 142px !important;
        min-height: 142px !important;
        padding: 0 !important;
        border-radius: 10px !important;
        border: 1px solid rgba(103, 232, 249, 0.28) !important;
        background-color: rgba(8, 15, 28, 0.9) !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-size: contain !important;
        color: transparent !important;
        font-size: 0 !important;
        transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease !important;
    }

    .mission-image-button button:hover {
        transform: translateY(-4px) scale(1.015) !important;
        border-color: #67e8f9 !important;
        box-shadow: 0 0 22px rgba(103, 232, 249, .28) !important;
    }

    .mission-name {
        color: #fff0e7;
        font-weight: 700;
        font-size: 16px;
        margin-top: 10px;
        line-height: 1.35;
    }

    .mission-year {
        color: #ffb184;
        font-size: 13px;
        margin-top: 4px;
    }

    .section-heading {
        color: #ffd0b5;
        font-size: 23px;
        font-weight: 750;
        margin: 30px 0 14px;
        line-height: 1.35;
    }

    .timeline-line {
        height: 3px;
        background: linear-gradient(90deg, transparent, #a94f31, #ffad7b, #a94f31, transparent);
        margin: 22px 0;
        border-radius: 5px;
    }

    .mission-status-active, .mission-status-ended {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.4px;
    }

    .mission-status-active { color: #9cffb5; }
    .mission-status-ended { color: #ffc09d; }

    div.stButton > button {
        border: 1px solid rgba(255, 147, 100, 0.45);
        background: rgba(70, 32, 25, 0.7);
        color: #ffe0ce;
        border-radius: 9px;
        transition: all 0.2s ease;
        font-weight: 650;
    }

    div.stButton > button:hover {
        border-color: #ff9b67;
        background: rgba(130, 55, 32, 0.8);
        color: white;
        box-shadow: 0 0 15px rgba(255, 111, 60, 0.25);
    }

    .window-tag {
        color: #ffad7b;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .window-title {
        color: #fff0e7;
        font-size: clamp(30px, 4vw, 42px);
        font-weight: 800;
        line-height: 1.15;
    }

    .window-year {
        color: #ffb184;
        font-size: 16px;
        font-weight: 650;
        margin: 8px 0 14px;
    }

    .window-status {
        display: inline-block;
        padding: 7px 12px;
        margin-bottom: 16px;
        border-radius: 30px;
        color: #aaffbd;
        border: 1px solid rgba(90, 255, 130, 0.4);
        background: rgba(20, 100, 50, 0.2);
        font-size: 11px;
        font-weight: 700;
    }

    .window-info-card {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 173, 123, 0.16);
        border-radius: 12px;
        padding: 14px 16px;
        margin: 12px 0;
    }

    .window-label {
        color: #ffb184;
        font-size: 15px;
        font-weight: 750;
        margin: 0 0 7px;
        line-height: 1.4;
    }

    .window-text {
        color: #eee4df;
        font-size: 15px;
        font-weight: 400;
        line-height: 1.75;
        overflow-wrap: anywhere;
    }

    .window-source {
        display: inline-block;
        margin-top: 16px;
        color: #ffbd98 !important;
        text-decoration: none !important;
        border-bottom: 1px solid rgba(255, 173, 123, 0.5);
        font-size: 13px;
        font-weight: 650;
    }

    /* Chữ đậm và sáng hơn để dễ đọc trên nền tối. */
    .mars-title {
        color: #ffd0ad !important;
        font-weight: 900 !important;
        text-shadow: 0 2px 5px rgba(0,0,0,.85), 0 0 24px rgba(255,125,70,.55) !important;
    }

    .mars-subtitle {
        color: #fff0e7 !important;
        font-weight: 700 !important;
        text-shadow: 0 1px 4px rgba(0,0,0,.9);
    }

    .section-heading {
        color: #ffe0ca !important;
        font-weight: 900 !important;
        text-shadow: 0 2px 8px rgba(0,0,0,.8), 0 0 12px rgba(255,135,82,.25);
    }

    .mission-name {
        color: #ffffff !important;
        font-weight: 850 !important;
        text-shadow: 0 1px 5px rgba(0,0,0,.9);
    }

    .mission-year {
        color: #ffd0ad !important;
        font-weight: 800 !important;
    }

    .mission-status-active, .mission-status-ended {
        font-weight: 850 !important;
        text-shadow: 0 1px 4px rgba(0,0,0,.9);
    }

    .window-tag, .window-label {
        color: #ffd0ad !important;
        font-weight: 900 !important;
        text-shadow: 0 1px 4px rgba(0,0,0,.85);
    }

    .window-title {
        color: #ffffff !important;
        font-weight: 900 !important;
        text-shadow: 0 2px 12px rgba(0,0,0,.9), 0 0 18px rgba(255,130,75,.3);
    }

    .window-year, .window-source {
        color: #ffd0ad !important;
        font-weight: 800 !important;
    }

    .window-text {
        color: #ffffff !important;
        font-weight: 600 !important;
        line-height: 1.85 !important;
        text-shadow: 0 1px 2px rgba(0,0,0,.65);
    }

    .mars-caption {
        color: #ffffff !important;
        font-weight: 800 !important;
        text-shadow: 0 2px 5px #000;
    }

    /* Bảng màu mới: xanh cyan và tím sáng, tương phản rõ với nền tối. */
    .mars-title { color: #67e8f9 !important; text-shadow: 0 2px 8px #06121d, 0 0 24px rgba(34,211,238,.45) !important; }
    .mars-subtitle { color: #e0f2fe !important; }
    .section-heading { color: #a5f3fc !important; text-shadow: 0 2px 8px #06121d, 0 0 14px rgba(34,211,238,.3) !important; }
    .mission-name { color: #f5f3ff !important; }
    .mission-year, .window-year { color: #c4b5fd !important; }
    .mission-status-active { color: #86efac !important; }
    .mission-status-ended { color: #fda4af !important; }
    .window-tag, .window-label { color: #67e8f9 !important; }
    .window-title { color: #f0f9ff !important; text-shadow: 0 2px 12px #020617, 0 0 18px rgba(34,211,238,.25) !important; }
    .window-text { color: #f1f5f9 !important; }
    .window-source { color: #a5f3fc !important; }
    .mars-caption { color: #e0f2fe !important; }

    /* Hiệu ứng chữ xuất hiện: mờ dần, trượt nhẹ từ dưới lên. */
    @keyframes text-appear {
        from {
            opacity: 0;
            transform: translateY(18px);
            filter: blur(4px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
            filter: blur(0);
        }
    }

    @keyframes card-appear {
        from {
            opacity: 0;
            transform: translateY(24px) scale(.97);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    .mars-title {
        animation: text-appear .85s cubic-bezier(.2,.75,.25,1) both;
    }

    .mars-subtitle {
        animation: text-appear .85s .15s cubic-bezier(.2,.75,.25,1) both;
    }

    .mars-caption {
        animation: text-appear .8s .45s ease-out both;
    }

    .section-heading {
        animation: text-appear .8s .2s ease-out both;
    }

    .mission-card {
        animation: card-appear .7s cubic-bezier(.2,.75,.25,1) both;
    }

    .mission-name, .mission-year,
    .mission-status-active, .mission-status-ended {
        animation: text-appear .65s .18s ease-out both;
    }

    .window-tag, .window-title, .window-year, .window-status,
    .window-label, .window-text, .window-source {
        animation: text-appear .7s ease-out both;
    }

    .window-info-card:nth-of-type(1) { animation-delay: .12s; }
    .window-info-card:nth-of-type(2) { animation-delay: .24s; }
    .window-info-card:nth-of-type(3) { animation-delay: .36s; }

    @media (prefers-reduced-motion: reduce) {
        .mars-title, .mars-subtitle, .mars-caption, .section-heading,
        .mission-card, .mission-name, .mission-year,
        .mission-status-active, .mission-status-ended,
        .window-tag, .window-title, .window-year, .window-status,
        .window-label, .window-text, .window-source {
            animation: none !important;
        }
    }

    @media (max-width: 700px) {
        .mars-stage { height: 300px; }
        .mars-planet { width: 190px; height: 190px; }
        .window-title { font-size: 30px; }
        .window-info-card { padding: 12px; }
    }
    </style>
    """, unsafe_allow_html=True)

def clear_selected_mission():
    st.session_state.pop("selected_mars_mission", None)


@st.dialog(
    "NASA MISSION ARCHIVE",
    width="large",
    on_dismiss=clear_selected_mission
)
def show_mission_window(mission, language):
    vi = language == "vi"
    explored = set(st.session_state.get("mars_explored_missions", []))
    explored.add(mission["id"])
    st.session_state["mars_explored_missions"] = sorted(explored)

    mission_text = mission["vi_mission"] if vi else mission["en_mission"]
    discovery_text = mission["vi_discovery"] if vi else mission["en_discovery"]
    fate_text = mission["vi_fate"] if vi else mission["en_fate"]
    status = mission["status_vi"] if vi else mission["status_en"]

    labels = {
        "mission": "NHIỆM VỤ" if vi else "MISSION",
        "discovery": "NHỮNG KHÁM PHÁ" if vi else "DISCOVERIES",
        "fate": "SỐ PHẬN NHIỆM VỤ" if vi else "MISSION STATUS",
        "type": "LOẠI PHƯƠNG TIỆN" if vi else "VEHICLE TYPE",
        "archive": "HỒ SƠ NHIỆM VỤ NASA" if vi else "NASA MISSION ARCHIVE"
    }

    st.markdown(
        f'<div class="window-tag">{labels["archive"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="window-title">{mission["name"]}</div>'
        f'<div class="window-year">MARS EXPLORATION · {mission["year"]}</div>'
        f'<div class="window-status">● {status}</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1, 1])

    with left:
        st.image(
            nasa_image(mission["image"]),
            use_container_width=True
        )

        st.caption(f'{labels["type"]}: {mission["type"]}')

    with right:
        st.markdown(
            f'<div class="window-info-card"><div class="window-label">{labels["mission"]}</div>'
            f'<div class="window-text">{mission_text}</div></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="window-info-card"><div class="window-label">{labels["discovery"]}</div>'
            f'<div class="window-text">{discovery_text}</div></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="window-info-card"><div class="window-label">{labels["fate"]}</div>'
            f'<div class="window-text">{fate_text}</div></div>',
            unsafe_allow_html=True
        )

        link_text = (
            "XEM NGUỒN NASA CHÍNH THỨC ↗"
            if vi else "VIEW OFFICIAL NASA SOURCE ↗"
        )

        st.markdown(
            f'<a class="window-source" href="{mission["source"]}" '
            f'target="_blank">{link_text}</a>',
            unsafe_allow_html=True
        )

    st.divider()

    close_text = "ĐÓNG HỒ SƠ" if vi else "CLOSE ARCHIVE"

    if st.button(close_text, key=f"close_{mission['id']}", use_container_width=True):
        clear_selected_mission()
        st.rerun()


def show_mission_card(mission, language):
    image_url = nasa_image(mission["image"])

    # Tạo nút có ảnh nền: người dùng bấm trực tiếp vào hình để mở hồ sơ.
    button_key = f"open_{mission['id']}"
    st.markdown(
        f"""
        <style>
        .st-key-{button_key} button {{
            height: 142px !important;
            min-height: 142px !important;
            padding: 0 !important;
            border-radius: 10px !important;
            border: 1px solid rgba(103, 232, 249, 0.28) !important;
            background-color: rgba(8, 15, 28, 0.9) !important;
            background-image: url('{image_url}') !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-size: contain !important;
            color: transparent !important;
            font-size: 0 !important;
            transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease !important;
        }}
        .st-key-{button_key} button:hover {{
            transform: translateY(-4px) scale(1.015) !important;
            border-color: #67e8f9 !important;
            box-shadow: 0 0 22px rgba(103, 232, 249, .28) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    clicked = st.button(
        " ",
        key=button_key,
        help=(f"Mở hồ sơ {mission['name']}" if language == "vi" else f"Open {mission['name']} mission profile"),
        use_container_width=True
    )
    st.markdown(
        f'<div class="mission-name">{mission["name"]}</div>'
        f'<div class="mission-year">{mission["year"]}</div>',
        unsafe_allow_html=True
    )

    if mission["status"] == "active":
        status_class = "mission-status-active"
    else:
        status_class = "mission-status-ended"

    status_text = (
        mission["status_vi"] if language == "vi"
        else mission["status_en"]
    )

    st.markdown(
        f'<div class="{status_class}" style="text-align:center; margin:8px 0;">'
        f'{status_text}</div>',
        unsafe_allow_html=True
    )

    if clicked:
        st.session_state["selected_mars_mission"] = mission["id"]
        st.rerun()


QUIZ_QUESTIONS = [
    {
        "question_vi": "Robot tự hành nào là robot đầu tiên hoạt động thành công trên Sao Hỏa?",
        "question_en": "Which rover was the first to successfully operate on Mars?",
        "options_vi": ["Sojourner", "Curiosity", "Spirit", "Perseverance"],
        "options_en": ["Sojourner", "Curiosity", "Spirit", "Perseverance"],
        "answer": 0,
        "explain_vi": "Sojourner hoạt động trên Sao Hỏa trong sứ mệnh Mars Pathfinder năm 1997.",
        "explain_en": "Sojourner operated on Mars during the 1997 Mars Pathfinder mission."
    },
    {
        "question_vi": "Spirit và Opportunity được phóng lên Sao Hỏa vào năm nào?",
        "question_en": "In which year did Spirit and Opportunity arrive at Mars?",
        "options_vi": ["1997", "2004", "2008", "2012"],
        "options_en": ["1997", "2004", "2008", "2012"],
        "answer": 1,
        "explain_vi": "Spirit và Opportunity cùng bắt đầu nhiệm vụ trên Sao Hỏa vào năm 2004.",
        "explain_en": "Spirit and Opportunity both began their Mars missions in 2004."
    },
    {
        "question_vi": "Tàu đổ bộ Phoenix xác nhận điều gì bên dưới bề mặt Sao Hỏa?",
        "question_en": "What did the Phoenix lander confirm beneath the Martian surface?",
        "options_vi": ["Dầu mỏ", "Băng nước", "Rừng cây", "Đại dương hiện tại"],
        "options_en": ["Petroleum", "Water ice", "Forests", "A present-day ocean"],
        "answer": 1,
        "explain_vi": "Phoenix xác nhận sự tồn tại của băng nước trong lớp đất bên dưới bề mặt.",
        "explain_en": "Phoenix confirmed water ice beneath the surface soil."
    },
    {
        "question_vi": "Curiosity đang khám phá khu vực nào trên Sao Hỏa?",
        "question_en": "Which area of Mars is Curiosity exploring?",
        "options_vi": ["Miệng núi lửa Gale", "Miệng núi lửa Jezero", "Vùng cực Bắc", "Thung lũng Mariner"],
        "options_en": ["Gale Crater", "Jezero Crater", "The North Pole", "Valles Marineris"],
        "answer": 0,
        "explain_vi": "Curiosity tiếp tục khám phá miệng núi lửa Gale.",
        "explain_en": "Curiosity continues to explore Gale Crater."
    },
    {
        "question_vi": "InSight tập trung nghiên cứu điều gì?",
        "question_en": "What was InSight designed to study?",
        "options_vi": ["Khí hậu Trái Đất", "Cấu trúc bên trong Sao Hỏa", "Vành đai Sao Thổ", "Các vệ tinh của Sao Hỏa"],
        "options_en": ["Earth's climate", "Mars's interior structure", "Saturn's rings", "Mars's moons"],
        "answer": 1,
        "explain_vi": "InSight nghiên cứu cấu trúc bên trong và ghi nhận các trận động đất Sao Hỏa.",
        "explain_en": "InSight studied Mars's interior and recorded marsquakes."
    },
    {
        "question_vi": "Perseverance thu thập mẫu vật tại miệng núi lửa nào?",
        "question_en": "At which crater does Perseverance collect samples?",
        "options_vi": ["Gale", "Jezero", "Endeavour", "Gusev"],
        "options_en": ["Gale", "Jezero", "Endeavour", "Gusev"],
        "answer": 1,
        "explain_vi": "Perseverance thu thập mẫu đá và đất tại miệng núi lửa Jezero.",
        "explain_en": "Perseverance collects rock and soil samples at Jezero Crater."
    },
    {
        "question_vi": "Ingenuity là phương tiện thuộc loại nào?",
        "question_en": "What type of vehicle was Ingenuity?",
        "options_vi": ["Tàu quỹ đạo", "Tàu đổ bộ", "Trực thăng", "Xe tự hành bánh xích"],
        "options_en": ["Orbiter", "Lander", "Helicopter", "Tracked rover"],
        "answer": 2,
        "explain_vi": "Ingenuity là trực thăng công nghệ thử nghiệm chuyến bay có động cơ trên Sao Hỏa.",
        "explain_en": "Ingenuity was a technology demonstrator for powered flight on Mars."
    },
    {
        "question_vi": "NASA tuyên bố kết thúc nhiệm vụ Opportunity vào năm nào?",
        "question_en": "In which year did NASA declare the Opportunity mission complete?",
        "options_vi": ["2010", "2012", "2019", "2024"],
        "options_en": ["2010", "2012", "2019", "2024"],
        "answer": 2,
        "explain_vi": "NASA tuyên bố kết thúc nhiệm vụ Opportunity vào tháng 2 năm 2019.",
        "explain_en": "NASA declared Opportunity's mission complete in February 2019."
    }
]


def show_mars_quiz(language):
    vi = language == "vi"
    explored = set(st.session_state.get("mars_explored_missions", []))
    total = len(MISSIONS)
    done = len(explored.intersection(mission["id"] for mission in MISSIONS))

    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    heading = "Thử thách kiến thức Sao Hỏa" if vi else "Mars knowledge challenge"
    st.markdown(f'<div class="section-heading">🧠 {heading}</div>', unsafe_allow_html=True)

    if done < total:
        message = (
            f"Hãy mở hồ sơ và khám phá đủ {total} nhiệm vụ để mở khóa bài quiz."
            if vi else f"Open and explore all {total} mission profiles to unlock the quiz."
        )
        st.info(message)
        st.progress(done / total, text=(f"Đã khám phá {done}/{total} nhiệm vụ" if vi else f"Explored {done}/{total} missions"))
        return

    intro = (
        "Bạn đã khám phá toàn bộ 8 nhiệm vụ! Hãy thử xem mình nhớ được bao nhiêu nhé."
        if vi else "You explored all 8 missions! Test how much you remember."
    )
    st.success(intro)

    if st.session_state.get("mars_quiz_submitted", False):
        score = st.session_state.get("mars_quiz_score", 0)
        total_questions = len(QUIZ_QUESTIONS)
        st.markdown(f"### {'Kết quả của bạn' if vi else 'Your result'}: **{score}/{total_questions}**")
        st.progress(score / total_questions)
        if score == total_questions:
            st.balloons()
            st.success("Xuất sắc! Bạn đã trở thành chuyên gia Sao Hỏa!" if vi else "Perfect! You are a Mars exploration expert!")
        elif score >= 5:
            st.success("Rất tốt! Bạn đã nắm được nhiều kiến thức." if vi else "Great work! You know a lot about Mars missions.")
        else:
            st.info("Hãy xem lại các hồ sơ nhiệm vụ rồi thử lại nhé." if vi else "Review the mission profiles and give it another try.")

        with st.expander("Xem đáp án và giải thích" if vi else "Review answers and explanations"):
            for i, question in enumerate(QUIZ_QUESTIONS):
                options = question["options_vi"] if vi else question["options_en"]
                qtext = question["question_vi"] if vi else question["question_en"]
                explanation = question["explain_vi"] if vi else question["explain_en"]
                st.markdown(f"**{i + 1}. {qtext}**")
                st.write(("Đáp án: " if vi else "Answer: ") + options[question["answer"]])
                st.caption(explanation)

        if st.button("Làm lại quiz" if vi else "Try the quiz again", key="mars_quiz_retry", use_container_width=True):
            st.session_state["mars_quiz_submitted"] = False
            st.session_state.pop("mars_quiz_score", None)
            st.rerun()
        return

    with st.form("mars_quiz_form"):
        answers = []
        for i, question in enumerate(QUIZ_QUESTIONS):
            qtext = question["question_vi"] if vi else question["question_en"]
            options = question["options_vi"] if vi else question["options_en"]
            st.markdown(f"**Câu {i + 1}. {qtext}**" if vi else f"**Question {i + 1}. {qtext}**")
            choice = st.radio(
                "Chọn một đáp án" if vi else "Choose one answer",
                options,
                index=None,
                key=f"mars_quiz_answer_{i}",
                label_visibility="collapsed"
            )
            answers.append((choice, options))

        submitted = st.form_submit_button(
            "NỘP BÀI" if vi else "SUBMIT QUIZ",
            use_container_width=True
        )

    if submitted:
        if any(choice is None for choice, _ in answers):
            st.warning("Bạn hãy trả lời tất cả câu hỏi trước khi nộp nhé." if vi else "Please answer every question before submitting.")
        else:
            score = sum(
                choice == options[question["answer"]]
                for question, (choice, options) in zip(QUIZ_QUESTIONS, answers)
            )
            st.session_state["mars_quiz_score"] = score
            st.session_state["mars_quiz_submitted"] = True
            st.rerun()


def show_mars_credits(language):
    """Credit cuối trang Sao Hỏa."""
    vi = language == "vi"
    st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
    heading = "Ghi công & nguồn tham khảo" if vi else "Credits & references"
    st.markdown(
        f'<div class="section-heading">✦ {heading}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    .mars-credit-panel {
        padding: 22px 24px;
        border: 1px solid rgba(105, 220, 255, .42);
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(15, 35, 66, .94), rgba(35, 25, 70, .88));
        box-shadow: 0 8px 30px rgba(20, 120, 190, .12);
        animation: marsCreditIn .8s ease both;
    }
    .mars-credit-title {
        color: #ffffff;
        font-size: 17px;
        font-weight: 850;
        margin: 0 0 5px 0;
    }
    .mars-credit-value {
        color: #d9f5ff;
        font-size: 15px;
        font-weight: 600;
        line-height: 1.7;
        margin-bottom: 15px;
    }
    .mars-credit-value a { color: #70dcff !important; font-weight: 750; }
    @keyframes marsCreditIn {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    person_label = "Người thực hiện" if vi else "Created by"
    project_label = "Nhóm / dự án" if vi else "Project team"
    data_label = "Nguồn dữ liệu" if vi else "Data sources"
    image_label = "Nguồn hình ảnh" if vi else "Image sources"
    nasa_data = '<a href="https://science.nasa.gov/" target="_blank">NASA Science</a> · <a href="https://images-api.nasa.gov/" target="_blank">NASA Image and Video Library</a>'
    nasa_images = '<a href="https://images.nasa.gov/" target="_blank">NASA Images</a> · <a href="https://www.jpl.nasa.gov/" target="_blank">NASA/JPL</a>'
    st.markdown(
        f'<div class="mars-credit-panel">'
        f'<div class="mars-credit-title">{person_label}</div>'
        f'<div class="mars-credit-value">Bùi Hữu Minh Đăng</div>'
        f'<div class="mars-credit-title">{project_label}</div>'
        f'<div class="mars-credit-value">SPACE LEGACY</div>'
        f'<div class="mars-credit-title">{data_label}</div>'
        f'<div class="mars-credit-value">{nasa_data}</div>'
        f'<div class="mars-credit-title">{image_label}</div>'
        f'<div class="mars-credit-value">{nasa_images}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def show_mars_timeline(language="vi"):
    if language not in ("vi", "en"):
        language = "vi"

    mars_css()

    # Dùng URL ảnh Sao Hỏa lấy trực tiếp từ kho tài sản NASA.
    globe_url = nasa_image("PIA00407")
    st.markdown(
        f'<style>.mars-planet {{ background-image: '
        f'linear-gradient(100deg, rgba(0,0,0,0.85), rgba(0,0,0,0.08)), '
        f'url("{globe_url}"); }}</style>',
        unsafe_allow_html=True
    )

    title = (
        "Khám phá Sao Hỏa"
        if language == "vi"
        else "MARS EXPLORATION"
    )

    subtitle = (
        "Những chuyến thám hiểm Sao Hỏa qua các năm"
        if language == "en"
        else "Những cột mốc khám phá hành tinh Đỏ"
    )

    st.markdown(
        f'<div class="mars-title">{title}</div>'
        f'<div class="mars-subtitle">{subtitle}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="mars-stage">
        <div class="mars-orbit"></div>
        <div class="mars-orbit-two"></div>
        <div class="mars-planet"></div>
        <div class="mars-caption">MARS · THE RED PLANET</div>
    </div>
    """, unsafe_allow_html=True)

    heading = (
        "Các nhiệm vụ nổi bật"
        if language == "vi"
        else "Featured Mars missions"
    )

    st.markdown(
        f'<div class="section-heading">{heading}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="timeline-line"></div>',
        unsafe_allow_html=True
    )

    # SEARCH AND FILTER

    search_label = "Tìm kiếm nhiệm vụ" if language == "vi" else "Search missions"
    search_placeholder = (
        "Nhập tên robot..."
        if language == "vi"
        else "Enter a rover name..."
    )

    search_text = st.text_input(
        search_label,
        placeholder=search_placeholder,
        key="mars_search"
    )

    filter_label = "Trạng thái nhiệm vụ" if language == "vi" else "Mission status"

    filter_options = (
        ["Tất cả", "Đang hoạt động", "Đã kết thúc"]
        if language == "vi"
        else ["All", "Active", "Ended"]
    )

    selected_filter = st.selectbox(
        filter_label,
        filter_options,
        key="mars_status_filter"
    )

    filtered_missions = MISSIONS.copy()

    if search_text:
        filtered_missions = [
            mission for mission in filtered_missions
            if search_text.lower() in mission["name"].lower()
        ]

    if selected_filter in ("Đang hoạt động", "Active"):
        filtered_missions = [
            mission for mission in filtered_missions
            if mission["status"] == "active"
        ]

    elif selected_filter in ("Đã kết thúc", "Ended"):
        filtered_missions = [
            mission for mission in filtered_missions
            if mission["status"] == "ended"
        ]

    # SORTING

    sort_label = "Sắp xếp theo năm" if language == "vi" else "Sort by year"

    sort_options = (
        ["Cũ nhất trước", "Mới nhất trước"]
        if language == "vi"
        else ["Oldest first", "Newest first"]
    )

    sort_choice = st.selectbox(
        sort_label,
        sort_options,
        key="mars_sort"
    )

    if sort_choice in ("Mới nhất trước", "Newest first"):
        filtered_missions.sort(
            key=lambda mission: mission["year"],
            reverse=True
        )
    else:
        filtered_missions.sort(
            key=lambda mission: mission["year"]
        )

    count_text = (
        f"Tìm thấy {len(filtered_missions)} nhiệm vụ"
        if language == "vi"
        else f'{len(filtered_missions)} missions found'
    )

    st.caption(count_text)

    # MISSION CARDS

    if not filtered_missions:
        st.warning(
            "Không tìm thấy nhiệm vụ phù hợp."
            if language == "vi"
            else "No matching missions found."
        )
    else:
        for start in range(0, len(filtered_missions), 4):
            columns = st.columns(4)

            for column, mission in zip(
                columns,
                filtered_missions[start:start + 4]
            ):
                with column:
                    show_mission_card(mission, language)

    # OPEN SELECTED MISSION

    selected_id = st.session_state.get("selected_mars_mission")

    if selected_id:
        selected_mission = next(
            (
                mission for mission in MISSIONS
                if mission["id"] == selected_id
            ),
            None
        )

        if selected_mission:
            show_mission_window(selected_mission, language)
        else:
            clear_selected_mission()

    # Quiz is a separate final section and unlocks after all mission profiles have been opened.
    show_mars_quiz(language)
    show_mars_credits(language)
            