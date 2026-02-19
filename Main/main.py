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

# ===============================
# FILTER SECTION
# ===============================

with st.container():
    st.markdown("### ")

    # --- Row 1 ---
    col1, col2, col3 = st.columns([4, 4, 1])

    with col1:
        selected_class = st.selectbox(
            "Filter by class",
            ["All classes", "Computer Science L3.1", "Computer Science L1", "Python L1"]
        )

    with col2:
        selected_subject = st.selectbox(
            "Filter by subject",
            ["All subjects", "Computer Science Level 3.1", "Computer Science Level 1", "Python Level 1"]
        )

    with col3:
        st.write("")  # spacing
        st.write("")
        st.button("Clear", use_container_width=True)

    # --- Row 2 ---
    col4, col5, col6 = st.columns([4, 3, 3])

    with col4:
        search_student = st.text_input(
            "Search students",
            placeholder="Search by name..."
        )

    with col5:
        selected_grade = st.selectbox(
            "Filter by grade",
            ["All grades", "Grade 4", "Grade 5", "Grade 7"]
        )

    with col6:
        selected_school = st.selectbox(
            "Filter by school",
            ["All schools", "Lincoln Elementary", "Riverside Middle School"]
        )

# ===============================
# SUMMARY CARDS
# ===============================

st.markdown("### ")

card1, card2, card3 = st.columns(3)

# --- Card Styling ---
st.markdown("""
    <style>
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #e6e6e6;
        }
        .card-title {
            font-size: 14px;
            color: #6c757d;
        }
        .card-value {
            font-size: 28px;
            font-weight: 700;
        }
        .card-subtext {
            font-size: 12px;
            color: #6c757d;
        }
    </style>
""", unsafe_allow_html=True)

with card1:
    st.markdown("""
        <div class="card">
            <div class="card-title">Total Students</div>
            <div class="card-value">0</div>
            <div class="card-subtext">Current total</div>
        </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
        <div class="card">
            <div class="card-title">This Month</div>
            <div class="card-value">0 students</div>
            <div class="card-subtext">Active students this month</div>
        </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
        <div class="card">
            <div class="card-title">Recent Notes</div>
            <div class="card-value">0 notes</div>
            <div class="card-subtext">Total notes for this student</div>
        </div>
    """, unsafe_allow_html=True)
