import streamlit as st

st.set_page_config(
    page_title="Areesh Rashid — AI/ML & Product Design",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

CONTACT = {
    "email": "areeshrashid6@gmail.com",
    "github": "https://github.com/areeshrashid6",
    "github_label": "github.com/areeshrashid6",
}

SKILLS = [
    ("AI / ML", ["PyTorch", "CNN + BiLSTM + CTC (ASR)", "Tacotron 2 (TTS)", "Gemini Flash", "Prompt & agent design"]),
    ("Data & Backend", ["Postgres", "Vector search", "Query routing", "Python"]),
    ("Product Design", ["Figma", "Design systems", "Progressive disclosure / wizard flows", "UX research"]),
    ("Workflow & Delivery", ["Streamlit", "n8n", "GitHub", "Freelance client delivery"]),
]

LIVE_PROJECTS = [
    {
        "name": "DocuMind",
        "note": "Document intelligence app for reading, querying, and reasoning over uploaded files.",
        "url": "https://documind-jeqivg4ydgx5rvf5ke3xmq.streamlit.app/",
    },
    {
        "name": "FinTech Analyzer",
        "note": "Financial data analysis and insight tool built on Streamlit.",
        "url": "https://fintech-9h4qumpsksshphkyrljzfo.streamlit.app/",
    },
    {
        "name": "LegalEaseAI",
        "note": "AI assistant that simplifies legal documents and language for non-lawyers.",
        "url": "https://legaleaseai-cthwvseohv3adhchzdng6v.streamlit.app/",
    },
    {
        "name": "MarketMind AI",
        "note": "AI-driven market research and analysis assistant.",
        "url": "https://marketmind-ai-kcgwgnaxwxkhwvespm2cjp.streamlit.app/",
    },
    {
        "name": "MediGuide",
        "note": "AI health guidance app for symptom understanding and triage support.",
        "url": "https://areeshrashid6-mediguide--ai-app-wzxooc.streamlit.app/",
    },
    {
        "name": "Support PearlzAI",
        "note": "AI-powered customer support assistant.",
        "url": "https://support-pearlzai-6xxutuufijrqs3a2j5jj3m.streamlit.app/",
    },
]

CASE_STUDIES = [
    {
        "name": "Castora",
        "role": "Product & UX Design",
        "note": (
            "Script marketplace connecting writers and producers. Designed the full deal-flow layer — "
            "a five-stage producer pipeline from meeting to payment — plus the talent side: hiring "
            "pipelines, audition/casting flows, and a 12-screen professional hiring prototype grounded "
            "in real WGA deal structures."
        ),
    },
    {
        "name": "Astora",
        "role": "Product & UX Design",
        "note": (
            "Film production management platform built around a ten-stage pipeline, from idea "
            "development through financing. Designed a TurboTax-style progressive disclosure flow, "
            "investor deal structures, and a full funding waterfall tab."
        ),
    },
    {
        "name": "CardioAI",
        "role": "ML & Dashboard Engineering",
        "note": (
            "Heart disease classification dashboard with a full multi-tab workflow — exploratory data "
            "analysis, model training, hyperparameter tuning, and a live prediction form."
        ),
    },
    {
        "name": "Final Year Project",
        "role": "System Architecture",
        "note": (
            "AI-powered engineering intelligence platform, scoped to a GitHub + task-board agent. "
            "Hybrid architecture pairing Postgres for structured queries with a vector store for "
            "semantic search, routed through a query classifier."
        ),
    },
]

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

    :root {
        --bg: #0F1620;
        --bg-alt: #161F2C;
        --line: #26323F;
        --ink: #ECEEF1;
        --ink-muted: #93A1B3;
        --amber: #E3A857;
        --blue: #6FA9D6;
    }

    html, body, [class*="css"]  { font-family: 'Inter', sans-serif; }

    .stApp { background-color: var(--bg); color: var(--ink); }

    .block-container { max-width: 860px; padding-top: 3.5rem; padding-bottom: 5rem; }

    h1, h2, h3 { font-family: 'Fraunces', serif; color: var(--ink); }

    a { color: var(--blue); text-decoration: none; }
    a:hover { color: var(--amber); }

    .eyebrow {
        color: var(--ink-muted);
        font-size: 0.95rem;
        letter-spacing: 0.02em;
        margin-bottom: 0.4rem;
    }

    .hero-name {
        font-family: 'Fraunces', serif;
        font-size: 3rem;
        font-weight: 600;
        line-height: 1.1;
        margin: 0;
        border-left: 3px solid var(--amber);
        padding-left: 1rem;
    }

    .hero-tagline {
        font-size: 1.15rem;
        color: var(--ink-muted);
        margin-top: 0.9rem;
        padding-left: 1.1rem;
        max-width: 34rem;
    }

    .contact-row { padding-left: 1.1rem; margin-top: 1.4rem; }
    .contact-row a { margin-right: 1.6rem; font-size: 0.98rem; }

    .section-title {
        font-size: 1.5rem;
        margin-top: 3.2rem;
        margin-bottom: 1.1rem;
        padding-bottom: 0.6rem;
        border-bottom: 1px solid var(--line);
    }

    .bio { font-size: 1.02rem; line-height: 1.75; color: var(--ink); max-width: 42rem; }

    .skill-group { margin-bottom: 1.2rem; }
    .skill-group-title { color: var(--amber); font-family: 'Fraunces', serif; font-size: 1.05rem; margin-bottom: 0.4rem; }
    .skill-list { color: var(--ink-muted); font-size: 0.96rem; line-height: 1.6; }

    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 1rem;
        margin-top: 0.5rem;
    }
    .project-card {
        background: var(--bg-alt);
        border: 1px solid var(--line);
        border-top: 2px solid var(--blue);
        padding: 1.3rem 1.3rem 1.1rem 1.3rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 168px;
        transition: transform 0.15s ease, border-color 0.15s ease;
    }
    .project-card:hover { transform: translateY(-3px); border-top-color: var(--amber); }
    .project-name { font-family: 'Fraunces', serif; font-size: 1.15rem; color: var(--ink); margin-bottom: 0.5rem; }
    .project-note { color: var(--ink-muted); font-size: 0.9rem; line-height: 1.5; margin: 0 0 1rem 0; flex-grow: 1; }
    .project-link {
        font-size: 0.85rem;
        color: var(--blue);
        border: 1px solid var(--line);
        padding: 0.4rem 0.8rem;
        display: inline-block;
        width: fit-content;
    }
    .project-link:hover { color: var(--amber); border-color: var(--amber); }

    .case-row {
        border-left: 2px solid var(--line);
        padding: 0.4rem 0 0.4rem 1.1rem;
        margin-bottom: 1.4rem;
    }
    .case-row:hover { border-left-color: var(--amber); }
    .case-name { font-family: 'Fraunces', serif; font-size: 1.2rem; color: var(--ink); }
    .case-role { color: var(--amber); font-size: 0.85rem; margin-bottom: 0.35rem; }
    .case-note { color: var(--ink-muted); font-size: 0.94rem; max-width: 40rem; line-height: 1.6; }

    .footer {
        margin-top: 4rem;
        padding-top: 1.5rem;
        border-top: 1px solid var(--line);
        color: var(--ink-muted);
        font-size: 0.88rem;
    }

    #MainMenu, header, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------

st.markdown('<p class="eyebrow">Portfolio</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-name">Areesh Rashid</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-tagline">AI/ML &amp; Data Engineer with a product design background — '
    'I design and ship intelligent systems end to end, from data pipeline to interface.</p>',
    unsafe_allow_html=True,
)
st.markdown(
    f'''
    <div class="contact-row">
        <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>
        <a href="{CONTACT['github']}" target="_blank">{CONTACT['github_label']}</a>
    </div>
    ''',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------

st.markdown('<p class="section-title">About</p>', unsafe_allow_html=True)
st.markdown(
    '''
    <p class="bio">
    I'm a Computer Science / Software Engineering student and product designer moving into
    AI/ML and data engineering. My background is in designing end-to-end platforms for the
    entertainment industry — casting flows, hiring pipelines, and production management systems —
    and I now build and deploy AI-powered applications, from ML dashboards to LLM-driven tools,
    while keeping the same product-design discipline in how they're structured and used.
    </p>
    ''',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Skills
# ---------------------------------------------------------------------------

st.markdown('<p class="section-title">Skills</p>', unsafe_allow_html=True)
cols = st.columns(2)
for i, (group, items) in enumerate(SKILLS):
    with cols[i % 2]:
        st.markdown(
            f'''
            <div class="skill-group">
                <div class="skill-group-title">{group}</div>
                <div class="skill-list">{" · ".join(items)}</div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------------------------
# Live projects
# ---------------------------------------------------------------------------

st.markdown('<p class="section-title">Deployed apps</p>', unsafe_allow_html=True)

cards_html = "".join(
    f'''
    <div class="project-card">
        <div>
            <div class="project-name">{p['name']}</div>
            <p class="project-note">{p['note']}</p>
        </div>
        <a class="project-link" href="{p['url']}" target="_blank">Open live app</a>
    </div>
    '''
    for p in LIVE_PROJECTS
)
st.markdown(f'<div class="project-grid">{cards_html}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Case studies
# ---------------------------------------------------------------------------

st.markdown('<p class="section-title">Product &amp; design case studies</p>', unsafe_allow_html=True)
for c in CASE_STUDIES:
    st.markdown(
        f'''
        <div class="case-row">
            <div class="case-name">{c['name']}</div>
            <div class="case-role">{c['role']}</div>
            <p class="case-note">{c['note']}</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.markdown(
    f'''
    <div class="footer">
        Areesh Rashid — {CONTACT['email']} — <a href="{CONTACT['github']}" target="_blank">{CONTACT['github_label']}</a>
    </div>
    ''',
    unsafe_allow_html=True,
)
