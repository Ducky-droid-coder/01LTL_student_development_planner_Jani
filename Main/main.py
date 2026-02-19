import streamlit as st
import json
import os

st.set_page_config(page_title="Student Development Planner", layout="centered")

DATA_FILE = "data.json"


# ---------- JSON Helpers ----------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------- UI ----------

st.title("📘 Student Development Planner")

st.subheader("Add New Entry")

name = st.text_input("Student Name")
goal = st.text_area("Development Goal")

if st.button("Save Entry"):
    if name and goal:
        data = load_data()
        new_entry = {
            "name": name,
            "goal": goal
        }
        data.append(new_entry)
        save_data(data)
        st.success("Entry saved successfully!")
    else:
        st.warning("Please fill in all fields.")


st.subheader("Saved Entries")

data = load_data()

if data:
    for entry in data:
        st.markdown(f"**Name:** {entry['name']}")
        st.markdown(f"**Goal:** {entry['goal']}")
        st.divider()
else:
    st.info("No entries yet.")
