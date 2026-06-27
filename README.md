# 🏋️‍♂️ Workout Planner & Dashboard

A lightweight, automated Streamlit dashboard to manage and dynamically display my biweekly workout routines based on structured planning data.

---

## Project Overview
The goal of this project is to provide a clean, visual interface for my workout routine. I prefer to keep my training consistent but enjoy implementing slight variations every two weeks. This app handles those dynamic updates automatically so I don't have to track them manually.

Most of the structural planning and exercise pools are managed via the `Exercises.csv` table. 

---

## Planned Features
* **Max Load & Progress Tracking:** Incorporate data inputs to log maximum weight loads for specific focus exercises.
* **Progressive Overload Metrics:** Generate progress charts over time to visualize gains.

---

## Workout Split

The routine follows a 3-day targeted split:
* **Day 1:** Legs
* **Day 2:** Back / Shoulders / Arms focus
* **Day 3:** Chest / Shoulders / Arms focus

---

## Rule-Compliance Criteria
The app features built-in automated test scripts to scan the spreadsheet data and verify that the routine satisfies the following strict programming constraints:

### Frequency Rules
* **Daily Heavy Carry:** At least one carrier exercise must be programmed per day.
* **Daily Plyometrics:** Every single day must contain a plyometric  exercise.
* **Leg Day Stability:** Leg day must contain at least 1 stability exercise per week.

### Exercise Ordering Rules
1. **Plyometrics First:** Plyometric exercises must always be the very first movement in the sequence.
2. **Stability Positioning:** Stability exercises must also come at the beginning. They can be superset *with* plyometrics, but the plyometric exercise must still remain first in order.
3. **Finishing with Carries:** Heavy Carries are strictly reserved as the final exercises of the session.

---

## How to Run Locally

1. **Install dependencies:**
   ```bash
   python3 -m pip install streamlit pandas

2. **Launch the app:**
   ```bash
   streamlit run Planner.py

3. **To see it in your phone:** Connect directly with Streamlit Community Cloud platform via GitHub.
