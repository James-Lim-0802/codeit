# import streamlit as st

# st.image("ruler.png")
# st.title("단위변환기")
# st.header("길이")
# input = st.number_input("cm", value = 10.00)
# st.header("바꿀 단위")
# unit = st.selectbox("단위", ["mm", "inch"])
# st.button("변환하기")
# st.header("바꾼 길이")
# if input:
#     if unit == "mm":
#         result = input * 10
#     elif unit == "inch":
#         result = input * 0.38
#     st.write(f"{result} {unit}")


# import streamlit as st

# value1 = st.data_editor([
#     "도윤",
#     "하빈",
#     "유하"
# ])
# st.write(value1)

# value2 = st.data_editor([
#   { "메뉴": "아이스커피", "가격": 4500 },
#   { "메뉴": "카페 모카", "가격": 5000 },
#   { "메뉴": "녹차", "가격": 5000 },
# ])
# st.write(value2)

# import streamlit as st

# data1 = [10, 25, 30, 40, 55]
# st.bar_chart(data1, x_label="게임 시간", y_label="경험치")

# data2 = [
#     {
#         "날짜": "2025-01",
#         "경험치": 10,
#         "특수 경험치": 2,
#     },
#     {
#         "날짜": "2025-02",
#         "경험치": 15,
#         "특수 경험치": 4,
#     },
#     {
#         "날짜": "2025-03",
#         "경험치": 30,
#         "특수 경험치": 10,
#     },
#     {
#         "날짜": "2025-04",
#         "경험치": 40,
#         "특수 경험치": 15,
#     }
# ]
# st.bar_chart(data2, x="날짜", y=["경험치", "특수 경험치"], stack=True)

# import streamlit as st

# data1 = [10, 25, 30, 40, 55]

# st.line_chart(data1, x_label="게임 시간", y_label="경험치")

# data2 = [
#     {
#         "날짜": "2025-01",
#         "경험치": 10,
#         "체력": 100,
#     },
#     {
#         "날짜": "2025-02",
#         "경험치": 15,
#         "체력": 200
#     },
#     {
#         "날짜": "2025-03",
#         "경험치": 30,
#         "체력": 250,
#     },
#     {
#         "날짜": "2025-04",
#         "경험치": 40,
#         "체력": 300,
#     }
# ]

# st.line_chart(data2, x="날짜", y=["경험치", "체력"])

# import streamlit as st
# data = [
#     {
#         "날짜": "2024-01",
#         "평균 기온": -0.5,
#         "평균 최저 기온": -3.9,
#         "평균 최고 기온": 3.6
#     },
#     {
#         "날짜": "2024-02",
#         "평균 기온": 3.8,
#         "평균 최저 기온": 0.2,
#         "평균 최고 기온": 8.2
#     },
#     {
#         "날짜": "2024-03",
#         "평균 기온": 7,
#         "평균 최저 기온": 2.4,
#         "평균 최고 기온": 12
#     },
#     {
#         "날짜": "2024-04",
#         "평균 기온": 16.3,
#         "평균 최저 기온": 11.5,
#         "평균 최고 기온": 22.4
#     },
#     {
#         "날짜": "2024-05",
#         "평균 기온": 18.5,
#         "평균 최저 기온": 13.8,
#         "평균 최고 기온": 23.7
#     },
#     {
#         "날짜": "2024-06",
#         "평균 기온": 24.6,
#         "평균 최저 기온": 19.9,
#         "평균 최고 기온": 30.1
#     },
#     {
#         "날짜": "2024-07",
#         "평균 기온": 26.6,
#         "평균 최저 기온": 24.1,
#         "평균 최고 기온": 29.6
#     },
#     {
#         "날짜": "2024-08",
#         "평균 기온": 29.3,
#         "평균 최저 기온": 26.3,
#         "평균 최고 기온": 33.3
#     },
#     {
#         "날짜": "2024-09",
#         "평균 기온": 25.5,
#         "평균 최저 기온": 22,
#         "평균 최고 기온": 29.8
#     },
#     {
#         "날짜": "2024-10",
#         "평균 기온": 16.7,
#         "평균 최저 기온": 12.7,
#         "평균 최고 기온": 21.4
#     },
#     {
#         "날짜": "2024-11",
#         "평균 기온": 9.7,
#         "평균 최저 기온": 5.5,
#         "평균 최고 기온": 14.9
#     },
#     {
#         "날짜": "2024-12",
#         "평균 기온": 0.8,
#         "평균 최저 기온": -2.9,
#         "평균 최고 기온": 5.3
#     }
#     ]
# st.header("2024년 서울 날씨")
# st.line_chart(data, x="날짜", y=["평균 기온", "평균 최저 기온", "평균 최고 기온"], y_label = "기온")


# import streamlit as st

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("제목1")
#     st.text("column 1")

# with col2:
#     st.header("제목2")
#     st.text("column 2")
#     st.button("확인")

# with col3:
#     st.header("제목3")
#     st.text("column 3")

# import streamlit as st

# tab1, tab2, tab3 = st.tabs(["Python", "Streamlit", "Pandas"])

# with tab1:
#     st.header("Python")
#     st.text("I ❤️ Python")
# with tab2:
#     st.header("Streamlit")
#     st.text("I ❤️ Streamlit")
# with tab3:
#     st.header("Pandas")
#     st.text("I ❤️ Pandas")


import streamlit as st

if "number" not in st.session_state:
    st.session_state["number"] = 1
st.text(st.session_state["number"])

clicked = st.button("더하기")
if clicked:
    st.session_state["number"] += 1
    st.rerun()