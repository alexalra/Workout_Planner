
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rule-Based Workout Planner", page_icon="⚙️", layout="centered")

st.title("⚙️ Rule-Based Workout Planner")
st.write("An automated engine executing a workout plan.")

# 1. DATA IMPORT
try:
    loaded_df = pd.read_csv("Exercises.csv")
    
    # Standardize column naming 
    loaded_df.columns = [col.strip().replace(" ", "_").title() for col in loaded_df.columns]
    
    # Filter only active exercises
    df = loaded_df[loaded_df["Is_Active"] == 1]

except FileNotFoundError:
    st.error("❌ **Data File Error:** Could not locate 'Exercises.csv' in this folder.")
    st.stop()

# 2. CONTROL PANEL on the left for user input
st.sidebar.header("⚙️ Set Configurations")
selected_day = st.sidebar.selectbox("Select Training Day:", [1, 2, 3], format_func=lambda x: f"Day {x}")
selected_week = st.sidebar.selectbox("Select Microcycle Week:", [1, 2], format_func=lambda x: f"Week {x}")


# 3. THE CRITERIA FILTER ENGINE  

# Exercises for the selected day and week
day_pool = df[(df["Day"] == selected_day) & (df["Week"].astype(str).isin([str(selected_week), "All"]))]

st.subheader(f"📋 Validated Output Card: Day {selected_day} (Week {selected_week})")
st.markdown("---")

unique_steps = sorted(day_pool["Exercise_Nr"].unique())

for step in unique_steps:
    step_items = day_pool[day_pool["Exercise_Nr"] == step]

    st.markdown(f"### Block {int(step)}")
    
    # Loop and print whatever is assigned to this exact number step
    for _, row in step_items.iterrows():
        # Clean string structures 
        exercise_name = str(row['Exercise']).strip()
        exercise_type = str(row['Type']).strip()
        muscle_group = str(row['Muscle_Group']).strip()
        
        st.write(f"🔹 **{exercise_name}** — *{exercise_type}* ({muscle_group})")
    
    st.markdown(" ")

# 4. DATA COMPLIANCE -- small tests

st.markdown("---")
st.subheader("📊 Spreadsheet Rule-Compliance Verification")

# Rule Test 1: Daily Plyo Check
has_plyo = not day_pool[day_pool["Type"] == "Plyometric"].empty
if has_plyo:
    st.write("✅ **Rule: Daily Plyometric Check:** Passed for this selection.")
else:
    st.write("❌ **Rule: Daily Plyometric Check:** Failed! This spreadsheet day is missing a Plyometric warmup.")

# Rule Test 2: Heavy Carry Check
has_carry_day = not day_pool[day_pool["Type"].str.contains("Heavy carries")].empty
if has_carry_day:
    st.write("✅ **Rule: Daily Heavy Carry Check:** Passed. Heavy carries exist for this day.")
else:
    st.write("❌ **Rule: Daily Heavy Carry Check:** Failed! No Heavy Carries found for this day.")

# Rule Test 3: Leg Day Stability Check
if selected_day == 1:
    has_stability = not day_pool[day_pool["Type"].isin(["Balance", "Stability"])].empty
    if has_stability:
        st.write("✅ **Rule: Leg Day Stability Check:** Passed.")
    else:
        st.write("❌ **Rule: Leg Day Stability Check:** Failed! No balance/stability exercise found for this Leg week.")
