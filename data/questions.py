PART_I_QUESTIONS = [
    {
        "id": 1,
        "event": "Paid $48 cash to repurchase shares of the company's own stock.",
        "answers": {
            "ca": "↓",
            "cl": "=",
            "d": "=",
            "e": "↓",
            "ni": "=",
            "avg_a": "↓",
            "cfo": "=",
        },
        "explanation": "Debit Treasury Stock (equity decreases) | Credit Cash (current assets decrease). Cash outflow is financing, so CFO has no effect.",
    },
    {
        "id": 2,
        "event": "Purchased $30 of inventory on credit (accounts payable); no cash paid yet.",
        "answers": {
            "ca": "↑",
            "cl": "↑",
            "d": "↑",
            "e": "=",
            "ni": "=",
            "avg_a": "↑",
            "cfo": "=",
        },
        "explanation": "Debit Inventory (current assets increase) | Credit Accounts Payable (current liabilities increase). No income effect and no cash flow effect.",
    },
    {
        "id": 3,
        "event": "Wrote off $40 of accounts receivable after a customer declared bankruptcy. The company uses the allowance method.",
        "answers": {
            "ca": "=",
            "cl": "=",
            "d": "=",
            "e": "=",
            "ni": "=",
            "avg_a": "=",
            "cfo": "=",
        },
        "explanation": "Debit Allowance for Doubtful Accounts | Credit Accounts Receivable. Under the allowance method, net A/R does not change at write-off, so there is no income or cash flow effect.",
    },
    {
        "id": 4,
        "event": "Recognized $60 of depreciation on manufacturing equipment.",
        "answers": {
            "ca": "=",
            "cl": "=",
            "d": "=",
            "e": "↓",
            "ni": "↓",
            "avg_a": "↓",
            "cfo": "=",
        },
        "explanation": "Debit Depreciation Expense (net income decreases, equity decreases) | Credit Accumulated Depreciation (assets decrease on a net basis). Depreciation is non-cash, so CFO has no effect under this study guide convention.",
    },
    {
        "id": 5,
        "event": "Declared and paid a $150 cash dividend to shareholders.",
        "answers": {
            "ca": "↓",
            "cl": "=",
            "d": "=",
            "e": "↓",
            "ni": "=",
            "avg_a": "↓",
            "cfo": "=",
        },
        "explanation": "Debit Retained Earnings (equity decreases) | Credit Cash (current assets decrease). Dividend payment is financing, so CFO has no effect.",
    },
    {
        "id": 6,
        "event": "Sold PP&E for $55 cash. The asset had a net book value of $70 at the time of sale.",
        "answers": {
            "ca": "↑",
            "cl": "=",
            "d": "=",
            "e": "↓",
            "ni": "↓",
            "avg_a": "↓",
            "cfo": "=",
        },
        "explanation": "Debit Cash 55 | Debit Loss on Sale 15 | Credit PP&E 70. Cash increases, a loss reduces net income and equity, and CFO is not affected by the investing cash flow.",
    },
]

BONUS_FSET_QUESTIONS = [
    {
        "id": 1,
        "event": "Bought $80k equipment for cash",
        "answers": {"ca": "↓", "cl": "=", "d": "=", "e": "=", "ni": "=", "avg_a": "=", "cfo": "="},
        "explanation": "Debit PP&E (noncurrent asset) | Credit Cash (current assets decrease). No effect on liabilities, equity, or net income. Cash outflow is investing, so CFO has no effect.",
    },
    {
        "id": 2,
        "event": "Recognized $12k of accrued wages that will be paid next month",
        "answers": {"ca": "=", "cl": "↑", "d": "↑", "e": "↓", "ni": "↓", "avg_a": "=", "cfo": "="},
        "explanation": "Debit Wage Expense (NI and equity decrease) | Credit Wages Payable (current liabilities increase). No cash flow until paid.",
    },
    {
        "id": 3,
        "event": "Recognized $12k of accrued wages that will be paid now",
        "answers": {"ca": "↓", "cl": "=", "d": "=", "e": "↓", "ni": "↓", "avg_a": "↓", "cfo": "↓"},
        "explanation": "Debit Wage Expense (NI and equity decrease) | Credit Cash (CA and avg assets decrease). Cash paid is operating outflow, so CFO decreases.",
    },
    {
        "id": 4,
        "event": "Paid $1k for prepaid rent",
        "answers": {"ca": "=", "cl": "=", "d": "=", "e": "=", "ni": "=", "avg_a": "=", "cfo": "↓"},
        "explanation": "Debit Prepaid Rent (one current asset) | Credit Cash (another current asset). Net CA unchanged; cash outflow is operating, so CFO decreases.",
    },
    {
        "id": 5,
        "event": "Paid the $12k in wages from Question #2",
        "answers": {"ca": "↓", "cl": "↓", "d": "=", "e": "=", "ni": "=", "avg_a": "=", "cfo": "↓"},
        "explanation": "Debit Wages Payable (CL decrease) | Credit Cash (CA decrease). No income effect; cash outflow is operating, so CFO decreases.",
    },
    {
        "id": 6,
        "event": "Collected $25k in cash from a customer for work to be done in 3 years",
        "answers": {"ca": "↑", "cl": "=", "d": "↑", "e": "=", "ni": "=", "avg_a": "=", "cfo": "↑"},
        "explanation": "Debit Cash (CA increase) | Credit Unearned Revenue (long-term liability, so D increases). Cash received is operating inflow, so CFO increases.",
    },
    {
        "id": 7,
        "event": "In the year we are to complete the work from Question #6, move the liability to current",
        "answers": {"ca": "=", "cl": "↓", "d": "=", "e": "=", "ni": "=", "avg_a": "=", "cfo": "="},
        "explanation": "Reclassify Unearned Revenue from long-term to current. Total liabilities unchanged; no cash or income effect.",
    },
    {
        "id": 8,
        "event": "Record the sale for the job for the customer from Question #6",
        "answers": {"ca": "=", "cl": "↓", "d": "↓", "e": "↑", "ni": "↑", "avg_a": "=", "cfo": "="},
        "explanation": "Debit Unearned Revenue (CL and D decrease) | Credit Revenue (NI and equity increase). No cash; revenue recognition only.",
    },
    {
        "id": 9,
        "event": "Record the cost of goods sold for the job for the customer in Question #6",
        "answers": {"ca": "↓", "cl": "=", "d": "=", "e": "↓", "ni": "↓", "avg_a": "↓", "cfo": "="},
        "explanation": "Debit COGS (NI and equity decrease) | Credit Inventory (CA and avg assets decrease). No cash flow; COGS is non-cash.",
    },
    {
        "id": 10,
        "event": "Issued $200K of 5% bonds at par value on Dec 31, 2026 due in 5 years, paid annually",
        "answers": {"ca": "↑", "cl": "=", "d": "↑", "e": "=", "ni": "=", "avg_a": "↑", "cfo": "="},
        "explanation": "Debit Cash (CA and avg assets increase) | Credit Bonds Payable (D increase). Financing inflow; no effect on CFO.",
    },
    {
        "id": 11,
        "event": "Recognized and paid interest on the bond from Question #10 on Dec 31, 2027",
        "answers": {"ca": "↓", "cl": "=", "d": "=", "e": "↓", "ni": "↓", "avg_a": "↓", "cfo": "↓"},
        "explanation": "Debit Interest Expense (NI and equity decrease) | Credit Cash (CA and avg assets decrease). Interest paid is operating outflow, so CFO decreases.",
    },
    {
        "id": 12,
        "event": "Sold $40K of inventory for $60K. We estimate that 5% of these sales will be returned via warranty",
        "answers": {"ca": "↑", "cl": "↑", "d": "↑", "e": "↑", "ni": "↑", "avg_a": "↑", "cfo": "↑"},
        "explanation": "Sale increases receivables/cash, revenue (and COGS reduces inventory); warranty accrual adds estimated liability and expense. Per the key, net effect on components and CFO is increase.",
    },
]

PART_II_Q1 = [
    {
        "question": "Treasury stock is reissued at a price above its historical repurchase cost.",
        "answer": "Increase",
        "explanation": "Reissuing treasury stock above cost increases additional paid-in capital, which increases total shareholders' equity.",
    },
    {
        "question": "The company declares a cash dividend (not yet paid).",
        "answer": "Decrease",
        "explanation": "A declared cash dividend reduces retained earnings, so total shareholders' equity decreases.",
    },
    {
        "question": "PP&E is sold for exactly its net book value.",
        "answer": "No effect",
        "explanation": "If sold at net book value, there is no gain or loss, so no effect on shareholders' equity.",
    },
    {
        "question": "Goodwill impairment is recognized.",
        "answer": "Decrease",
        "explanation": "Impairment loss reduces net income and therefore reduces shareholders' equity.",
    },
]

PART_II_Q2 = [
    {
        "question": "Effect on total assets for a 10% stock dividend declared and distributed.",
        "answer": "No effect",
        "explanation": "A stock dividend does not distribute assets, so total assets are unchanged.",
    },
    {
        "question": "Effect on retained earnings for a 10% stock dividend declared and distributed.",
        "answer": "Decrease",
        "explanation": "Retained earnings decreases because equity is reclassified into contributed capital accounts.",
    },
    {
        "question": "Effect on total shareholders' equity for a 10% stock dividend declared and distributed.",
        "answer": "No effect",
        "explanation": "This is an internal reclassification within equity, so total equity does not change.",
    },
]

PART_II_Q3 = {
    "question": "How does the carrying value of a bond payable change over time?",
    "discount_answer": "Increase",
    "premium_answer": "Decrease",
    "explanation_discount": "A discount amortizes upward toward face value, so carrying value increases over time.",
    "explanation_premium": "A premium amortizes downward toward face value, so carrying value decreases over time.",
}

PART_II_Q4 = {
    "prompt": "A company reports the following (in millions). Estimate Inventory and COGS under All-FIFO.",
    "reported_inventory_lifo": 8400,
    "reported_cogs_lifo": 52300,
    "lifo_reserve_end": 210,
    "lifo_reserve_prior": 195,
    "correct_inventory_fifo": 8610,
    "correct_cogs_fifo": 52285,
    "explanation": [
        "All-FIFO Inventory = Reported Inventory + LIFO Reserve (end)",
        "8,400 + 210 = 8,610",
        "ΔLIFO Reserve = 210 − 195 = 15",
        "Reserve grew, so LIFO COGS was higher",
        "All-FIFO COGS = Reported COGS − ΔLIFO Reserve",
        "52,300 − 15 = 52,285",
    ],
}

PART_II_Q5 = {
    "prompt": "Use the data below to answer the following questions. All amounts are in millions.",
    "data": {
        "Net PP&E (end of year)": 22500,
        "Accumulated Depreciation (end of year)": 18600,
        "Total Liabilities": 12400,
        "Total shareholders' equity": 9800,
        "Operating Income": 3800,
        "Depreciation & Amortization": 2100,
    },
    "gross_ppe_answer": 41100,
    "gross_ppe_explanation": "Gross PP&E = Net PP&E + Accumulated Depreciation = 22,500 + 18,600 = 41,100",
    "de_ratio_answer": 1.27,
    "de_ratio_explanation": "Debt-to-Equity ratio = 12,400 / 9,800 = 1.27",
    "credit_risk_answer": "Lower credit risk",
    "credit_risk_explanation": "If liabilities decrease while equity stays the same, leverage falls, so credit risk decreases.",
    "bonus_ebitda_answer": 5900,
    "bonus_ebitda_explanation": "EBITDA = Operating Income + Depreciation & Amortization = 3,800 + 2,100 = 5,900",
}

PART_II_Q6 = {
    "prompt": "When a company records depreciation, how does it affect each of the following?",
    "answers": {
        "Net income": "Decrease",
        "Cash flow from operating activities": "No effect",
        "Debt-to-Equity ratio": "Increase",
    },
    "explanations": {
        "Net income": "Depreciation is an expense, so net income decreases.",
        "Cash flow from operating activities": "Under the indirect method, depreciation is added back because it is non-cash, so CFO has no effect.",
        "Debt-to-Equity ratio": "Depreciation lowers equity through lower net income while debt stays unchanged, so D/E increases.",
    },
}