
import streamlit as st

def show_moon_timeline(language="VI"):

    if language == "VI":
        title = "HỒ SƠ DI SẢN MẶT TRĂNG"
        subtitle = "MỖI THIẾT BỊ ĐỀU CÓ MỘT CÂU CHUYỆN ĐÁNG ĐƯỢC GHI NHỚ"
        intro = "Hãy khám phá những cỗ máy từng rời Trái Đất, hoàn thành sứ mệnh và để lại dấu tích trên Mặt Trăng."
        labels = {
            "mission": "NHIỆM VỤ",
            "journey": "HÀNH TRÌNH",
            "fact": "ĐIỀU THÚ VỊ",
            "fate": "SỐ PHẬN CUỐI CÙNG",
            "type": "LOẠI THIẾT BỊ",
            "date": "THỜI GIAN",
            "status": "TRẠNG THÁI",
            "open": "MỞ HỒ SƠ CHI TIẾT",
            "count": "HỒ SƠ ĐƯỢC GIỚI THIỆU",
            "note": "LƯU Ý",
            "note_text": "Lunar Reconnaissance Orbiter vẫn đang hoạt động. Thiết bị này được đưa vào để so sánh với các sứ mệnh trước đó, không phải phần cứng đã bị bỏ lại."
        }

        missions = [
            {
                "year": "1964",
                "name": "RANGER 7",
                "type": "Tàu thăm dò va chạm",
                "status": "Đã kết thúc nhiệm vụ · Va chạm xuống Mặt Trăng",
                "mission": "Chụp ảnh cận cảnh bề mặt Mặt Trăng và truyền dữ liệu về Trái Đất trước khi va chạm. Những hình ảnh này giúp các nhà khoa học đánh giá địa hình và tìm hiểu khả năng hạ cánh của tàu có người lái.",
                "journey": "Ranger 7 được phóng ngày 28/7/1964. Ngày 31/7/1964, khi tiếp cận Mặt Trăng, hệ thống camera bắt đầu gửi hình ảnh về Trái Đất. Trong khoảng 17 phút cuối cùng, tàu liên tục truyền ảnh trước khi va chạm xuống khu vực Sea of Clouds.",
                "fact": "Ranger 7 gửi về 4.316 hình ảnh. Bức ảnh cuối cùng được truyền về chỉ khoảng 2,3 giây trước khi tàu va chạm. Đây là thành công đầu tiên của Mỹ trong chương trình tàu thăm dò va chạm Mặt Trăng sau một chuỗi thất bại trước đó.",
                "fate": "Ranger 7 đã va chạm xuống Mặt Trăng theo đúng thiết kế. Nó không thể trở về Trái Đất, nhưng những hình ảnh cuối cùng đã trở thành nguồn dữ liệu quan trọng cho các chương trình thám hiểm tiếp theo.",
                "highlight": "4.316 HÌNH ẢNH",
                "highlight_text": "Được truyền về trước khi va chạm."
            },
            {
                "year": "1966",
                "name": "LUNAR ORBITER 1",
                "type": "Tàu quỹ đạo",
                "status": "Đã kết thúc nhiệm vụ · Va chạm xuống Mặt Trăng",
                "mission": "Chụp ảnh và khảo sát bề mặt Mặt Trăng nhằm tìm kiếm những địa điểm phù hợp cho các chuyến hạ cánh của tàu Surveyor và phi hành gia Apollo.",
                "journey": "Được phóng ngày 10/8/1966, Lunar Orbiter 1 đi vào quỹ đạo Mặt Trăng ngày 14/8. Tàu chụp ảnh các khu vực dự kiến hạ cánh, đồng thời khảo sát những vùng khác trên bề mặt Mặt Trăng.",
                "fact": "Lunar Orbiter 1 là tàu vũ trụ đầu tiên của Mỹ bay vào quỹ đạo Mặt Trăng. Nó còn ghi lại bức ảnh đầu tiên chụp Trái Đất từ khu vực gần Mặt Trăng.",
                "fate": "Sau khi hoàn thành nhiệm vụ chính, tàu được điều khiển va chạm xuống Mặt Trăng ngày 29/10/1966. Việc này giúp tránh gây nhiễu cho những tàu Lunar Orbiter tiếp theo.",
                "highlight": "BỨC ẢNH TRÁI ĐẤT",
                "highlight_text": "Được chụp từ khu vực gần Mặt Trăng."
            },
            {
                "year": "1966",
                "name": "SURVEYOR 1",
                "type": "Tàu đổ bộ",
                "status": "Đã kết thúc nhiệm vụ · Nằm lại trên Mặt Trăng",
                "mission": "Thực hiện cú hạ cánh mềm thành công để kiểm tra khả năng chịu lực của đất Mặt Trăng, chụp ảnh bề mặt và cung cấp dữ liệu phục vụ các chuyến đổ bộ có người lái.",
                "journey": "Surveyor 1 được phóng ngày 30/5/1966 và hạ cánh mềm xuống khu vực Ocean of Storms ngày 2/6/1966. Tàu sử dụng động cơ và hệ thống điều khiển để giảm tốc trước khi chạm xuống bề mặt.",
                "fact": "Surveyor 1 truyền về hơn 11.000 hình ảnh. Đây là lần đầu tiên một tàu vũ trụ Mỹ thực hiện thành công cú hạ cánh mềm trên Mặt Trăng.",
                "fate": "Nhiệm vụ chính kết thúc ngày 14/7/1966. NASA tiếp tục liên lạc với tàu đến ngày 7/1/1967. Sau đó, Surveyor 1 im lặng và nằm lại trên bề mặt Mặt Trăng.",
                "highlight": "11.240 HÌNH ẢNH",
                "highlight_text": "Một bước tiến lớn trong công nghệ hạ cánh."
            },
            {
                "year": "1967",
                "name": "SURVEYOR 3",
                "type": "Tàu đổ bộ",
                "status": "Đã kết thúc nhiệm vụ · Một số bộ phận được đưa về Trái Đất",
                "mission": "Nghiên cứu đất Mặt Trăng bằng camera và cánh tay lấy mẫu. Các thí nghiệm giúp xác định đặc điểm của đất và khả năng chịu lực của bề mặt.",
                "journey": "Surveyor 3 hạ cánh xuống khu vực Ocean of Storms vào tháng 4/1967. Tàu sử dụng thiết bị lấy mẫu để đào rãnh, kiểm tra đất và gửi hình ảnh về Trái Đất.",
                "fact": "Đây là một trong những thiết bị đặc biệt nhất trong lịch sử khám phá Mặt Trăng. Năm 1969, phi hành gia Apollo 12 đã hạ cánh gần Surveyor 3, đi bộ đến thăm nó và tháo một số bộ phận mang về Trái Đất.",
                "fate": "Surveyor 3 ngừng liên lạc vào tháng 5/1967. Hơn hai năm sau, camera và một số bộ phận của nó được đưa về Trái Đất để nghiên cứu ảnh hưởng của môi trường Mặt Trăng.",
                "highlight": "ĐƯỢC CON NGƯỜI GHÉ THĂM",
                "highlight_text": "Apollo 12 đã đến kiểm tra thiết bị vào năm 1969."
            },
            {
                "year": "2009",
                "name": "LUNAR RECONNAISSANCE ORBITER",
                "type": "Tàu quỹ đạo",
                "status": "Đang hoạt động · Không phải thiết bị bị bỏ lại",
                "mission": "Lập bản đồ chi tiết bề mặt Mặt Trăng, nghiên cứu nhiệt độ, thành phần và môi trường bức xạ. Dữ liệu giúp lựa chọn địa điểm phù hợp cho những chuyến thám hiểm tương lai.",
                "journey": "LRO được phóng ngày 18/6/2009 và đi vào quỹ đạo Mặt Trăng ngày 23/6/2009. Ban đầu, nhiệm vụ chính được dự kiến kéo dài khoảng một năm, nhưng tàu tiếp tục hoạt động vượt xa thời gian dự kiến.",
                "fact": "LRO đã giúp lập bản đồ Mặt Trăng với độ chi tiết cao, hỗ trợ các nhà khoa học nghiên cứu những khu vực có thể chứa băng nước gần hai cực.",
                "fate": "Khác với các thiết bị trong những hồ sơ trước, LRO vẫn là một sứ mệnh hoạt động. Nó được đưa vào đây như một ví dụ về sự phát triển của công nghệ khám phá Mặt Trăng.",
                "highlight": "TỪ NĂM 2009",
                "highlight_text": "Tiếp tục quan sát và nghiên cứu Mặt Trăng."
            }
        ]

    else:
        title = "LUNAR HERITAGE ARCHIVES"
        subtitle = "EVERY MACHINE HAS A STORY WORTH REMEMBERING"
        intro = "Explore the machines that left Earth, completed their missions and left traces on the Moon."
        labels = {
            "mission": "MISSION",
            "journey": "JOURNEY",
            "fact": "DID YOU KNOW?",
            "fate": "FINAL FATE",
            "type": "HARDWARE TYPE",
            "date": "DATE",
            "status": "STATUS",
            "open": "OPEN FULL MISSION FILE",
            "count": "FEATURED MISSION FILES",
            "note": "IMPORTANT NOTE",
            "note_text": "Lunar Reconnaissance Orbiter is still active. It is included for comparison, not as abandoned hardware."
        }

        missions = [
            {
                "year": "1964",
                "name": "RANGER 7",
                "type": "Impact probe",
                "status": "Mission completed · Impacted the Moon",
                "mission": "Photograph the lunar surface at close range and transmit images to Earth before impact. The images helped scientists assess the terrain and prepare for crewed lunar landings.",
                "journey": "Ranger 7 launched on July 28, 1964. On July 31, its cameras began transmitting images as it approached the Moon. During its final 17 minutes, the spacecraft sent pictures before impacting the Sea of Clouds region.",
                "fact": "Ranger 7 returned 4,316 images. Its final image was transmitted about 2.3 seconds before impact. It was the first successful U.S. lunar impact mission after a series of earlier failures.",
                "fate": "Ranger 7 intentionally impacted the Moon as designed. It never returned to Earth, but its final images became important data for later exploration missions.",
                "highlight": "4,316 IMAGES",
                "highlight_text": "Transmitted before lunar impact."
            },
            {
                "year": "1966",
                "name": "LUNAR ORBITER 1",
                "type": "Orbiter",
                "status": "Mission completed · Impacted the Moon",
                "mission": "Photograph and survey the lunar surface to identify potential landing sites for Surveyor spacecraft and Apollo astronauts.",
                "journey": "Launched on August 10, 1966, Lunar Orbiter 1 entered lunar orbit on August 14. It photographed potential landing sites and other areas of the Moon.",
                "fact": "Lunar Orbiter 1 was the first U.S. spacecraft to orbit the Moon. It also captured the first image of Earth from the vicinity of the Moon.",
                "fate": "After its primary mission, the spacecraft was commanded to impact the Moon on October 29, 1966, to prevent interference with later Lunar Orbiter missions.",
                "highlight": "EARTHRISE IMAGE",
                "highlight_text": "Captured from near the Moon."
            },
            {
                "year": "1966",
                "name": "SURVEYOR 1",
                "type": "Lunar lander",
                "status": "Mission completed · Remains on the Moon",
                "mission": "Make a successful soft landing, test the strength of lunar soil, photograph the surface and provide data for future crewed landings.",
                "journey": "Surveyor 1 launched on May 30, 1966, and made a soft landing in the Ocean of Storms on June 2. Its engines and control systems slowed the spacecraft before touchdown.",
                "fact": "Surveyor 1 transmitted more than 11,000 images. It was the first U.S. spacecraft to make a successful soft landing on the Moon.",
                "fate": "Its primary mission ended on July 14, 1966. NASA maintained contact until January 7, 1967. The spacecraft then fell silent and remained on the lunar surface.",
                "highlight": "11,240 IMAGES",
                "highlight_text": "A major step in lunar landing technology."
            },
            {
                "year": "1967",
                "name": "SURVEYOR 3",
                "type": "Lunar lander",
                "status": "Mission completed · Some parts returned to Earth",
                "mission": "Study lunar soil using a camera and surface sampler. Its experiments helped determine the characteristics and bearing strength of the lunar surface.",
                "journey": "Surveyor 3 landed in the Ocean of Storms in April 1967. It used its sampling device to dig trenches, test the soil and send images back to Earth.",
                "fact": "In 1969, Apollo 12 astronauts landed near Surveyor 3, walked over to it and removed several parts to bring back to Earth.",
                "fate": "Surveyor 3 stopped communicating in May 1967. More than two years later, its camera and other parts were returned to Earth to study the effects of the lunar environment.",
                "highlight": "VISITED BY ASTRONAUTS",
                "highlight_text": "Apollo 12 visited the spacecraft in 1969."
            },
            {
                "year": "2009",
                "name": "LUNAR RECONNAISSANCE ORBITER",
                "type": "Orbiter",
                "status": "Active mission · Not abandoned hardware",
                "mission": "Map the lunar surface in detail and study temperature, composition and radiation. Its data helps identify suitable locations for future exploration.",
                "journey": "LRO launched on June 18, 2009, and entered lunar orbit on June 23. Its primary mission was initially expected to last about one year, but the spacecraft continued operating far beyond that period.",
                "fact": "LRO has helped map the Moon in great detail and study areas near the poles that may contain water ice.",
                "fate": "Unlike the earlier spacecraft in this archive, LRO remains an active mission. It is included as an example of how lunar exploration technology has developed.",
                "highlight": "SINCE 2009",
                "highlight_text": "Continuing to observe and study the Moon."
            }
        ]

    st.markdown("""
    <style>
    .archive-title {
        font-size: 30px;
        font-weight: 800;
        letter-spacing: 3px;
        color: white;
        margin-top: 15px;
        margin-bottom: 12px;
    }

    .archive-subtitle {
        color: #69adff;
        font-size: 12px;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }

    .archive-intro {
        color: #b7c8e0;
        font-size: 15px;
        line-height: 1.8;
        margin-bottom: 30px;
    }

    .mission-year {
        font-size: 13px;
        color: #75baff;
        letter-spacing: 3px;
        font-weight: bold;
    }

    .mission-name {
        font-size: 21px;
        font-weight: bold;
        color: white;
        letter-spacing: 1px;
        margin: 5px 0;
    }

    .mission-type {
        color: #a9bad3;
        font-size: 13px;
    }

    .mission-highlight {
        color: #72baff;
        font-size: 17px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 12px;
    }

    .mission-highlight-text {
        color: #aabbd3;
        font-size: 12px;
    }

    .detail-label {
        color: #72baff;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 2px;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .detail-copy {
        color: #d0dced;
        font-size: 14px;
        line-height: 1.8;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="archive-title">{title}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="archive-subtitle">{subtitle}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="archive-intro">{intro}</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"**{len(missions)} {labels['count']}**")

    st.markdown("---")

    for mission in missions:

        with st.container(border=True):

            left, right = st.columns([3, 2])

            with left:
                st.markdown(
                    f'<div class="mission-year">{mission["year"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="mission-name">{mission["name"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="mission-type">{labels["type"]}: {mission["type"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="mission-highlight">{mission["highlight"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="mission-highlight-text">{mission["highlight_text"]}</div>',
                    unsafe_allow_html=True
                )

            with right:
                st.caption(labels["date"])
                st.markdown(f"**{mission['year']}**")
                st.caption(labels["status"])
                st.markdown(mission["status"])

            with st.expander(labels["open"]):

                st.markdown(
                    f'<div class="detail-label">{labels["mission"]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="detail-copy">{mission["mission"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="detail-label">{labels["journey"]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="detail-copy">{mission["journey"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="detail-label">{labels["fact"]}</div>',
                    unsafe_allow_html=True
                )
                st.info(mission["fact"], icon="💡")

                st.markdown(
                    f'<div class="detail-label">{labels["fate"]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="detail-copy">{mission["fate"]}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("")

    st.warning(labels["note_text"], icon="ℹ️")
