import streamlit as st

def show_archive_timeline(language="VI"):
    """Hiển thị các mục Kho Trữ: 2 mục 1 dòng, ảnh thu nhỏ gọn, khi bấm vào xem chi tiết sẽ có 2 ảnh riêng biệt cho Mặt Trăng và Sao Hỏa"""
    
    # CSS tùy chỉnh kích thước thẻ và hình ảnh gọn gàng
    st.markdown("""
    <style>
    .archive-card {
        background: #101a2c;
        border: 1px solid rgba(100, 160, 255, 0.3);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .archive-card:hover {
        border-color: #65aaff;
        box-shadow: 0 0 20px rgba(85, 165, 255, 0.3);
    }
    .archive-img-wrapper {
        width: 100%;
        height: 110px;
        border-radius: 6px;
        overflow: hidden;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #080d19;
    }
    .archive-img-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)

    data = {
        "VI": [
            {
                "id": "item_1",
                "title": "🛸 1. Tàu vũ trụ",
                "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "Đưa các sứ mệnh Apollo và robot hạ cánh xuống Mặt Trăng.",
                    "invented": "Năm 1957",
                    "used": "Thập niên 1960 (Apollo)",
                    "structure": "Khoang chỉ huy, module mặt trăng (LM), hệ thống phanh hãm quỹ đạo."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                    "important": "Vận chuyển tàu quỹ đạo và thiết bị thám hiểm hành tinh đỏ.",
                    "invented": "Năm 1960",
                    "used": "Thập niên 1964 (Mariner)",
                    "structure": "Tấm chắn nhiệt hành tinh, hệ thống dù siêu âm và phệ tời hạ cánh Sky Crane."
                },
                "link": "https://www.nasa.gov/mission_pages/station/main/index.html",
                "link_text": "Nguồn: NASA Spacecraft Overview"
            },
            {
                "id": "item_2",
                "title": "🤖 2. Robot thám hiểm",
                "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                    "important": "Xe tự hành nghiên cứu lớp bụi Regolith và địa hình tối trên Mặt Trăng (Lunokhod).",
                    "invented": "Năm 1970",
                    "used": "17/11/1970 (Lunokhod 1)",
                    "structure": "Khung bánh xe địa hình kim loại, pin năng lượng mặt trời và hệ thống camera điều khiển từ xa."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "Phòng thí nghiệm di động tìm kiếm dấu vết sự sống cổ đại (Curiosity, Perseverance).",
                    "invented": "Năm 1996",
                    "used": "04/07/1997",
                    "structure": "Hệ thống treo rocker-bogie, camera phân tích quang phổ tia laser và nguồn phát điện hạt nhân RTG."
                },
                "link": "https://science.nasa.gov/mission/mars-2020-perseverance/",
                "link_text": "Nguồn: NASA Mars Perseverance"
            },
            {
                "id": "item_3",
                "title": "🛰️ 3. Vệ tinh nhân tạo",
                "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                    "important": "Chụp bản đồ bề mặt và tìm kiếm băng nước ở các cực Mặt Trăng (Lunar Reconnaissance Orbiter).",
                    "invented": "Năm 1966",
                    "used": "Tháng 08/1966 (Lunar Orbiter 1)",
                    "structure": "Camera độ phân giải cao, máy đo độ cao bằng laser và hệ thống viễn thông quỹ đạo thấp."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                    "important": "Chuyển tiếp tín hiệu liên lạc cho các robot dưới mặt đất và chụp ảnh khí hậu Sao Hỏa.",
                    "invented": "Năm 1964",
                    "used": "Tháng 11/1964 (Mariner 4)",
                    "structure": "Antenna hướng cao, cảm biến khí quyển hồng ngoại và pin mặt trời hiệu suất cao."
                },
                "link": "https://www.nasa.gov/headquarters/library/find/bibliographies/earth-observing-satellites/",
                "link_text": "Nguồn: NASA Satellites"
            },
            {
                "id": "item_4",
                "title": "🔭 4. Kính thiên văn",
                "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                    "important": "Quan sát vũ trụ từ phía xa không bị ảnh hưởng bởi tầng khí quyển Trái Đất hoặc đặt trên trạm quỹ đạo mặt trăng.",
                    "invented": "Năm 1990",
                    "used": "24/04/1990",
                    "structure": "Gương phản xạ quang học siêu phẳng, cảm biến quang phổ và hệ thống ổn định con quay hồi chuyển."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                    "important": "Hỗ trợ quan sát hình ảnh thời tiết sao hỏa và các tiểu hành tinh lân cận quỹ đạo.",
                    "invented": "Năm 1990",
                    "used": "Thập niên 1990",
                    "structure": "Hệ thống ống kính hồng ngoại xa và thiết bị lọc bức xạ vũ trụ."
                },
                "link": "https://webb.nasa.gov/",
                "link_text": "Nguồn: NASA Telescopes"
            },
            {
                "id": "item_5",
                "title": "👩‍🚀 5. Trang phục",
                "image": "https://images.unsplash.com/photo-1517976487534-5f25626011e0?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1517976487534-5f25626011e0?w=800",
                    "important": "Bộ đồ Apollo A7L giúp phi hành gia đi lại trên bề mặt bụi bặm và trọng lực thấp của Mặt Trăng.",
                    "invented": "Năm 1968",
                    "used": "20/07/1969 (Apollo 11)",
                    "structure": "Nhiều lớp vải chống rách, hệ thống tản nhiệt nước tuần hoàn và balo dưỡng khí khép kín."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                    "important": "Mẫu trang phục thế hệ mới (AxEMU) thiết kế chịu được nhiệt độ khắc nghiệt và bão cát Sao Hỏa.",
                    "invented": "Năm 2020",
                    "used": "Thử nghiệm cho sứ mệnh Artemis & Mars tương lai",
                    "structure": "Khớp cử động linh hoạt bằng hợp kim titan, lớp chống bức xạ ion hóa và kính chắn tia cực tím cường độ cao."
                },
                "link": "https://www.nasa.gov/reference/spacesuits/",
                "link_text": "Nguồn: NASA Spacesuits"
            },
            {
                "id": "item_6",
                "title": "⚙️ 6. Công nghệ NASA",
                "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                    "important": "Công nghệ pin nhiên liệu hydro-oxy cung cấp điện và nước sạch cho các phi hành gia trên tàu Apollo.",
                    "invented": "Năm 1965",
                    "used": "Sứ mệnh Apollo",
                    "structure": "Màng lọc trao đổi ion, hệ thống tái chế nước tiểu thành nước uống và vật liệu cách nhiệt siêu nhẹ."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "Công nghệ lọc khí CO2 thành oxy (MOXIE trên tàu Perseverance) phục vụ căn cứ Sao Hỏa tương lai.",
                    "invented": "Năm 2014",
                    "used": "Năm 2021 (On Sao Hỏa)",
                    "structure": "Thiết bị điện phân oxit rắn, cảm biến áp suất khí quyển mỏng và vi mạch điều khiển tự động chịu nhiệt."
                },
                "link": "https://spinoff.nasa.gov/",
                "link_text": "Nguồn: NASA Spinoff"
            }
        ],
        "EN": [
            {
                "id": "item_1",
                "title": "🛸 1. Spacecraft",
                "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "Transported Apollo missions and lunar modules to the Moon.",
                    "invented": "1957",
                    "used": "1960s (Apollo)",
                    "structure": "Command module, lunar module (LM), and orbital braking systems."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                    "important": "Transported orbiters and exploratory equipment to the Red Planet.",
                    "invented": "1960",
                    "used": "1964 (Mariner)",
                    "structure": "Planetary heat shields, supersonic parachutes, and Sky Crane landing systems."
                },
                "link": "https://www.nasa.gov/mission_pages/station/main/index.html",
                "link_text": "Source: NASA Spacecraft"
            },
            {
                "id": "item_2",
                "title": "🤖 2. Robotic Explorers",
                "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                    "important": "Autonomous rovers studying lunar regolith and dark terrain (Lunokhod).",
                    "invented": "1970",
                    "used": "November 17, 1970",
                    "structure": "Metal mesh wheel chassis, solar panels, and remote control camera systems."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "Mobile laboratories searching for ancient microbial life (Curiosity, Perseverance).",
                    "invented": "1996",
                    "used": "July 4, 1997",
                    "structure": "Rocker-bogie suspension, laser spectrometry cameras, and RTG nuclear power sources."
                },
                "link": "https://science.nasa.gov/mission/mars-2020-perseverance/",
                "link_text": "Source: NASA Perseverance"
            },
            {
                "id": "item_3",
                "title": "🛰️ 3. Satellites",
                "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800",
                    "important": "Mapped lunar surfaces and searched for water ice at the poles (LRO).",
                    "invented": "1966",
                    "used": "August 1966",
                    "structure": "High-resolution cameras, laser altimeters, and low-orbit telecommunication arrays."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                    "important": "Relayed communications for ground rovers and monitored Martian climate.",
                    "invented": "1964",
                    "used": "November 1964",
                    "structure": "High-gain antennas, infrared atmospheric sensors, and high-efficiency solar panels."
                },
                "link": "https://www.nasa.gov/headquarters/library/find/bibliographies/earth-observing-satellites/",
                "link_text": "Source: NASA Satellites"
            },
            {
                "id": "item_4",
                "title": "🔭 4. Telescopes",
                "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800",
                    "important": "Observed the universe free from Earth's atmospheric distortion.",
                    "invented": "1990",
                    "used": "April 24, 1990",
                    "structure": "Ultra-flat optical reflecting mirrors, spectrographic sensors, and gyroscope stabilization."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                    "important": "Assisted in tracking Martian weather phenomena and nearby planetary orbits.",
                    "invented": "1990",
                    "used": "1990s",
                    "structure": "Far-infrared optical lenses and cosmic ray filtration equipment."
                },
                "link": "https://webb.nasa.gov/",
                "link_text": "Source: NASA Telescopes"
            },
            {
                "id": "item_5",
                "title": "👩‍🚀 5. Astronaut Suits",
                "image": "https://images.unsplash.com/photo-1517976487534-5f25626011e0?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1517976487534-5f25626011e0?w=800",
                    "important": "Apollo A7L suit allowed astronauts to walk on the dusty, low-gravity lunar surface.",
                    "invented": "1968",
                    "used": "July 20, 1969",
                    "structure": "Multi-layer tear-resistant fabrics, water-cooled thermal garment, and closed-circuit life support backpack."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=800",
                    "important": "Next-gen suits (AxEMU) engineered to withstand harsh Martian temperatures and dust storms.",
                    "invented": "2020",
                    "used": "Testing for Artemis & future Mars missions",
                    "structure": "Titanium alloy mobility joints, ionizing radiation shielding, and high-intensity UV visors."
                },
                "link": "https://www.nasa.gov/reference/spacesuits/",
                "link_text": "Source: NASA Spacesuits"
            },
            {
                "id": "item_6",
                "title": "⚙️ 6. NASA Technology",
                "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                "moon_info": {
                    "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
                    "important": "Hydrogen-oxygen fuel cell technology provided power and drinking water on Apollo missions.",
                    "invented": "1965",
                    "used": "Apollo Missions",
                    "structure": "Ion-exchange filtration membranes, urine-to-water recycling, and ultra-light insulation."
                },
                "mars_info": {
                    "image": "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800",
                    "important": "MOXIE device converts Martian atmospheric CO2 into breathable oxygen for future colonies.",
                    "invented": "2014",
                    "used": "2021 (On Mars)",
                    "structure": "Solid oxide electrolysis cells, thin atmospheric pressure sensors, and thermal micro-controllers."
                },
                "link": "https://spinoff.nasa.gov/",
                "link_text": "Source: NASA Spinoff"
            }
        ]
    }

    items = data.get(language, data["VI"])

    if "active_archive_modal" not in st.session_state:
        st.session_state.active_archive_modal = None

    # Hiển thị bảng chi tiết khi người dùng bấm xem mục
    if st.session_state.active_archive_modal:
        selected_item = next((i for i in items if i["id"] == st.session_state.active_archive_modal), None)
        
        if selected_item:
            with st.container():
                st.markdown(f"""
                <div style="background: #17294b; border: 2px solid #55a5ff; border-radius: 12px; padding: 20px; margin-bottom: 25px; box-shadow: 0 0 25px rgba(85,165,255,0.3);">
                    <h2 style="color: #ffffff; font-family: 'Orbitron', sans-serif; margin-bottom: 15px;">{selected_item['title']}</h2>
                """, unsafe_allow_html=True)
                
                # Nút Đóng (X)
                if st.button("❌ Đóng & Tiếp tục khám phá", key="close_modal_btn"):
                    st.session_state.active_archive_modal = None
                    st.rerun()

                # Bảng chia 2 phần: Mặt Trăng và Sao Hỏa (Mỗi phần có hình ảnh riêng biệt)
                col_moon, col_mars = st.columns(2, gap="medium")
                
                with col_moon:
                    st.markdown("### 🌕 Mặt Trăng (Moon)")
                    st.image(selected_item["moon_info"]["image"], use_container_width=True)
                    st.info(f"**📌 Thông tin:** {selected_item['moon_info']['important']}")
                    st.markdown(f"🗓️ **Phát minh:** {selected_item['moon_info']['invented']}")
                    st.markdown(f"🚀 **Sử dụng:** {selected_item['moon_info']['used']}")
                    st.markdown(f"🛠️ **Cấu tạo:** {selected_item['moon_info']['structure']}")
                    
                with col_mars:
                    st.markdown("### 🔴 Sao Hỏa (Mars)")
                    st.image(selected_item["mars_info"]["image"], use_container_width=True)
                    st.info(f"**📌 Thông tin:** {selected_item['mars_info']['important']}")
                    st.markdown(f"🗓️ **Phát minh:** {selected_item['mars_info']['invented']}")
                    st.markdown(f"🚀 **Sử dụng:** {selected_item['mars_info']['used']}")
                    st.markdown(f"🛠️ **Cấu tạo:** {selected_item['mars_info']['structure']}")

                # Đường link nguồn NASA
                st.markdown(
                    f"<div style='text-align: right; margin-top: 15px;'><a href='{selected_item['link']}' target='_blank' style='font-size: 12px; color: #38bdf8; text-decoration: none; background: rgba(56, 189, 248, 0.15); padding: 5px 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.4);'>🔗 {selected_item['link_text']}</a></div>", 
                    unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")
        return

    # Sắp xếp 2 mục trên 1 dòng ở giao diện chính
    for i in range(0, len(items), 2):
        cols = st.columns(2, gap="medium")
        for j in range(2):
            if i + j < len(items):
                item = items[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="archive-card">
                        <h4 style="color: #65aaff; font-family: 'Orbitron', sans-serif; font-size: 15px; margin-bottom: 8px;">{item['title']}</h4>
                        <div class="archive-img-wrapper">
                            <img src="{item['image']}" alt="{item['title']}">
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"🔍 Xem thông tin", key=f"btn_{item['id']}", use_container_width=True):
                        st.session_state.active_archive_modal = item["id"]
                        st.rerun()