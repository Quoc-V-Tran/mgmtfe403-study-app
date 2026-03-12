import streamlit as st
from utils.validators import normalize_numeric_input, is_close_answer


SYMBOL_OPTIONS = ["↑", "↓", "="]
# All dropdowns: "Select" first as neutral default; treat "Select" as unanswered/incorrect when checking
FSET_DROPDOWN_OPTIONS = ["Select", "↑", "↓", "="]
EFFECT_OPTIONS = ["Select", "Increase", "Decrease", "No effect"]
BOND_OPTIONS = ["Select", "Increase", "Decrease", "Insufficient information"]
PPE_RISK_OPTIONS = ["Select", "Higher credit risk", "Lower credit risk", "No change"]

# Readable labels for FSET fields (short key -> display label)
FSET_LABELS = {
    "ca": "Current assets (CA)",
    "cl": "Current liabilities (CL)",
    "cr": "Current ratio, CR (CA ÷ CL)",
    "d": "Debt (D)",
    "e": "Equity (E)",
    "de": "Debt-to-equity (D ÷ E)",
    "ni": "Net income (NI)",
    "avg_a": "Average assets (Avg A)",
    "roa": "ROA (NI ÷ Avg A)",
    "cfo": "Cash flow from operations (CFO)",
}


# Part I compact column labels and field keys (order: CA, CL, CR, D, E, D/E, NI, Avg A, ROA, CFO)
FSET_COL_LABELS = ["CA", "CL", "CR", "D", "E", "D/E", "NI", "Avg A", "ROA", "CFO"]
FSET_KEYS = ["ca", "cl", "cr", "d", "e", "de", "ni", "avg_a", "roa", "cfo"]


def render_part_i_question(question, key_prefix="part_i"):
    st.markdown("**Part I — Financial Statement Effects of Transactions (FSET)**")
    st.markdown(
        "For each event, determine the effect on the relevant inputs first, then determine the resulting ratio.\n\n"
        "For each ratio set:\n"
        "- Choose the effect on the numerator\n"
        "- Choose the effect on the denominator\n"
        "- Then choose the effect on the overall ratio\n\n"
        "Use:\n"
        "- ↑ = increase\n"
        "- ↓ = decrease\n"
        "- = = no effect\n\n"
        "You will answer for:\n"
        "- Current Ratio (CR = CA ÷ CL)\n"
        "- Debt-to-Equity (D/E = D ÷ E)\n"
        "- Return on Assets (ROA = NI ÷ Avg A)\n"
        "- Cash Flow from Operations (CFO)"
    )
    st.markdown("---")
    st.markdown(f"**Event {question['id']}**")
    st.write(question["event"])

    cols = st.columns(10)
    values = []
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"**{FSET_COL_LABELS[i]}**")
            values.append(
                st.selectbox(
                    FSET_COL_LABELS[i],
                    FSET_DROPDOWN_OPTIONS,
                    key=f"{key_prefix}_{FSET_KEYS[i]}",
                    label_visibility="collapsed",
                )
            )
    ca, cl, cr, d, e, de, ni, avg_a, roa, cfo = values

    st.caption(
        "CA = Current assets · CL = Current liabilities · CR = Current ratio · D = Debt · E = Equity · "
        "NI = Net income · Avg A = Average assets · ROA = Return on assets · CFO = Cash flow from operations"
    )

    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        user_answers = stored["user_answers"]
        correct = stored["correct"]
        st.markdown("---")
        st.markdown("**Results**")
        result_cols = st.columns(10)
        for i, field in enumerate(FSET_KEYS):
            user_val = user_answers[field]
            corr_val = correct[field]
            is_correct = user_val == corr_val
            with result_cols[i]:
                if is_correct:
                    st.success(f"✓ {user_val}")
                else:
                    display_you = user_val if user_val != "Select" else "—"
                    st.error(f"✗ yours {display_you} → correct {corr_val}")
        with st.expander("Explanation"):
            st.write(question["explanation"])
        return False

    if st.button("Check Answer", key=f"{key_prefix}_check"):
        user_answers = {
            "ca": ca, "cl": cl, "cr": cr,
            "d": d, "e": e, "de": de,
            "ni": ni, "avg_a": avg_a, "roa": roa,
            "cfo": cfo,
        }
        correct = question["answers"]
        all_correct = True
        st.markdown("---")
        st.markdown("**Results**")
        result_cols = st.columns(10)
        for i, field in enumerate(FSET_KEYS):
            user_val = user_answers[field]
            corr_val = correct[field]
            is_correct = user_val == corr_val
            if not is_correct:
                all_correct = False
            with result_cols[i]:
                if is_correct:
                    st.success(f"✓ {user_val}")
                else:
                    display_you = user_val if user_val != "Select" else "—"
                    st.error(f"✗ yours {display_you} → correct {corr_val}")
        with st.expander("Explanation"):
            st.write(question["explanation"])
        st.session_state[feedback_key] = {"user_answers": user_answers, "correct": correct}
        return all_correct
    return False


def render_mcq(question_text, answer, explanation, key_prefix):
    choice = st.selectbox("Your answer (Increase / Decrease / No effect)", EFFECT_OPTIONS, key=f"{key_prefix}_choice")
    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        is_correct = stored["is_correct"]
        if is_correct:
            st.success("Correct.")
        else:
            st.error(f"Incorrect. Correct answer: **{stored['answer']}**")
        with st.expander("Explanation"):
            st.write(stored["explanation"])
        return False
    if st.button("Check Answer", key=f"{key_prefix}_check"):
        if choice == answer:
            st.success("Correct.")
            with st.expander("Explanation"):
                st.write(explanation)
            st.session_state[feedback_key] = {
                "is_correct": True,
                "answer": answer,
                "explanation": explanation,
            }
            return True
        else:
            st.error(f"Incorrect. Correct answer: **{answer}**")
            with st.expander("Explanation"):
                st.write(explanation)
            st.session_state[feedback_key] = {
                "is_correct": False,
                "answer": answer,
                "explanation": explanation,
            }
        return False
    return False


def render_bond_question(data, key_prefix="bond"):
    c1, c2 = st.columns(2)
    with c1:
        discount = st.selectbox(
            "Bond issued at discount",
            BOND_OPTIONS,
            key=f"{key_prefix}_discount",
        )
    with c2:
        premium = st.selectbox(
            "Bond issued at premium",
            BOND_OPTIONS,
            key=f"{key_prefix}_premium",
        )

    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        st.markdown("---")
        if stored["ok1"]:
            st.success("Discount: correct")
        else:
            st.error(f"Discount: correct answer is **{stored['discount_answer']}**")
        if stored["ok2"]:
            st.success("Premium: correct")
        else:
            st.error(f"Premium: correct answer is **{stored['premium_answer']}**")
        with st.expander("Explanation"):
            st.write(f"**Discount:** {stored['explanation_discount']}")
            st.write(f"**Premium:** {stored['explanation_premium']}")
        return False
    if st.button("Check Answer", key=f"{key_prefix}_check"):
        ok1 = discount == data["discount_answer"]
        ok2 = premium == data["premium_answer"]
        st.markdown("---")
        if ok1:
            st.success("Discount: correct")
        else:
            st.error(f"Discount: correct answer is **{data['discount_answer']}**")
        if ok2:
            st.success("Premium: correct")
        else:
            st.error(f"Premium: correct answer is **{data['premium_answer']}**")
        with st.expander("Explanation"):
            st.write(f"**Discount:** {data['explanation_discount']}")
            st.write(f"**Premium:** {data['explanation_premium']}")
        st.session_state[feedback_key] = {
            "ok1": ok1, "ok2": ok2,
            "discount_answer": data["discount_answer"],
            "premium_answer": data["premium_answer"],
            "explanation_discount": data["explanation_discount"],
            "explanation_premium": data["explanation_premium"],
        }
        return ok1 and ok2
    return False


def render_lifo_fifo(data, key_prefix="lifo_fifo"):
    st.write(data["prompt"])
    st.dataframe(
        {
            "Field": [
                "Reported Inventory (LIFO)",
                "Reported COGS (LIFO)",
                "LIFO Reserve (end of year)",
                "LIFO Reserve (prior year)",
            ],
            "Value": [
                data["reported_inventory_lifo"],
                data["reported_cogs_lifo"],
                data["lifo_reserve_end"],
                data["lifo_reserve_prior"],
            ],
        },
        use_container_width=True,
        hide_index=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        inv = st.text_input("All-FIFO Inventory", key=f"{key_prefix}_inv", label_visibility="visible")
    with c2:
        cogs = st.text_input("All-FIFO COGS", key=f"{key_prefix}_cogs", label_visibility="visible")

    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        st.markdown("---")
        if stored["ok1"]:
            st.success("All-FIFO Inventory: correct")
        else:
            st.error(f"All-FIFO Inventory: correct **{stored['correct_inventory_fifo']}**")
        if stored["ok2"]:
            st.success("All-FIFO COGS: correct")
        else:
            st.error(f"All-FIFO COGS: correct **{stored['correct_cogs_fifo']}**")
        with st.expander("Explanation"):
            for line in stored["explanation"]:
                st.write(line)
        return False
    if st.button("Check Answer", key=f"{key_prefix}_check"):
        ok1 = is_close_answer(inv, data["correct_inventory_fifo"], tolerance=0.5)
        ok2 = is_close_answer(cogs, data["correct_cogs_fifo"], tolerance=0.5)
        st.markdown("---")
        if ok1:
            st.success("All-FIFO Inventory: correct")
        else:
            st.error(f"All-FIFO Inventory: correct **{data['correct_inventory_fifo']}**")
        if ok2:
            st.success("All-FIFO COGS: correct")
        else:
            st.error(f"All-FIFO COGS: correct **{data['correct_cogs_fifo']}**")
        with st.expander("Explanation"):
            for line in data["explanation"]:
                st.write(line)
        st.session_state[feedback_key] = {
            "ok1": ok1, "ok2": ok2,
            "correct_inventory_fifo": data["correct_inventory_fifo"],
            "correct_cogs_fifo": data["correct_cogs_fifo"],
            "explanation": data["explanation"],
        }
        return ok1 and ok2
    return False


def render_ppe_question(data, key_prefix="ppe"):
    st.write(data["prompt"])
    st.dataframe(
        {"Metric": list(data["data"].keys()), "Value": list(data["data"].values())},
        use_container_width=True,
        hide_index=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        gross = st.text_input("Gross PP&E", key=f"{key_prefix}_gross", label_visibility="visible")
        de = st.text_input("Debt-to-Equity ratio", key=f"{key_prefix}_de", label_visibility="visible")
    with c2:
        risk = st.selectbox(
            "If liabilities ↓ and equity unchanged → credit risk?",
            PPE_RISK_OPTIONS,
            key=f"{key_prefix}_risk",
        )
        bonus = st.text_input("Bonus: EBITDA (optional)", key=f"{key_prefix}_ebitda", label_visibility="visible")

    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        st.markdown("---")
        if stored["ok1"]:
            st.success("Gross PP&E: correct")
        else:
            st.error(f"Gross PP&E → **{stored['gross_ppe_answer']}**")
        if stored["ok2"]:
            st.success("Debt-to-Equity: correct")
        else:
            st.error(f"Debt-to-Equity → **{stored['de_ratio_answer']}**")
        if stored["ok3"]:
            st.success("Credit risk: correct")
        else:
            st.error(f"Credit risk → **{stored['credit_risk_answer']}**")
        if stored.get("bonus_filled"):
            if stored["ok4"]:
                st.success("Bonus EBITDA: correct")
            else:
                st.error(f"Bonus EBITDA → **{stored['bonus_ebitda_answer']}**")
        with st.expander("Explanation"):
            st.write(stored["gross_ppe_explanation"])
            st.write(stored["de_ratio_explanation"])
            st.write(stored["credit_risk_explanation"])
            st.write(stored["bonus_ebitda_explanation"])
        return False
    if st.button("Check Answer", key=f"{key_prefix}_check"):
        ok1 = is_close_answer(gross, data["gross_ppe_answer"], tolerance=0.5)
        ok2 = is_close_answer(de, data["de_ratio_answer"], tolerance=0.01)
        ok3 = risk == data["credit_risk_answer"]
        ok4 = bonus.strip() == "" or is_close_answer(bonus, data["bonus_ebitda_answer"], tolerance=0.5)
        st.markdown("---")
        if ok1:
            st.success("Gross PP&E: correct")
        else:
            st.error(f"Gross PP&E → **{data['gross_ppe_answer']}**")
        if ok2:
            st.success("Debt-to-Equity: correct")
        else:
            st.error(f"Debt-to-Equity → **{data['de_ratio_answer']}**")
        if ok3:
            st.success("Credit risk: correct")
        else:
            st.error(f"Credit risk → **{data['credit_risk_answer']}**")
        if bonus.strip():
            if ok4:
                st.success("Bonus EBITDA: correct")
            else:
                st.error(f"Bonus EBITDA → **{data['bonus_ebitda_answer']}**")
        with st.expander("Explanation"):
            st.write(data["gross_ppe_explanation"])
            st.write(data["de_ratio_explanation"])
            st.write(data["credit_risk_explanation"])
            st.write(data["bonus_ebitda_explanation"])
        st.session_state[feedback_key] = {
            "ok1": ok1, "ok2": ok2, "ok3": ok3, "ok4": ok4,
            "bonus_filled": bool(bonus.strip()),
            "gross_ppe_answer": data["gross_ppe_answer"],
            "de_ratio_answer": data["de_ratio_answer"],
            "credit_risk_answer": data["credit_risk_answer"],
            "bonus_ebitda_answer": data["bonus_ebitda_answer"],
            "gross_ppe_explanation": data["gross_ppe_explanation"],
            "de_ratio_explanation": data["de_ratio_explanation"],
            "credit_risk_explanation": data["credit_risk_explanation"],
            "bonus_ebitda_explanation": data["bonus_ebitda_explanation"],
        }
        return ok1 and ok2 and ok3
    return False


def render_dep_question(data, key_prefix="dep"):
    labels = list(data["answers"].keys())
    answers = {}
    for i, item in enumerate(labels):
        answers[item] = st.selectbox(item, EFFECT_OPTIONS, key=f"{key_prefix}_{item}", label_visibility="visible")
    feedback_key = f"{key_prefix}_feedback"
    stored = st.session_state.get(feedback_key)
    if stored is not None:
        st.markdown("---")
        for item, correct in stored["correct_answers"].items():
            user_val = stored["user_answers"].get(item)
            if user_val == correct:
                st.success(f"{item}: **{correct}**")
            else:
                st.error(f"{item}: yours **{user_val}** → **{correct}**")
        with st.expander("Explanation"):
            for item, text in stored["explanations"].items():
                st.write(f"**{item}:** {text}")
        return False
    if st.button("Check Answer", key=f"{key_prefix}_check"):
        all_correct = True
        st.markdown("---")
        for item, correct in data["answers"].items():
            if answers[item] == correct:
                st.success(f"{item}: **{correct}**")
            else:
                all_correct = False
                st.error(f"{item}: yours **{answers[item]}** → **{correct}**")
        with st.expander("Explanation"):
            for item, text in data["explanations"].items():
                st.write(f"**{item}:** {text}")
        st.session_state[feedback_key] = {
            "user_answers": dict(answers),
            "correct_answers": dict(data["answers"]),
            "explanations": dict(data["explanations"]),
        }
        return all_correct
    return False
