import random
import streamlit as st
from data.questions import (
    PART_I_QUESTIONS,
    BONUS_FSET_QUESTIONS,
    PART_II_Q1,
    PART_II_Q2,
    PART_II_Q3,
    PART_II_Q4,
    PART_II_Q5,
    PART_II_Q6,
)
from components.renderers import (
    render_part_i_question,
    render_mcq,
    render_bond_question,
    render_lifo_fifo,
    render_ppe_question,
    render_dep_question,
)

st.set_page_config(page_title="MGMTFE 403 Study App", layout="wide", initial_sidebar_state="expanded")

# --- Tab config for sidebar: (key, label, total_questions) ---
TAB_CONFIG = [
    ("part_i", "FSET Ratios + CFO", len(PART_I_QUESTIONS)),
    ("bonus_fset", "Bonus FSET Ratios + CFO", len(BONUS_FSET_QUESTIONS)),
    ("q1", "Shareholders' Equity", len(PART_II_Q1)),
    ("q2", "Stock Dividends", len(PART_II_Q2)),
    ("bond", "Bond Carrying Value", 1),
    ("lifo_fifo", "LIFO → FIFO", 1),
    ("ppe", "PP&E / D/E / Credit Risk", 1),
    ("dep", "Depreciation Effects", 1),
]

def _init_state():
    for key, _, total in TAB_CONFIG:
        if f"{key}_completed" not in st.session_state:
            st.session_state[f"{key}_completed"] = set()
        if key == "part_i" and "part_i_index" not in st.session_state:
            st.session_state.part_i_index = 0
        if key == "part_i" and "part_i_order" not in st.session_state:
            st.session_state.part_i_order = random.sample(range(len(PART_I_QUESTIONS)), len(PART_I_QUESTIONS))
        if key == "bonus_fset" and "bonus_fset_index" not in st.session_state:
            st.session_state.bonus_fset_index = 0
        if key == "bonus_fset" and "bonus_fset_order" not in st.session_state:
            st.session_state.bonus_fset_order = random.sample(range(len(BONUS_FSET_QUESTIONS)), len(BONUS_FSET_QUESTIONS))
        if key == "q1" and "q1_index" not in st.session_state:
            st.session_state.q1_index = 0
        if key == "q2" and "q2_index" not in st.session_state:
            st.session_state.q2_index = 0

def _get_index(key):
    if key == "part_i":
        return st.session_state.get("part_i_index", 0)
    if key == "bonus_fset":
        return st.session_state.get("bonus_fset_index", 0)
    if key == "q1":
        return st.session_state.get("q1_index", 0)
    if key == "q2":
        return st.session_state.get("q2_index", 0)
    return 0

def _get_score(key):
    return len(st.session_state.get(f"{key}_completed", set()))

def _mark_completed(key, question_id):
    if f"{key}_completed" not in st.session_state:
        st.session_state[f"{key}_completed"] = set()
    st.session_state[f"{key}_completed"] = st.session_state[f"{key}_completed"] | {question_id}

def _clear_tab_feedback(key, total):
    """Clear stored feedback state for a tab so it doesn't persist after Reset."""
    if total > 1:
        for i in range(total):
            st.session_state.pop(f"{key}_{i}_feedback", None)
    else:
        st.session_state.pop(f"{key}_feedback", None)

def _reset_tab(key):
    _, _, total = next((t for t in TAB_CONFIG if t[0] == key), (key, "", 1))
    _clear_tab_feedback(key, total)
    st.session_state[f"{key}_completed"] = set()
    if key == "part_i":
        st.session_state.part_i_index = 0
    elif key == "bonus_fset":
        st.session_state.bonus_fset_index = 0
    elif key == "q1":
        st.session_state.q1_index = 0
    elif key == "q2":
        st.session_state.q2_index = 0
    st.rerun()

def _reset_all():
    for key, _, total in TAB_CONFIG:
        _clear_tab_feedback(key, total)
        st.session_state[f"{key}_completed"] = set()
    st.session_state.part_i_index = 0
    st.session_state.bonus_fset_index = 0
    st.session_state.q1_index = 0
    st.session_state.q2_index = 0
    st.rerun()

_init_state()

# --- Sidebar: progress & score by tab ---
with st.sidebar:
    st.markdown("### Progress by topic")
    st.caption("Score = unique questions answered correctly. Reset per tab or all.")
    for key, label, total in TAB_CONFIG:
        score = _get_score(key)
        progress = score / total if total > 0 else 0.0
        st.markdown(f"**{label}**")
        st.progress(progress)
        st.caption(f"Score: {score} / {total}")
    st.divider()
    if st.button("Reset all progress", type="secondary", width="stretch"):
        _reset_all()

st.title("MGMTFE 403 Study App")
st.caption("Practice by topic. Choose the effect on each FSET component (CA, CL, D, E, NI, Avg A, CFO) and use **Check Answer** for feedback. You can correct wrong answers and resubmit until correct. Reset per tab below or in the sidebar.")
st.caption("FSET tabs: question order is shuffled on each app load. Use ↑ / ↓ / = for increase / decrease / no effect.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "FSET Ratios + CFO",
    "Bonus FSET Ratios + CFO",
    "Shareholders' Equity Effects",
    "Stock Dividends",
    "Bond Carrying Value",
    "LIFO → FIFO Conversion",
    "PP&E / D/E / Credit Risk",
    "Effects of Recording Depreciation",
])

with tab1:
    idx = st.session_state.part_i_index
    order = st.session_state.part_i_order
    n = len(PART_I_QUESTIONS)
    st.caption(f"Question {idx + 1} of {n}")
    result = render_part_i_question(PART_I_QUESTIONS[order[idx]], key_prefix=f"part_i_{idx}")
    if result is True and idx not in st.session_state.get("part_i_completed", set()):
        _mark_completed("part_i", idx)
        st.rerun()
    row = st.columns([2, 1, 1])
    with row[0]:
        pass
    with row[1]:
        if st.button("Back", key="part_i_back") and idx > 0:
            st.session_state.part_i_index -= 1
            st.rerun()
    with row[2]:
        if st.button("Next", key="part_i_next") and idx < n - 1:
            st.session_state.part_i_index += 1
            st.rerun()
    if st.button("Reset this tab", key="part_i_reset"):
        _reset_tab("part_i")

with tab2:
    idx = st.session_state.bonus_fset_index
    order = st.session_state.bonus_fset_order
    n = len(BONUS_FSET_QUESTIONS)
    st.caption("Additional in-class review set.")
    st.caption(f"Question {idx + 1} of {n}")
    result = render_part_i_question(BONUS_FSET_QUESTIONS[order[idx]], key_prefix=f"bonus_fset_{idx}")
    if result is True and idx not in st.session_state.get("bonus_fset_completed", set()):
        _mark_completed("bonus_fset", idx)
        st.rerun()
    row = st.columns([2, 1, 1])
    with row[0]:
        pass
    with row[1]:
        if st.button("Back", key="bonus_fset_back") and idx > 0:
            st.session_state.bonus_fset_index -= 1
            st.rerun()
    with row[2]:
        if st.button("Next", key="bonus_fset_next") and idx < n - 1:
            st.session_state.bonus_fset_index += 1
            st.rerun()
    if st.button("Reset this tab", key="bonus_fset_reset"):
        _reset_tab("bonus_fset")

with tab3:
    idx = st.session_state.q1_index
    q = PART_II_Q1[idx]
    n = len(PART_II_Q1)
    st.caption(f"Question {idx + 1} of {n}")
    st.markdown("**Indicate the effect on total shareholders' equity.**")
    st.write(q["question"])
    result = render_mcq(q["question"], q["answer"], q["explanation"], key_prefix=f"q1_{idx}")
    if result is True:
        _mark_completed("q1", idx)
        st.rerun()
    row = st.columns([2, 1, 1])
    with row[1]:
        if st.button("Back", key="q1_back") and idx > 0:
            st.session_state.q1_index -= 1
            st.rerun()
    with row[2]:
        if st.button("Next", key="q1_next") and idx < n - 1:
            st.session_state.q1_index += 1
            st.rerun()
    if st.button("Reset this tab", key="q1_reset"):
        _reset_tab("q1")

with tab4:
    idx = st.session_state.q2_index
    q = PART_II_Q2[idx]
    n = len(PART_II_Q2)
    st.caption(f"Question {idx + 1} of {n}")
    st.markdown("**Stock Dividends**")
    st.write(q["question"])
    result = render_mcq(q["question"], q["answer"], q["explanation"], key_prefix=f"q2_{idx}")
    if result is True:
        _mark_completed("q2", idx)
        st.rerun()
    row = st.columns([2, 1, 1])
    with row[1]:
        if st.button("Back", key="q2_back") and idx > 0:
            st.session_state.q2_index -= 1
            st.rerun()
    with row[2]:
        if st.button("Next", key="q2_next") and idx < n - 1:
            st.session_state.q2_index += 1
            st.rerun()
    if st.button("Reset this tab", key="q2_reset"):
        _reset_tab("q2")

with tab5:
    st.markdown("**Bond Carrying Value**")
    st.write(PART_II_Q3["question"])
    result = render_bond_question(PART_II_Q3)
    if result is True:
        _mark_completed("bond", 0)
        st.rerun()
    if st.button("Reset this tab", key="bond_reset"):
        _reset_tab("bond")

with tab6:
    st.markdown("**LIFO → FIFO Conversion**")
    result = render_lifo_fifo(PART_II_Q4)
    if result is True:
        _mark_completed("lifo_fifo", 0)
        st.rerun()
    if st.button("Reset this tab", key="lifo_reset"):
        _reset_tab("lifo_fifo")

with tab7:
    st.markdown("**PP&E / D/E / Credit Risk**")
    result = render_ppe_question(PART_II_Q5)
    if result is True:
        _mark_completed("ppe", 0)
        st.rerun()
    if st.button("Reset this tab", key="ppe_reset"):
        _reset_tab("ppe")

with tab8:
    st.markdown("**Effects of Recording Depreciation**")
    st.write(PART_II_Q6["prompt"])
    result = render_dep_question(PART_II_Q6)
    if result is True:
        _mark_completed("dep", 0)
        st.rerun()
    if st.button("Reset this tab", key="dep_reset"):
        _reset_tab("dep")
