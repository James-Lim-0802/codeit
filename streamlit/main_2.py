# import streamlit as st

# to_do_input = st.text_input("할 일")
# deadline_input = st.date_input("마감 기한")
# adding = st.button("추가하기")

# if "to_do_list" not in st.session_state:
#     st.session_state["to_do_list"] = []

# if "deadline_list" not in st.session_state:
#     st.session_state["deadline_list"] = []

# # 추가하기 버튼 클릭 시
# if adding and to_do_input and deadline_input:
#     st.session_state["to_do_list"].append(to_do_input)
#     st.session_state["deadline_list"].append(deadline_input)
#     st.rerun()

# if st.session_state["to_do_list"]:
#     data = [
#         {"할 일" : todo, "마감 기한": deadline}
#         for todo, deadline in zip(
#             st.session_state["to_do_list"],
#             st.session_state["deadline_list"]
#         )
#     ]
#     st.data_editor(data)


#Code It Interpretation
import streamlit as st

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

task = st.text_input("할 일")
duedate = st.date_input("마감 기한")
clicked = st.button("추가하기")
if clicked:
    st.session_state["tasks"].append({
        "할 일": task,
        "마감 기한": duedate,
    })
    st.rerun()

st.data_editor(st.session_state["tasks"]) #task 칼럼에 2개의 서브칼럼을 넣는구조구나