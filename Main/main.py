import streamlit as st

st.set_page_config(
    page_title="LTL Pathfinder",
    layout="wide"
)

# --- Global Button Styling ---
st.markdown("""
    <style>
    div.stButton > button {
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Layout ---
left, right = st.columns([3, 7])

with left:
    st.markdown(
        "<h2 style='margin-top:10px;'>LTL Pathfinder</h2>",
        unsafe_allow_html=True
    )

with right:
    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.button("Categories", use_container_width=True)
    c2.button("Delete All", use_container_width=True)
    c3.button("Admin", use_container_width=True)

    c4.button("Add Student", type="primary", use_container_width=True)
    c5.button("AI Guide", type="primary", use_container_width=True)
    c6.button("Export", type="primary", use_container_width=True)

st.divider()
