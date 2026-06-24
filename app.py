import streamlit as st

from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from orchestrator import LegalOrchestrator
from document_processor.pdf_reader import extract_text_from_pdf
from document_processor.text_cleaner import clean_text


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="LegalMind AI",
    page_icon="⚖️",
    layout="wide"
)

# ------------------------------------------------
# SESSION MEMORY
# ------------------------------------------------

if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    max-width:1400px;
}

.main {
    background-color:#0f172a;
}

.hero {
    padding:50px;
    border-radius:24px;
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );
    text-align:center;
    margin-bottom:30px;
}

.hero h1{
    font-size:56px;
    color:white;
    margin-bottom:10px;
}

.hero p{
    font-size:20px;
    color:#94a3b8;
}

.metric-card{
    background:#111827;
    padding:25px;
    border-radius:18px;
    text-align:center;
    border:1px solid #1e293b;
}

.metric-card h2{
    color:white;
}

.metric-card p{
    color:#94a3b8;
}

.result-card{
    background:#111827;
    padding:30px;
    border-radius:18px;
    border:1px solid #1e293b;
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:14px;
    font-size:18px;
    font-weight:600;
}

section[data-testid="stSidebar"]{
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# PDF GENERATOR
# ------------------------------------------------

def create_pdf(report_text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "Legal Analysis Report",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1, 20))

    for line in report_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        paragraph = Paragraph(
            line.replace("#", ""),
            styles["BodyText"]
        )

        story.append(paragraph)

        story.append(Spacer(1, 8))

    doc.build(story)

    buffer.seek(0)

    return buffer

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.title("LegalMind AI")

    st.markdown("---")

    st.subheader("Recent Analyses")

    if len(st.session_state.analysis_history) == 0:

        st.caption("No documents analyzed.")

    else:

        for item in reversed(
                st.session_state.analysis_history):

            st.write(item["file_name"])

    st.markdown("---")

    if st.button("Clear Session"):

        st.session_state.analysis_history = []

        st.rerun()

    st.markdown("---")

    st.info(
        "Enterprise Legal Intelligence Platform"
    )

# ------------------------------------------------
# HERO SECTION
# ------------------------------------------------

st.markdown("""
<div class='hero'>

<h1>LegalMind AI</h1>

<p>
Enterprise Legal Intelligence Platform
</p>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Legal Document",
    type=["pdf"]
)

# ------------------------------------------------
# PROCESS
# ------------------------------------------------

if uploaded_file:

    with st.spinner("Processing document..."):

        raw_text = extract_text_from_pdf(
            uploaded_file
        )

        cleaned_text = clean_text(
            raw_text
        )

    st.success("Document processed successfully.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class='metric-card'>
        <p>Words</p>
        <h2>{len(cleaned_text.split())}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='metric-card'>
        <p>Characters</p>
        <h2>{len(cleaned_text)}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='metric-card'>
        <p>AI Agents</p>
        <h2>5</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("Preview Extracted Text"):

        st.write(cleaned_text[:5000])

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Analyze Document"):

        orchestrator = LegalOrchestrator()

        with st.spinner(
                "Running Multi-Agent Analysis..."):

            results = orchestrator.analyze_document(
                cleaned_text
            )

        st.session_state.analysis_history.append(
            {
                "file_name": uploaded_file.name,
                "report": results["report"]
            }
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            "<h2>Analysis Results</h2>",
            unsafe_allow_html=True
        )

        sections = {
            "Executive Summary":
                results["summary"],

            "Clauses":
                results["clauses"],

            "Risk Assessment":
                results["risks"],

            "Compliance":
                results["compliance"],

            "Final Report":
                results["report"]
        }

        for title, content in sections.items():

            with st.expander(title, expanded=False):

                st.markdown(content)

        pdf = create_pdf(
            results["report"]
        )

        st.download_button(
            label="Download Report as PDF",
            data=pdf,
            file_name="legal_analysis_report.pdf",
            mime="application/pdf"
        )