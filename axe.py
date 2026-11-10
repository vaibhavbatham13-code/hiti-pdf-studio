# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
    st.title("Studio Settings")
    st.markdown("Configure your AI backend and preferences.")

    api_key = st.text_input(
        "OpenAI API Key (Optional)", type="password",
        help="Leave blank to use simulation mode (no AI, uses only the PDF text).",
    )
    model_choice = st.selectbox("Select AI Model", MODELS)
    use_api = bool(api_key and api_key.startswith("sk-"))

    if use_api:
        st.success(f"Mode: OpenAI ({model_choice})")
    else:
        st.info("Mode: Simulation (no AI). Add an API key for AI answers.")

    st.markdown("---")
    st.markdown("### 💡 Project Guide")
    st.markdown("""
    1. **Upload** any academic paper or technical PDF.
    2. **Explore** the Executive Summary, ELI5 breakdown, and Jargon glossary.
    3. **Chat** directly with the document using the Q&A tab.
    """)
    st.markdown("---")
    st.caption("College Project Edition • Built with Streamlit")
    st.caption("Created by Hiti")
