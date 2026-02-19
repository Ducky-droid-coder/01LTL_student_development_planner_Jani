import streamlit as st

st.set_page_config(
    page_title="LTL Pathfinder",
    layout="wide"
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .main-title {
            font-size: 32px;
            font-weight: 700;
            padding-top: 10px;
        }
        .top-button {
            margin-top: 20px;
        }
        div.stButton > button {
            border-radius: 8px;
            padding: 8px 16px;
        }
        .blue-btn button {
            background-color: #3b82f6;
            color: blue;
            border: none;
        }
        .blue-btn button:hover {
            background-color: #2563eb;
            color: blue;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header Layout ---
col1, col2 = st.columns([4, 6])

with col1:
    st.markdown('<div class="main-title">LTL Pathfinder</div>', unsafe_allow_html=True)

with col2:
    btn_cols = st.columns(6)

    btn_cols[0].button("Categories")
    btn_cols[1].button("Delete All")
    btn_cols[2].button("Admin")

    with btn_cols[3]:
        st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
        st.button("Add Student")
        st.markdown('</div>', unsafe_allow_html=True)

    with btn_cols[4]:
        st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
        st.button("AI Guide")
        st.markdown('</div>', unsafe_allow_html=True)

    with btn_cols[5]:
        st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
        st.button("Export")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
