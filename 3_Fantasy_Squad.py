
import streamlit as st
import json
from pathlib import Path
from collections import defaultdict

st.title("Fantasy All-Time World Cup XI")

data_dir = Path(__file__).parents[1] / "data"
players = json.loads((data_dir / "players.json").read_text(encoding="utf-8"))
managers = json.loads((data_dir / "managers.json").read_text(encoding="utf-8"))

formation = st.selectbox("Choose a formation:", ["4-3-3", "4-4-2", "4-2-3-1"])
manager_name = st.selectbox("Choose a manager style:", [m["name"] for m in managers])
manager = next(m for m in managers if m["name"] == manager_name)

st.subheader("Manager philosophy")
st.write(manager["kid_friendly_summary"])

pos_map = {
    "4-3-3": ["GK","RB","RCB","LCB","LB","RCM","CM","LCM","RW","ST","LW"],
    "4-4-2": ["GK","RB","RCB","LCB","LB","RM","RCM","LCM","LM","ST1","ST2"],
    "4-2-3-1": ["GK","RB","RCB","LCB","LB","DM1","DM2","RW","CAM","LW","ST"]
}
positions = pos_map[formation]

by_pos = defaultdict(list)
for p in players:
    by_pos[p["position"]].append(p["name"])

st.subheader("Pick your XI")
selection = {}
for pos in positions:
    if pos.startswith("ST") or pos in ["RW","LW","RM","LM"]:
        key = "FW"
    elif pos.startswith("DM") or "CM" in pos or pos == "CAM":
        key = "CM"
    else:
        key = pos
    choices = by_pos.get(key, ["No players available yet"])
    selection[pos] = st.selectbox(pos, choices)

st.subheader("Your team sheet")
st.write(selection)
