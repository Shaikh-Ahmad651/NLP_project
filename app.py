import streamlit as st
from slang_detector import detect_slang
from detector import detect_word_ambiguity
from context_ambiguity import detect_contextual_ambiguity
from output_formatter import format_ambiguity_results

# Set up the web page
st.set_page_config(page_title="NLP Ambiguity Scanner", page_icon="🔍", layout="centered")

st.title("🔍 Linguistic Ambiguity & Slang Detector")
st.markdown("Enter a sentence below to analyze it using your custom NLP pipeline.")

# Text input box for the user
sentence = st.text_input("Enter a sentence to analyze:", placeholder="e.g., he sat near the bank .")

# Button to trigger the analysis
if st.button("Analyze Sentence"):
    if not sentence.strip():
        st.warning("Please enter a sentence first!")
    else:
        with st.spinner("Running NLP models..."):
            
            # --- Slang Detection ---
            st.subheader("=== Slang Detection ===")
            slang_results = detect_slang(sentence)
            if not slang_results:
                st.write("slang no detection")
            else:
                for word, meaning in slang_results.items():
                    st.write(f"**{word}** : {meaning}")

            st.divider() # Adds a clean visual line between sections

            # --- Word-Level Ambiguity ---
            st.subheader("=== Word-Level Ambiguity ===")
            word_ambiguity_results = detect_word_ambiguity(sentence)
            # Using st.text to preserve the exact spacing from your output_formatter
            st.text(format_ambiguity_results(word_ambiguity_results).strip())
            
            st.divider()

            # --- Contextual Ambiguity ---
            st.subheader("=== Contextual Ambiguity ===")
            is_ambiguous, ambiguous_words = detect_contextual_ambiguity(sentence)
            
            st.write(f"**ambiguity detected : {'yes' if is_ambiguous else 'no'}**")
            
            if is_ambiguous:
                for word, meanings in ambiguous_words.items():
                    st.markdown(f"**ambigous word : {word}**")
                    for i, meaning in enumerate(meanings, 1):
                        # Using HTML spaces (&nbsp;) to create the indentation you asked for
                        st.markdown(f"&nbsp;&nbsp;&nbsp;{i}. {meaning}")