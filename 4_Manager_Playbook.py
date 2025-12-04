
import streamlit as st
import json
from pathlib import Path

st.title("Manager Playbook")

data_path = Path(__file__).parents[1] / "data" / "managers.json"
managers = json.loads(data_path.read_text(encoding="utf-8"))

name = st.selectbox("Choose a manager:", [m["name"] for m in managers])
m = next(x for x in managers if x["name"] == name)

st.header(m["name"])
st.write(f"**Style:** {m['style']}")
st.write(f"**Favourite formations:** {', '.join(m['favourite_formations'])}")
st.subheader("How this manager thinks")
st.write(m["kid_friendly_summary"])
