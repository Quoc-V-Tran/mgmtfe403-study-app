# MGMTFE 403 Study App

A **Streamlit** study app for MGMTFE 403 final exam practice. All logic and data are local; no API keys or external services. Easy for classmates to run.

---

## Setup

1. **Install Python** (3.9 or newer).

2. **Clone or download** this project and open a terminal in the project folder.

3. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**:
   ```bash
   streamlit run app.py
   ```

6. Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## Project structure

```
MGMTFE 403 study app/
├── app.py                 # Main entry: tabs, sidebar, reset logic
├── requirements.txt       # streamlit, pandas
├── README.md              # This file
├── data/
│   ├── __init__.py
│   └── questions.py       # All practice questions and answer keys
├── components/
│   ├── __init__.py
│   ├── navigation.py      # Session-state helpers (optional / unused in current flow)
│   └── renderers.py       # UI for each topic (FSET, MCQ, bond, LIFO, PP&E, dep)
└── utils/
    ├── __init__.py
    └── validators.py      # Answer checking (numeric; strips commas and $ from input)
```

- **app.py** — Builds the sidebar (progress/score by tab, “Reset all”), the main tabs, and calls the renderers. Updates session state for scores and question indices when you click “Check Answer” or “Reset this tab”.
- **data/questions.py** — Defines `PART_I_QUESTIONS` (FSET events), `PART_II_Q1`–`PART_II_Q6` (equity, stock dividends, bond, LIFO, PP&E, depreciation). No question content is loaded from the network.
- **components/renderers.py** — One render function per topic: dropdowns, inputs, “Check Answer”, and expandable explanations. Uses **Streamlit only** (no custom CSS/JS).
- **utils/validators.py** — Helpers to compare your answers to the keys (e.g. numeric tolerance for LIFO/FIFO and PP&E).

---

## Using the app

- **Sidebar** — Shows progress (current question and total) and score per topic. Use **Reset all progress** to clear indices and scores for every tab.
- **Tabs** — One tab per topic. Use **Back** / **Next** where applicable to move between questions.
- **Check Answer** — Submits your choices and shows correct/incorrect and an explanation. Score in the sidebar updates when you get a question fully correct. Numeric inputs (e.g. LIFO, PP&E) accept commas and dollar signs.
- **Reset this tab** — Resets the current tab’s question index and score only.
- **Ratio directions (↑ / ↓ / =)** — In the FSET Ratios + CFO tab, answers follow the **instructor key / study guide convention**. Use that convention when in doubt.

Everything runs in your browser and on your machine; no data is sent elsewhere.
