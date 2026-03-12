"""
Navigation and session state helpers for MGMTFE 403 study app.
"""
from __future__ import annotations

import streamlit as st


def init_tab_state(tab_key: str, num_questions: int) -> None:
    """Initialize or reset session state for a tab: idx, submitted, score, streak."""
    if tab_key not in st.session_state:
        st.session_state[tab_key] = {
            "idx": 0,
            "submitted": False,
            "score": 0,
            "streak": 0,
            "max_streak": 0,
        }
    state = st.session_state[tab_key]
    state["num_questions"] = num_questions


def get_idx(tab_key: str) -> int:
    return st.session_state.get(tab_key, {}).get("idx", 0)


def set_idx(tab_key: str, value: int) -> None:
    if tab_key not in st.session_state:
        st.session_state[tab_key] = {}
    st.session_state[tab_key]["idx"] = max(0, value)


def get_submitted(tab_key: str) -> bool:
    return st.session_state.get(tab_key, {}).get("submitted", False)


def set_submitted(tab_key: str, value: bool) -> None:
    if tab_key not in st.session_state:
        st.session_state[tab_key] = {}
    st.session_state[tab_key]["submitted"] = value


def get_score(tab_key: str) -> int:
    return st.session_state.get(tab_key, {}).get("score", 0)


def add_score(tab_key: str, delta: int) -> None:
    if tab_key not in st.session_state:
        st.session_state[tab_key] = {}
    st.session_state[tab_key]["score"] = st.session_state[tab_key].get("score", 0) + delta


def get_streak(tab_key: str) -> int:
    return st.session_state.get(tab_key, {}).get("streak", 0)


def set_streak(tab_key: str, value: int) -> None:
    if tab_key not in st.session_state:
        st.session_state[tab_key] = {}
    st.session_state[tab_key]["streak"] = value
    st.session_state[tab_key]["max_streak"] = max(
        st.session_state[tab_key].get("max_streak", 0), value
    )


def nav_back(tab_key: str) -> None:
    set_idx(tab_key, get_idx(tab_key) - 1)
    set_submitted(tab_key, False)


def nav_next(tab_key: str) -> None:
    n = st.session_state.get(tab_key, {}).get("num_questions", 1)
    set_idx(tab_key, min(get_idx(tab_key) + 1, n - 1))
    set_submitted(tab_key, False)


def reset_tab(tab_key: str, num_questions: int) -> None:
    init_tab_state(tab_key, num_questions)
    set_idx(tab_key, 0)
    set_submitted(tab_key, False)
    st.session_state[tab_key]["score"] = 0
    st.session_state[tab_key]["streak"] = 0
    st.session_state[tab_key]["max_streak"] = 0
