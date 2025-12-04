
import streamlit as st
import json
from pathlib import Path

st.title("Stadium Explorer")

data_path = Path(__file__).parents[1] / "data" / "stadiums.json"
stadiums = json.loads(data_path.read_text(encoding="utf-8"))

years = sorted(set(s["world_cup_year"] for s in stadiums))
year = st.selectbox("Filter by World Cup year:", ["All"] + years)

if year == "All":
    filtered = stadiums
else:
    filtered = [s for s in stadiums if s["world_cup_year"] == year]

for s in filtered:
    with st.expander(f"{s['name']} ({s['world_cup_year']})"):
        st.write(f"**City:** {s['city']}, {s['country']}")
        st.write(f"**Capacity:** {s['capacity']}")
        st.write(f"**Built:** {s['built']}")
        st.write(f"**Current use:** {s['club_use']}")
        st.write(f"**Legacy:** {s['legacy']}")
        st.write(f"**Fun fact:** {s['fun_fact']}")
