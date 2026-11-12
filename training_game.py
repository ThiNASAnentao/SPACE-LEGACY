import streamlit as st
import streamlit.components.v1 as components
import random
import sqlite3
import hashlib
import secrets
from datetime import datetime
from pathlib import Path

# SPACE LEGACY - TRAINING CENTER
# All base-management values are fictional game values, not real mission operating limits.

ROBOT_QUESTIONS = [
    {
        "name": "SOJOURNER",
        "image": "https://images-assets.nasa.gov/image/PIA01122/PIA01122~orig.jpg",
        "q_vi": "Robot nào trở thành xe tự hành đầu tiên hoạt động trên Sao Hỏa?",
        "q_en": "Which rover became the first wheeled vehicle to operate on Mars?",
        "opts_vi": ["Curiosity", "Sojourner", "Perseverance", "Opportunity"],
        "opts_en": ["Curiosity", "Sojourner", "Perseverance", "Opportunity"],
        "answer": 1,
        "fact_vi": "Sojourner hoạt động trên Sao Hỏa trong sứ mệnh Mars Pathfinder năm 1997.",
        "fact_en": "Sojourner operated on Mars during the Mars Pathfinder mission in 1997.",
    },
    {
        "name": "SPIRIT & OPPORTUNITY",
        "image": "https://images-assets.nasa.gov/image/PIA05578/PIA05578~orig.jpg",
        "q_vi": "Spirit và Opportunity cùng hạ cánh xuống Sao Hỏa vào năm nào?",
        "q_en": "In which year did Spirit and Opportunity land on Mars?",
        "opts_vi": ["1997", "2001", "2004", "2012"],
        "opts_en": ["1997", "2001", "2004", "2012"],
        "answer": 2,
        "fact_vi": "Hai robot hạ cánh vào năm 2004. Opportunity hoạt động gần 15 năm.",
        "fact_en": "Both rovers landed in 2004. Opportunity operated for nearly 15 years.",
    },
    {
        "name": "PERSEVERANCE",
        "image": "https://images-assets.nasa.gov/image/PIA24342/PIA24342~orig.jpg",
        "q_vi": "Thiết bị bay nào được Perseverance mang theo để thử nghiệm trên Sao Hỏa?",
        "q_en": "Which flying vehicle did Perseverance carry to test on Mars?",
        "opts_vi": ["Dragonfly", "Ingenuity", "Huygens", "Viking"],
        "opts_en": ["Dragonfly", "Ingenuity", "Huygens", "Viking"],
        "answer": 1,
        "fact_vi": "Ingenuity là trực thăng thử nghiệm công nghệ, được đưa đến Sao Hỏa cùng Perseverance.",
        "fact_en": "Ingenuity was a technology-demonstration helicopter delivered to Mars with Perseverance.",
    },
]

# 5 decision rounds, 4 choices each. Values are game-only resource units.
BASE_ROUNDS = [
    {
        "title_vi": "BÃO BỤI ĐANG TIẾN ĐẾN",
        "title_en": "DUST STORM APPROACHING",
        "story_vi": "Cảm biến phát hiện một cơn bão bụi đang tiến gần. Tấm pin có thể giảm hiệu suất, nhưng đội vẫn cần điện cho hệ thống sống còn.",
        "story_en": "Sensors detect an approaching dust storm. Solar panels may lose efficiency, but life-support still needs power.",
        "choices": [
            ("Bật chế độ tiết kiệm điện", "Giữ điện, giảm một phần tiện nghi", {"power": 12, "oxygen": 0, "water": 0, "food": 0, "hull": 2}, 8),
            ("Đưa robot đi vệ sinh pin", "Tốn điện và rủi ro, nhưng cải thiện nguồn điện về sau", {"power": -8, "oxygen": 0, "water": -2, "food": 0, "hull": 0}, 12),
            ("Đóng kín khu vực phụ", "Bảo vệ căn cứ, giảm diện tích cần duy trì", {"power": 5, "oxygen": 3, "water": 0, "food": 0, "hull": 5}, 10),
            ("Giữ nguyên mọi hoạt động", "Không thay đổi kế hoạch, nhưng tiêu hao nhiều hơn", {"power": -12, "oxygen": -5, "water": -2, "food": 0, "hull": -4}, 1),
        ],
    },
    {
        "title_vi": "SỰ CỐ HỆ THỐNG OXY",
        "title_en": "OXYGEN SYSTEM ALERT",
        "story_vi": "Một bộ lọc không khí hoạt động kém. Bạn có thể chuyển sang bộ lọc dự phòng, sửa chữa ngay hoặc phân bổ lại khu sinh hoạt.",
        "story_en": "An air filter is underperforming. You can switch to backup filtration, repair it now, or reorganize the living area.",
        "choices": [
            ("Chuyển sang bộ lọc dự phòng", "Tốn điện nhưng ổn định oxy nhanh", {"power": -7, "oxygen": 14, "water": 0, "food": 0, "hull": 0}, 10),
            ("Dừng khu thí nghiệm để sửa", "Hy sinh tiến độ nghiên cứu để sửa hệ thống", {"power": -3, "oxygen": 10, "water": 0, "food": 0, "hull": 1}, 12),
            ("Chia nhỏ khu sinh hoạt", "Giảm nhu cầu oxy, nhưng bất tiện cho đội", {"power": 2, "oxygen": 5, "water": -1, "food": 0, "hull": 0}, 8),
            ("Bỏ qua cảnh báo", "Tiết kiệm thời gian trước mắt nhưng rủi ro tăng", {"power": 0, "oxygen": -16, "water": 0, "food": 0, "hull": -5}, 0),
        ],
    },
    {
        "title_vi": "KHO NƯỚC BỊ RÒ RỈ",
        "title_en": "WATER STORAGE LEAK",
        "story_vi": "Một đường ống nước bị rò. Đội có thể cô lập đường ống, dùng nước dự trữ hoặc điều robot kiểm tra điểm rò.",
        "story_en": "A water pipe is leaking. The crew can isolate the pipe, use reserve water, or send a robot to inspect the leak.",
        "choices": [
            ("Cô lập đường ống", "Giữ phần lớn nước, nhưng một khu phải tạm ngừng", {"power": -2, "oxygen": 0, "water": 9, "food": 0, "hull": 1}, 11),
            ("Dùng nước dự trữ để duy trì", "Đội vẫn sinh hoạt bình thường nhưng kho giảm", {"power": 0, "oxygen": 0, "water": -8, "food": 0, "hull": 0}, 4),
            ("Gửi robot kiểm tra và vá rò", "Tốn năng lượng, có cơ hội khôi phục hệ thống", {"power": -6, "oxygen": 0, "water": 13, "food": 0, "hull": 0}, 12),
            ("Phân phối nước theo mức ưu tiên", "Giảm nhu cầu ngay, không cần sửa tức thì", {"power": 1, "oxygen": 0, "water": 5, "food": 0, "hull": 0}, 8),
        ],
    },
    {
        "title_vi": "TÍN HIỆU CẦU CỨU TỪ ROBOT",
        "title_en": "ROVER DISTRESS SIGNAL",
        "story_vi": "Robot thám hiểm gửi tín hiệu lỗi ở khu vực nhiều đá. Bạn cần cân nhắc giá trị dữ liệu, độ an toàn và nguồn lực còn lại.",
        "story_en": "A rover sends a fault signal from a rocky area. Consider science value, safety, and remaining resources.",
        "choices": [
            ("Gửi robot cứu hộ", "Có thể cứu thiết bị nhưng tiêu tốn nhiều tài nguyên", {"power": -9, "oxygen": -2, "water": -1, "food": 0, "hull": 0, "fuel": -12}, 10),
            ("Điều khiển robot tự quay về", "Chọn đường vòng an toàn, chậm hơn", {"power": -4, "oxygen": 0, "water": 0, "food": 0, "hull": 2, "fuel": -5}, 12),
            ("Yêu cầu robot gửi dữ liệu trước", "Ưu tiên lưu dữ liệu khoa học rồi mới quyết định", {"power": -2, "oxygen": 0, "water": 0, "food": 0, "hull": 0}, 11),
            ("Bỏ lại robot và khóa khu vực", "Bảo vệ căn cứ nhưng mất thiết bị", {"power": 3, "oxygen": 1, "water": 0, "food": 0, "hull": 1}, 5),
        ],
    },
    {
        "title_vi": "QUYẾT ĐỊNH CUỐI CÙNG",
        "title_en": "FINAL MISSION DECISION",
        "story_vi": "Một chuyến vận chuyển tiếp tế bị trì hoãn. Bạn phải chọn cách sử dụng nguồn lực cuối cùng để duy trì căn cứ và hoàn thành mục tiêu.",
        "story_en": "A supply delivery is delayed. Choose how to use the remaining resources to sustain the base and complete the mission.",
        "choices": [
            ("Ưu tiên hệ thống sống còn", "Giữ oxy, nước và điện; hoãn nghiên cứu", {"power": 5, "oxygen": 8, "water": 5, "food": 4, "hull": 3}, 12),
            ("Tập trung thu thập mẫu khoa học", "Tăng giá trị nghiên cứu nhưng dùng nhiều tài nguyên", {"power": -8, "oxygen": -3, "water": -3, "food": -2, "hull": 0}, 8),
            ("Kích hoạt chế độ ngủ luân phiên", "Giảm tiêu thụ nhưng cần phối hợp lịch trực", {"power": 8, "oxygen": 5, "water": 3, "food": 2, "hull": 0}, 11),
            ("Sơ tán về khoang an toàn", "Bảo toàn đội, chấp nhận kết thúc sớm nhiệm vụ", {"power": 2, "oxygen": 6, "water": 3, "food": 3, "hull": 5}, 9),
        ],
    },
]


# Một câu hỏi tư duy bổ sung ở mỗi lượt; đáp án tốt sẽ cộng điểm chiến thuật.
STRATEGY_CHECKS = [
    {
        "q_vi": "Bão bụi có thể kéo dài lâu hơn dự kiến. Dữ liệu nào cần kiểm tra trước khi chọn phương án?",
        "q_en": "The dust storm may last longer than expected. What should you check first?",
        "opts_vi": ["Dự trữ điện và mức tiêu thụ của hệ thống sống còn", "Màu sơn của xe rover", "Số ảnh trong kho lưu trữ"],
        "opts_en": ["Power reserves and life-support consumption", "The rover's paint color", "The number of archived photos"],
        "answer": 0,
    },
    {
        "q_vi": "Bộ lọc chính yếu đi. Vì sao không nên chỉ bật mọi thiết bị dự phòng cùng lúc?",
        "q_en": "The main filter is weakening. Why not activate every backup device at once?",
        "opts_vi": ["Vì thiết bị dự phòng có thể tiêu thụ điện và tạo tải phụ", "Vì dự phòng không bao giờ hoạt động", "Vì oxy không cần được theo dõi"],
        "opts_en": ["Backups may consume power and add system load", "Backups never work", "Oxygen does not need monitoring"],
        "answer": 0,
    },
    {
        "q_vi": "Khi phát hiện rò rỉ nước, bước nào giúp tránh mất thêm tài nguyên?",
        "q_en": "When a water leak is detected, what helps prevent further resource loss?",
        "opts_vi": ["Cô lập khu vực bị rò trước khi sửa", "Tăng lượng nước bơm qua ống", "Tắt toàn bộ liên lạc"],
        "opts_en": ["Isolate the leaking section before repair", "Pump more water through the pipe", "Shut down all communications"],
        "answer": 0,
    },
    {
        "q_vi": "Robot gửi tín hiệu lỗi ở địa hình đá. Thông tin nào quan trọng nhất trước khi điều động cứu hộ?",
        "q_en": "A rover reports a fault in rocky terrain. What matters most before dispatching help?",
        "opts_vi": ["Vị trí, mức pin và tuyến đường an toàn", "Tên người đặt tên robot", "Màu nền giao diện điều khiển"],
        "opts_en": ["Location, battery level, and a safe route", "Who named the rover", "The control interface background color"],
        "answer": 0,
    },
    {
        "q_vi": "Nguồn tiếp tế bị trễ. Nguyên tắc nào nên dẫn dắt quyết định cuối cùng?",
        "q_en": "Resupply is delayed. Which principle should guide the final decision?",
        "opts_vi": ["Ưu tiên an toàn, rồi cân bằng tài nguyên và mục tiêu", "Dùng hết tài nguyên cho nghiên cứu", "Bỏ qua các cảnh báo còn lại"],
        "opts_en": ["Prioritize safety, then balance resources and objectives", "Spend everything on research", "Ignore all remaining warnings"],
        "answer": 0,
    },
]

ENDINGS = [
    ("Huyền thoại Mặt Trăng", "Căn cứ trở thành hình mẫu cho các thế hệ thám hiểm tương lai.", "LEGEND OF THE MOON"),
    ("Người kiến tạo tương lai", "Bạn giữ căn cứ ổn định và mở ra một chương mới cho khoa học.", "BUILDER OF TOMORROW"),
    ("Chỉ huy xuất sắc", "Đội ngũ phối hợp tốt, tài nguyên được sử dụng rất hiệu quả.", "EXCELLENT COMMANDER"),
    ("Ngọn hải đăng vũ trụ", "Căn cứ vẫn hoạt động và trở thành điểm tựa cho các chuyến bay sau.", "BEACON IN SPACE"),
    ("Nhà chiến lược tài ba", "Những quyết định cân bằng giúp nhiệm vụ đạt kết quả nổi bật.", "MASTER STRATEGIST"),
    ("Sứ mệnh vàng", "Bạn hoàn thành hầu hết mục tiêu và bảo toàn phần lớn tài nguyên.", "GOLDEN MISSION"),
    ("Người bảo vệ căn cứ", "Căn cứ an toàn, dù một vài mục tiêu nghiên cứu phải hoãn lại.", "BASE GUARDIAN"),
    ("Nhà thám hiểm kiên trì", "Nhiệm vụ thành công sau nhiều quyết định khó khăn.", "RESILIENT EXPLORER"),
    ("Thành công có điều kiện", "Căn cứ duy trì hoạt động nhưng cần bổ sung nguồn lực sớm.", "CONDITIONAL SUCCESS"),
    ("Trở về an toàn", "Đội ngũ được bảo toàn, nhiệm vụ kết thúc sớm hơn dự kiến.", "SAFE RETURN"),
    ("Bài học quý giá", "Bạn giữ được căn cứ nhưng phải đánh đổi nhiều thiết bị.", "VALUABLE LESSON"),
    ("Tín hiệu yếu", "Căn cứ còn hoạt động ở mức tối thiểu và cần hỗ trợ.", "WEAK SIGNAL"),
    ("Nhiệm vụ dang dở", "Một số hệ thống phải tắt để duy trì những khu vực quan trọng.", "INCOMPLETE MISSION"),
    ("Mất điện từng phần", "Nguồn điện thiếu hụt khiến nhiều hoạt động bị đình trệ.", "PARTIAL POWER LOSS"),
    ("Kho dự trữ cạn dần", "Căn cứ phải chuyển sang chế độ khẩn cấp để tiết kiệm tài nguyên.", "SUPPLIES RUNNING LOW"),
    ("Báo động đỏ", "Nhiều hệ thống cần sửa chữa trước khi đội có thể tiếp tục.", "RED ALERT"),
    ("Sơ tán bắt buộc", "Đội phải rời khỏi căn cứ để bảo đảm an toàn.", "EVACUATION"),
    ("Căn cứ im lặng", "Các hoạt động dừng lại và chỉ còn hệ thống ghi dữ liệu tự động.", "SILENT BASE"),
    ("Mất liên lạc", "Căn cứ không thể duy trì liên lạc ổn định với trung tâm điều khiển.", "COMMUNICATION LOST"),
    ("Di sản bị bỏ lại", "Nhiệm vụ kết thúc trong khó khăn; căn cứ trở thành một di tích cần được ghi nhớ.", "LEGACY LEFT BEHIND"),
]


ENDING_DESCRIPTIONS_EN = [
    "The base becomes a model for future generations of explorers.",
    "You keep the base stable and open a new chapter for science.",
    "The crew works together and resources are used efficiently.",
    "The base remains active and supports future missions.",
    "Balanced decisions lead to an outstanding mission result.",
    "You complete most objectives and preserve most resources.",
    "The base is safe, although some research must be postponed.",
    "The mission succeeds after a series of difficult decisions.",
    "The base keeps operating but needs supplies soon.",
    "The crew is safe, but the mission ends earlier than planned.",
    "You preserve the base but sacrifice several pieces of equipment.",
    "The base remains at minimum operations and needs support.",
    "Some systems must shut down to protect critical areas.",
    "Power shortages interrupt many activities.",
    "The base switches to emergency mode to conserve resources.",
    "Several systems need repairs before the crew can continue.",
    "The crew must leave the base to remain safe.",
    "Operations stop, leaving only automatic data recording.",
    "The base cannot maintain a stable connection with mission control.",
    "The mission ends in difficulty; the base becomes a legacy site to remember.",
]



DB_PATH = Path(__file__).with_name("space_legacy_accounts.db")


def db_connect():
    conn = sqlite3.connect(DB_PATH, timeout=20)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_database():
    with db_connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY COLLATE NOCASE,
            salt TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            mode TEXT NOT NULL,
            score INTEGER NOT NULL,
            ending TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")


def password_digest(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt), 260000).hex()


def create_account(username, password):
    username = username.strip()
    if not 3 <= len(username) <= 18 or not username.replace("_", "").isalnum():
        return False, "Tên tài khoản dài 3–18 ký tự, chỉ gồm chữ, số hoặc dấu gạch dưới."
    if len(password) < 8:
        return False, "Mật khẩu cần ít nhất 8 ký tự. Đừng dùng mật khẩu thật đang dùng ở nơi khác."
    salt = secrets.token_bytes(16).hex()
    digest = password_digest(password, salt)
    try:
        with db_connect() as conn:
            conn.execute("INSERT INTO users(username,salt,password_hash,created_at) VALUES(?,?,?,?)",
                         (username, salt, digest, datetime.utcnow().isoformat(timespec="seconds")))
        return True, "Tạo tài khoản thành công!"
    except sqlite3.IntegrityError:
        return False, "Tên tài khoản đã được sử dụng. Hãy chọn tên khác."


def verify_account(username, password):
    with db_connect() as conn:
        row = conn.execute("SELECT username,salt,password_hash FROM users WHERE username=?", (username.strip(),)).fetchone()
    if not row:
        return False
    return secrets.compare_digest(password_digest(password, row[1]), row[2])


def save_score(username, mode, score, ending):
    if not username:
        return
    with db_connect() as conn:
        conn.execute("INSERT INTO scores(username,mode,score,ending,created_at) VALUES(?,?,?,?,?)",
                     (username, mode, int(score), ending, datetime.utcnow().isoformat(timespec="seconds")))


def get_leaderboard(limit=10):
    with db_connect() as conn:
        return conn.execute("""SELECT s.username, s.mode, s.score, s.ending
            FROM scores AS s
            JOIN (SELECT username, mode, MAX(score) AS best_score
                  FROM scores GROUP BY username, mode) AS best
              ON s.username = best.username AND s.mode = best.mode AND s.score = best.best_score
            ORDER BY s.score DESC, s.created_at ASC LIMIT ?""", (limit,)).fetchall()


def account_gate(language):
    init_database()
    if st.session_state.auth_user:
        left, right = st.columns([4, 1])
        with left:
            st.success(tx(language, f"Đang đăng nhập: **{st.session_state.auth_user}**", f"Signed in as **{st.session_state.auth_user}**"))
        with right:
            if st.button(tx(language, "Đăng xuất", "Log out"), key="training_logout"):
                st.session_state.auth_user = None
                st.rerun()
        return True

    st.markdown("### 🔐 " + tx(language, "TÀI KHOẢN PHI HÀNH GIA", "ASTRONAUT ACCOUNT"))
    st.caption(tx(language, "Tạo tên người chơi riêng để lưu thành tích. Mật khẩu được băm trước khi lưu; đừng dùng mật khẩu cá nhân quan trọng.",
                  "Create a player name to save scores. Passwords are hashed before storage; do not reuse an important personal password."))
    tab_login, tab_register = st.tabs([tx(language, "Đăng nhập", "Sign in"), tx(language, "Tạo tài khoản", "Create account")])
    with tab_login:
        with st.form("training_login_form"):
            username = st.text_input(tx(language, "Tên người chơi", "Player name"), max_chars=18)
            password = st.text_input(tx(language, "Mật khẩu", "Password"), type="password")
            submitted = st.form_submit_button(tx(language, "ĐĂNG NHẬP", "SIGN IN"), use_container_width=True)
        if submitted:
            if verify_account(username, password):
                st.session_state.auth_user = username.strip()
                st.success(tx(language, "Đăng nhập thành công!", "Signed in successfully!")); st.rerun()
            else:
                st.error(tx(language, "Tên người chơi hoặc mật khẩu chưa đúng.", "Incorrect player name or password."))
    with tab_register:
        with st.form("training_register_form"):
            new_user = st.text_input(tx(language, "Tên người chơi (3–18 ký tự)", "Player name (3–18 characters)"), max_chars=18)
            new_password = st.text_input(tx(language, "Mật khẩu (ít nhất 8 ký tự)", "Password (at least 8 characters)"), type="password")
            confirm = st.text_input(tx(language, "Nhập lại mật khẩu", "Confirm password"), type="password")
            submitted = st.form_submit_button(tx(language, "TẠO TÀI KHOẢN", "CREATE ACCOUNT"), use_container_width=True)
        if submitted:
            if new_password != confirm:
                st.error(tx(language, "Hai mật khẩu không khớp.", "Passwords do not match."))
            else:
                ok, message = create_account(new_user, new_password)
                if ok:
                    st.success(tx(language, message, "Account created. Sign in to continue."))
                else:
                    st.error(message)
    return False

def tx(language, vi, en):
    return vi if language == "VI" else en


def init_state():
    defaults = {
        "training_stage": "menu", "training_game": None, "memory_round": 0,
        "memory_score": 0, "memory_failed": None, "memory_read": [],
        "base_round": 0, "base_resources": {"oxygen": 80, "power": 80, "water": 70, "food": 75, "hull": 90, "fuel": 65},
        "base_points": 0, "base_log": [], "base_ending": None,
        "training_leaderboard": [], "training_attempts": 0, "auth_user": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, (dict, list)) else value


def reset_memory():
    st.session_state.training_stage = "memory"
    st.session_state.memory_round = 0
    st.session_state.memory_score = 0
    st.session_state.memory_failed = None
    st.session_state.memory_read = []


def reset_base():
    st.session_state.training_stage = "base"
    st.session_state.base_round = 0
    st.session_state.base_resources = {"oxygen": 80, "power": 80, "water": 70, "food": 75, "hull": 90, "fuel": 65}
    st.session_state.base_points = 0
    st.session_state.base_log = []
    st.session_state.base_ending = None


def add_leaderboard(mode, score, ending):
    st.session_state.training_attempts += 1
    st.session_state.training_leaderboard.append({
        "mode": mode, "score": int(score), "ending": ending,
        "attempt": st.session_state.training_attempts,
    })
    st.session_state.training_leaderboard = sorted(
        st.session_state.training_leaderboard,
        key=lambda item: item["score"], reverse=True
    )[:10]
    save_score(st.session_state.auth_user, mode, score, ending)


def render_base_scene(language="VI", event_name="DUST"):
    st.markdown("### 🌕 " + tx(language, "MÔ PHỎNG CĂN CỨ MẶT TRĂNG 3D", "3D LUNAR SURFACE SIMULATION"))
    st.caption(tx(language, "Kéo chuột để xoay 360° · Cuộn để phóng to/thu nhỏ · Nhấn nút để đổi góc nhìn", "Drag to orbit 360° · Scroll to zoom · Use buttons to change camera view"))
    event_map = {
        "DUST": ("BỤI MẶT TRĂNG", "Bụi mịn bay ngang bề mặt, làm giảm tầm nhìn và hiệu suất pin", "LUNAR DUST", "Fine dust sweeps across the surface and reduces solar output"),
        "METEOR": ("MƯA THIÊN THẠCH XA", "Các vệt sáng xuất hiện trên bầu trời; hệ thống quan sát chuyển sang theo dõi", "DISTANT METEOR SHOWER", "Bright streaks cross the sky as the observation system tracks them"),
        "ECLIPSE": ("NHẬT THỰC TRÊN MẶT TRĂNG", "Ánh sáng Mặt Trời bị che khuất tạm thời; nguồn điện mặt trời giảm", "LUNAR ECLIPSE VIEW", "Sunlight is temporarily obscured, reducing solar power"),
        "THERMAL": ("BIẾN ĐỘNG NHIỆT ĐỘ", "Bề mặt chuyển sang trạng thái lạnh sâu; căn cứ cần ưu tiên hệ thống sưởi", "THERMAL SWING", "The surface enters an extreme cold phase; heating becomes a priority"),
        "MICRO": ("CẢNH BÁO VI HẠT", "Cảm biến phát hiện hạt nhỏ đi qua vùng quan sát; đóng cửa chắn ngoài", "MICROMETEOROID WATCH", "Sensors detect small particles crossing the observation zone"),
    }
    vi_title, vi_desc, en_title, en_desc = event_map.get(event_name, event_map["DUST"])
    st.markdown(f"<div style='padding:10px 14px;border:1px solid #477ca8;border-radius:12px;background:#0b1b2e;color:#fff;margin:6px 0 10px'><b>⚠️ {tx(language, vi_title, en_title)}</b><br><span style='color:#c5d9ed'>{tx(language, vi_desc, en_desc)}</span></div>", unsafe_allow_html=True)
    scene_html = r"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#030711;font-family:Arial;color:#eaf6ff}
    #view{width:100%;height:520px;position:relative;border:1px solid #3d78a8;border-radius:16px;overflow:hidden;background:#050a14}
    #hud{position:absolute;top:12px;left:14px;z-index:5;background:#061323d9;border:1px solid #4c86b7;border-radius:10px;padding:9px 12px;font-size:11px;letter-spacing:1.5px;pointer-events:none}
    #hint{position:absolute;bottom:10px;left:14px;z-index:5;color:#c7d9ec;background:#061323d9;padding:7px 10px;border-radius:8px;font-size:11px;pointer-events:none}
    #controls{position:absolute;right:12px;top:12px;z-index:6;display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end;max-width:55%}
    button{background:#0d3961;color:white;border:1px solid #65baff;border-radius:8px;padding:8px 10px;font-weight:bold;cursor:pointer}button:hover{background:#176ca8}
    #legend{position:absolute;right:12px;bottom:10px;z-index:5;background:#061323e8;border:1px solid #345a7c;border-radius:9px;padding:8px 10px;font-size:11px;line-height:1.7;pointer-events:none}
    </style></head><body><div id="view"><div id="hud">SPACE LEGACY · LUNAR OUTPOST 07<br><span style="color:#8dcaff">INTERACTIVE 3D FIELD VIEW</span></div><div id="controls"><button onclick="window.setView('top')">TOP</button><button onclick="window.setView('front')">FRONT</button><button onclick="window.setView('reset')">RESET</button></div><div id="hint">Drag: orbit · Scroll: zoom · Right-drag: pan</div><div id="legend">● Habitat & lab<br>● Solar farm<br>● Water / oxygen tanks<br>● Rover & landing zone</div><div id="stage" style="position:absolute;inset:0"></div><div id="scene-error" style="display:none;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:10;max-width:80%;padding:14px 18px;border:1px solid #ffb45e;border-radius:10px;background:#24170d;color:#fff;text-align:center">Không tải được thư viện 3D. Hãy kiểm tra kết nối Internet hoặc trình duyệt có hỗ trợ WebGL.</div></div>
    <script type="importmap">
    {"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}
    </script>
    <script>
    window.addEventListener('error',function(){const e=document.getElementById('scene-error');if(e)e.style.display='block'});
    window.addEventListener('unhandledrejection',function(){const e=document.getElementById('scene-error');if(e)e.style.display='block'});
    </script>
    <script type="module">
    import * as THREE from 'three';
    import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
    const root=document.getElementById('stage'),scene=new THREE.Scene();scene.background=new THREE.Color(0x050a14);scene.fog=new THREE.Fog(0x070d18,38,100);
    const camera=new THREE.PerspectiveCamera(48,root.clientWidth/root.clientHeight,.1,500);camera.position.set(27,22,30);
    const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setSize(root.clientWidth,root.clientHeight);renderer.shadowMap.enabled=true;renderer.toneMapping=THREE.ACESFilmicToneMapping;root.appendChild(renderer.domElement);
    const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.dampingFactor=.06;controls.minDistance=12;controls.maxDistance=65;controls.maxPolarAngle=Math.PI*.48;controls.target.set(0,0,0);
    scene.add(new THREE.HemisphereLight(0xa9c9ed,0x35313a,2));const sun=new THREE.DirectionalLight(0xffedcf,3.3);sun.position.set(-22,30,18);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);scene.add(sun);
    const ground=new THREE.Mesh(new THREE.CircleGeometry(29,96),new THREE.MeshStandardMaterial({color:0x777982,roughness:1}));ground.rotation.x=-Math.PI/2;ground.position.y=-.35;ground.receiveShadow=true;scene.add(ground);
    const craterMat=new THREE.MeshStandardMaterial({color:0x484b55,roughness:1});function crater(x,z,r){let g=new THREE.Group(),b=new THREE.Mesh(new THREE.CylinderGeometry(r*.72,r,.28,32,1,true),craterMat);b.rotation.x=Math.PI;b.position.y=-.18;g.add(b);let rim=new THREE.Mesh(new THREE.TorusGeometry(r*.83,.12,8,40),new THREE.MeshStandardMaterial({color:0x9698a0}));rim.rotation.x=Math.PI/2;rim.position.y=-.02;g.add(rim);g.position.set(x,0,z);scene.add(g)}
    [[-15,-10,3],[14,-12,4],[-13,12,2.4],[17,10,2.2],[2,-19,1.8]].forEach(v=>crater(...v));
    const mat=(c,m=0)=>new THREE.MeshStandardMaterial({color:c,metalness:m,roughness:.62});function box(x,y,z,sx,sy,sz,color,rot=0){let o=new THREE.Mesh(new THREE.BoxGeometry(sx,sy,sz),mat(color,.35));o.position.set(x,y,z);o.rotation.y=rot;o.castShadow=true;o.receiveShadow=true;scene.add(o);return o}function cyl(x,y,z,rt,rb,h,color){let o=new THREE.Mesh(new THREE.CylinderGeometry(rt,rb,h,24),mat(color,.35));o.position.set(x,y,z);o.castShadow=true;scene.add(o);return o}
    function dome(x,z,r){let o=new THREE.Mesh(new THREE.SphereGeometry(r,32,20,0,Math.PI*2,0,Math.PI/2),new THREE.MeshPhysicalMaterial({color:0x75bce9,metalness:.3,roughness:.18,transparent:true,opacity:.78,clearcoat:1}));o.position.set(x,.05,z);o.castShadow=true;scene.add(o);let b=new THREE.Mesh(new THREE.CylinderGeometry(r,r,.28,32),mat(0x9ba8b7,.6));b.position.set(x,0,z);scene.add(b)}
    dome(-3,0,3.1);box(2,.9,0,4.2,1.8,3.3,0xb7c2ce,.1);box(2,1.9,0,3.4,.18,2.7,0x607e9a,.1);box(-7,.65,1,3.2,1.3,2.6,0x8999aa,-.2);
    let tunnel=new THREE.Mesh(new THREE.CylinderGeometry(.48,.48,5,20),mat(0x9caab7,.55));tunnel.rotation.z=Math.PI/2;tunnel.position.set(-.4,.65,.4);scene.add(tunnel);
    for(let i=0;i<3;i++){box(8+i*2,.95,-5,1.7,.12,3.4,0x123d70,.12);for(let j=0;j<4;j++)box(8+i*2,.99,-6.25+j*.83,1.62,.025,.025,0x76b9e9,.12);cyl(8+i*2,.4,-5,.08,.08,.9,0xadb8c3)}
    [0x4d9bd1,0x9cc7dc,0xd0a75d].forEach((c,i)=>{cyl(-8,.8,-4+i*2,.65,.65,1.6,c);let cap=new THREE.Mesh(new THREE.SphereGeometry(.65,18,10,0,Math.PI*2,0,Math.PI/2),mat(c));cap.position.set(-8,1.6,-4+i*2);scene.add(cap)});
    cyl(7,1,4,.12,.12,2.1,0xc6d1dc);let dish=new THREE.Mesh(new THREE.SphereGeometry(1,24,12,0,Math.PI,0,Math.PI/2),mat(0xd5e0e9,.5));dish.position.set(7,2,4);scene.add(dish);
    box(3,.55,7,1.8,.65,1.25,0xc89a48);for(let x of [2.4,3.6])for(let z of [6.35,7.65]){let w=new THREE.Mesh(new THREE.CylinderGeometry(.32,.32,.18,18),mat(0x20252c));w.rotation.z=Math.PI/2;w.position.set(x,.28,z);scene.add(w)}box(3,1.25,7,.45,.8,.45,0xd5e2eb);
    const pad=new THREE.Mesh(new THREE.CylinderGeometry(3.3,3.3,.12,48),mat(0x555b65));pad.position.set(13,.02,5);scene.add(pad);box(13,.12,5,2.4,.05,.15,0xf0c65d);
    const sg=new THREE.BufferGeometry(),sp=[];for(let i=0;i<700;i++)sp.push((Math.random()-.5)*180,Math.random()*100+12,(Math.random()-.5)*180);sg.setAttribute('position',new THREE.Float32BufferAttribute(sp,3));scene.add(new THREE.Points(sg,new THREE.PointsMaterial({color:0xd9e9ff,size:.16})));
    const event='EVENT_TOKEN';if(event==='DUST'){const g=new THREE.BufferGeometry(),a=[];for(let i=0;i<900;i++)a.push((Math.random()-.5)*55,Math.random()*7+.2,(Math.random()-.5)*45);g.setAttribute('position',new THREE.Float32BufferAttribute(a,3));const dust=new THREE.Points(g,new THREE.PointsMaterial({color:0xb9a98c,size:.22,transparent:true,opacity:.45}));scene.add(dust);window.animateDust=()=>{let p=dust.geometry.attributes.position;for(let i=0;i<p.count;i++){p.array[i*3]+=.045;if(p.array[i*3]>28)p.array[i*3]=-28}p.needsUpdate=true}}
    if(event==='METEOR'){for(let i=0;i<8;i++){let m=new THREE.Mesh(new THREE.CylinderGeometry(.025,.025,5,6),new THREE.MeshBasicMaterial({color:0xffd9a0}));m.position.set(-22+i*6,17+Math.random()*8,-18+Math.random()*28);m.rotation.z=-1.15;scene.add(m)}}if(event==='ECLIPSE'){sun.intensity=.6;let d=new THREE.Mesh(new THREE.SphereGeometry(3.2,32,24),new THREE.MeshBasicMaterial({color:0x080b15}));d.position.set(-15,22,-18);scene.add(d)}if(event==='THERMAL'){let l=new THREE.PointLight(0x83baff,1.5,35);l.position.set(0,9,0);scene.add(l)}if(event==='MICRO'){for(let i=0;i<18;i++){let p=new THREE.Mesh(new THREE.SphereGeometry(.09,8,8),new THREE.MeshBasicMaterial({color:0xffc978}));p.position.set((Math.random()-.5)*40,4+Math.random()*12,(Math.random()-.5)*40);scene.add(p)}}
    window.setView=(v)=>{camera.position.set(...(v==='top'?[0,38,.1]:v==='front'?[0,12,37]:[27,22,30]));controls.target.set(0,0,0);controls.update()};const resize=()=>{camera.aspect=root.clientWidth/root.clientHeight;camera.updateProjectionMatrix();renderer.setSize(root.clientWidth,root.clientHeight)};new ResizeObserver(resize).observe(root);function loop(){requestAnimationFrame(loop);controls.update();if(window.animateDust)window.animateDust();renderer.render(scene,camera)}loop();
    </script></body></html>"""
    scene_html = scene_html.replace("EVENT_TOKEN", event_name)
    components.html(scene_html, height=535, scrolling=False)


def render_resources(r):
    labels = [("oxygen", "🫁 OXYGEN"), ("power", "⚡ POWER"), ("water", "💧 WATER"), ("food", "🥫 FOOD"), ("fuel", "⛽ FUEL"), ("hull", "🛡️ BASE INTEGRITY")]
    cols = st.columns(6)
    for col, (key, title) in zip(cols, labels):
        with col:
            value = max(0, min(100, int(r.get(key, 65))))
            st.metric(title, f"{value}%")
            st.progress(value / 100)


def choose_ending(resources, points):
    avg = sum(max(0, min(100, v)) for v in resources.values()) / len(resources)
    score = max(0, min(100, round((points / 60) * 55 + avg * 0.45)))
    # 20 distinct endings, from strongest to weakest.
    index = min(19, max(0, 19 - score // 5))
    return index, score


def show_leaderboard(language):
    st.markdown("## 🏆 " + tx(language, "BẢNG XẾP HẠNG", "LEADERBOARD"))
    st.caption(tx(language, "Thành tích tốt nhất của từng người chơi được lưu trong cơ sở dữ liệu. Bản SQLite trên Streamlit Cloud có thể bị làm mới khi máy chủ khởi động lại.",
                  "Each player's best score is stored in the app database. SQLite data on Streamlit Cloud may reset when the server restarts."))
    rows = get_leaderboard(10)
    if not rows:
        st.info(tx(language, "Chưa có kết quả. Hãy hoàn thành thử thách đầu tiên!", "No scores yet. Complete your first challenge!"))
        return
    table_rows = []
    for rank, row in enumerate(rows, 1):
        table_rows.append({
            "#": rank, tx(language, "Người chơi", "Player"): row[0],
            tx(language, "Chế độ", "Mode"): row[1],
            tx(language, "Điểm", "Score"): f"{row[2]}/100",
            tx(language, "Kết thúc", "Ending"): row[3],
        })
    st.dataframe(table_rows, use_container_width=True, hide_index=True)


def show_training_game(language="VI"):
    init_state()
    if not account_gate(language):
        return
    st.markdown("""
    <div style="text-align:center;padding:18px 8px 22px;border:1px solid #35699f;border-radius:16px;
    background:linear-gradient(120deg,#102847,#080f1d);margin-bottom:20px">
      <div style="font:800 clamp(25px,4vw,40px) Orbitron,Arial;color:#eaf5ff;letter-spacing:3px;text-shadow:0 0 18px #4a9dff">TRAINING CENTER</div>
      <div style="font:700 13px Orbitron,Arial;color:#82bdff;letter-spacing:4px;margin-top:8px">REVENGE PROTOCOL · LUNAR COMMAND</div>
      <p style="color:#c1d5eb;margin:12px 0 0">Think ahead. Protect the crew. Preserve the legacy.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(tx(language, "← VỀ TRANG CHỦ", "← BACK HOME"), key="training_back_home"):
        st.session_state.page = "home"
        st.session_state.training_stage = "menu"
        st.rerun()

    stage = st.session_state.training_stage

    if stage == "menu":
        st.markdown("### " + tx(language, "CHỌN CHƯƠNG TRÌNH HUẤN LUYỆN", "SELECT TRAINING PROGRAM"))
        a, b = st.columns(2, gap="large")
        with a:
            st.markdown("<div class='training-panel'><h3>🤖 ROBOT MEMORY</h3><p>Nhận diện robot qua hình ảnh NASA và trả lời câu hỏi về sứ mệnh.</p></div>", unsafe_allow_html=True)
            if st.button(tx(language, "BẮT ĐẦU ROBOT MEMORY", "START ROBOT MEMORY"), use_container_width=True):
                reset_memory(); st.rerun()
        with b:
            st.markdown("<div class='training-panel'><h3>🌕 LUNAR BASE COMMAND</h3><p>Điều hành căn cứ Mặt Trăng, quản lý tài nguyên và đưa ra quyết định chiến thuật.</p></div>", unsafe_allow_html=True)
            if st.button(tx(language, "ĐIỀU HÀNH CĂN CỨ", "COMMAND THE BASE"), use_container_width=True):
                reset_base(); st.rerun()
        st.divider()
        show_leaderboard(language)

    elif stage == "memory":
        i = st.session_state.memory_round
        q = ROBOT_QUESTIONS[i]
        st.markdown(f"### 🤖 ROBOT MEMORY · {i + 1}/{len(ROBOT_QUESTIONS)}")
        st.progress((i + 1) / len(ROBOT_QUESTIONS))
        st.image(q["image"], use_container_width=True, caption=q["name"] + " · NASA mission image")
        st.markdown(f"<div class='question-box'><p>MISSION KNOWLEDGE CHECK</p><h2>{tx(language, q['q_vi'], q['q_en'])}</h2></div>", unsafe_allow_html=True)
        opts = q["opts_vi"] if language == "VI" else q["opts_en"]
        selected = st.radio(tx(language, "Chọn một đáp án:", "Choose one answer:"), opts, key=f"robot_answer_{i}")
        if st.button(tx(language, "XÁC NHẬN ĐÁP ÁN", "SUBMIT ANSWER"), key=f"robot_submit_{i}", use_container_width=True):
            if opts.index(selected) == q["answer"]:
                st.session_state.memory_score += 1
                if i == len(ROBOT_QUESTIONS) - 1:
                    score = round(st.session_state.memory_score / len(ROBOT_QUESTIONS) * 100)
                    add_leaderboard("ROBOT MEMORY", score, "MISSION PASSED")
                    st.session_state.training_stage = "memory_won"
                else:
                    st.session_state.memory_round += 1
                st.rerun()
            else:
                st.session_state.memory_failed = i
                st.session_state.training_stage = "memory_archive"
                st.rerun()

    elif stage == "memory_archive":
        st.error(tx(language, "Chưa hoàn thành! Đọc hồ sơ trước khi mở khóa lượt phục thù.", "Not complete! Review the archive before unlocking revenge."))
        st.markdown("## 📚 " + tx(language, "HỒ SƠ ROBOT", "ROVER ARCHIVE"))
        for i, q in enumerate(ROBOT_QUESTIONS):
            with st.expander(q["name"], expanded=(i == st.session_state.memory_failed)):
                st.image(q["image"], use_container_width=True)
                st.write(tx(language, q["fact_vi"], q["fact_en"]))
                st.checkbox(tx(language, "Tôi đã đọc và hiểu", "I have read and understood"), key=f"memory_read_{i}")
        if all(st.session_state.get(f"memory_read_{i}", False) for i in range(3)):
            st.success(tx(language, "ĐÃ MỞ KHÓA REVENGE PROTOCOL!", "REVENGE PROTOCOL UNLOCKED!"))
            if st.button(tx(language, "🔥 CHƠI LẠI ĐỂ PHỤC THÙ", "🔥 PLAY AGAIN — REVENGE"), use_container_width=True):
                for i in range(3): st.session_state.pop(f"memory_read_{i}", None)
                reset_memory(); st.rerun()

    elif stage == "memory_won":
        st.markdown("<div class='ending-card'><h1>🏅 ROBOT MEMORY CLEARED</h1><h2>EXPLORER KNOWLEDGE BADGE</h2></div>", unsafe_allow_html=True)
        st.write(tx(language, f"Bạn trả lời đúng {st.session_state.memory_score}/3 câu.", f"You answered {st.session_state.memory_score}/3 questions correctly."))
        show_leaderboard(language)
        if st.button(tx(language, "VỀ TRUNG TÂM HUẤN LUYỆN", "BACK TO TRAINING CENTER"), use_container_width=True):
            st.session_state.training_stage = "menu"; st.rerun()

    elif stage == "base":
        i = st.session_state.base_round
        if st.session_state.get("base_event_round") != i:
            st.session_state.base_event_round = i
            st.session_state.base_natural_event = random.choice(["DUST", "METEOR", "ECLIPSE", "THERMAL", "MICRO"])
            event_costs = {"DUST": {"power": -6}, "METEOR": {"fuel": -2}, "ECLIPSE": {"power": -10}, "THERMAL": {"power": -5, "fuel": -3}, "MICRO": {"hull": -4}}
            for resource, change in event_costs[st.session_state.base_natural_event].items():
                st.session_state.base_resources[resource] = max(0, min(100, st.session_state.base_resources[resource] + change))
        render_base_scene(language, st.session_state.get("base_natural_event", "DUST"))
        render_resources(st.session_state.base_resources)
        event = BASE_ROUNDS[i]
        st.markdown(f"### 🌑 {tx(language, event['title_vi'], event['title_en'])} · {i + 1}/5")
        st.progress((i + 1) / 5)
        st.markdown(f"<div class='question-box'><p>MISSION CONTROL · DECISION {i + 1}</p><h2>{tx(language, event['story_vi'], event['story_en'])}</h2></div>", unsafe_allow_html=True)
        st.markdown("### 📊 " + tx(language, "BẢNG TRAO ĐỔI TÀI NGUYÊN", "RESOURCE TRADE-OFF TABLES"))
        st.caption(tx(language, "Mở từng bảng để xem tài nguyên sẽ mất hoặc nhận trước khi quyết định.", "Open each panel to inspect resource costs and gains before deciding."))
        resource_names = {"oxygen": "Oxy", "power": "Điện", "water": "Nước", "food": "Lương thực", "fuel": "Nhiên liệu", "hull": "Độ bền"}
        if language == "EN":
            resource_names = {"oxygen": "Oxygen", "power": "Power", "water": "Water", "food": "Food", "fuel": "Fuel", "hull": "Integrity"}
        for n, (name, description, delta, points) in enumerate(event["choices"]):
            with st.expander(f"PHƯƠNG ÁN {n + 1} · {name}  |  {tx(language, 'Điểm chiến thuật', 'Strategy points')}: +{points}", expanded=(n == 0)):
                st.write(description)
                changes = [{"Tài nguyên" if language == "VI" else "Resource": resource_names[k],
                            "Thay đổi" if language == "VI" else "Change": f"{v:+d}",
                            "Sau quyết định" if language == "VI" else "After choice": f"{max(0, min(100, st.session_state.base_resources.get(k, 0) + v))}%"}
                           for k, v in delta.items()]
                st.table(changes)
        choice_labels = [f"{n + 1}. {item[0]} — {item[1]}" for n, item in enumerate(event["choices"])]
        chosen = st.radio(tx(language, "⚡ CHỌN PHƯƠNG ÁN ĐIỀU HÀNH — ĐỌC KỸ CHI PHÍ:", "⚡ SELECT A COMMAND — REVIEW THE COSTS:"), choice_labels, key=f"base_choice_{i}")
        check = STRATEGY_CHECKS[i]
        st.markdown(f"<div class='question-box'><p>🧠 STRATEGY CHECK · BONUS QUESTION</p><h2>{tx(language, check['q_vi'], check['q_en'])}</h2></div>", unsafe_allow_html=True)
        check_opts = check["opts_vi"] if language == "VI" else check["opts_en"]
        strategy_answer = st.radio(tx(language, "Câu hỏi tư duy bổ sung:", "Additional strategy question:"), check_opts, key=f"strategy_check_{i}")
        if st.button(tx(language, "XÁC NHẬN QUYẾT ĐỊNH", "CONFIRM DECISION"), key=f"base_confirm_{i}", use_container_width=True):
            choice_index = choice_labels.index(chosen)
            name, description, delta, points = event["choices"][choice_index]
            for key, amount in delta.items():
                st.session_state.base_resources[key] = max(0, min(100, st.session_state.base_resources.get(key, 0) + amount))
            st.session_state.base_points += points
            if check_opts.index(strategy_answer) == check["answer"]:
                st.session_state.base_points += 3
                st.toast(tx(language, "Chính xác! +3 điểm tư duy", "Correct! +3 strategy points"), icon="🧠")
            else:
                st.session_state.base_points = max(0, st.session_state.base_points - 1)
            st.session_state.base_log.append(name + (" | Bonus: +3" if check_opts.index(strategy_answer) == check["answer"] else " | Bonus: 0"))
            if i == 4:
                ending_index, score = choose_ending(st.session_state.base_resources, st.session_state.base_points)
                st.session_state.base_ending = ending_index
                st.session_state.base_final_score = score
                add_leaderboard("LUNAR BASE COMMAND", score, ENDINGS[ending_index][0])
                st.session_state.training_stage = "base_ending"
            else:
                st.session_state.base_round += 1
            st.rerun()

    elif stage == "base_ending":
        render_base_scene(language, st.session_state.get("base_natural_event", "DUST"))
        render_resources(st.session_state.base_resources)
        idx = st.session_state.base_ending
        title_vi, desc_vi, title_en = ENDINGS[idx]
        st.markdown(f"<div class='ending-card'><p style='letter-spacing:4px;color:#85bdff'>MISSION RESULT · ENDING {idx + 1:02d}/20</p><h1 style='color:#fff'>{'🏆' if idx < 6 else '🛰️' if idx < 13 else '⚠️'} {tx(language, title_vi, title_en)}</h1><h2 style='color:#9bcaff'>{st.session_state.base_final_score}/100</h2><p style='font-size:17px;color:#d2e2f5'>{tx(language, desc_vi, ENDING_DESCRIPTIONS_EN[idx])}</p></div>", unsafe_allow_html=True)
        st.markdown("### " + tx(language, "NHẬT KÝ QUYẾT ĐỊNH", "DECISION LOG"))
        for n, command in enumerate(st.session_state.base_log, 1):
            st.write(f"**{n}.** {command}")
        show_leaderboard(language)
        left, right = st.columns(2)
        with left:
            if st.button(tx(language, "🔁 CHƠI LẠI CĂN CỨ", "🔁 REPLAY BASE MISSION"), use_container_width=True):
                reset_base(); st.rerun()
        with right:
            if st.button(tx(language, "VỀ TRUNG TÂM", "BACK TO TRAINING CENTER"), use_container_width=True):
                st.session_state.training_stage = "menu"; st.rerun()

