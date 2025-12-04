
import streamlit as st
import json
from pathlib import Path

st.title("World Cup Timeline (1962–2022)")

data_path = Path(__file__).parents[1] / "data" / "tournaments.json"
tournaments = json.loads(data_path.read_text(encoding="utf-8"))

years = sorted([t["year"] for t in tournaments])
year = st.selectbox("Choose a World Cup year:", years, index=len(years)-1)

wc = next(t for t in tournaments if t["year"] == year)

st.header(f"{wc['year']} – {wc['host']}")
st.write(f"**Winner:** {wc['winner']}")
st.write(f"**Runner-up:** {wc['runner_up']}")
st.write(f"**Final score:** {wc['final_score']}")
st.write(f"**Golden Boot:** {wc['golden_boot']}")
st.write(f"**Golden Ball:** {wc['golden_ball']}")

st.subheader("Stories from this tournament")
for fact in wc["did_you_know"]:
    st.markdown(f"- {fact}")
