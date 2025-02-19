import streamlit as st
import json

# read the results from the json file
with open('results.json', 'r') as f:
    results = json.load(f)
    print(results)
    
def main():
    # Sidebar
    st.sidebar.title("Audio Selector")
    audio_files = list(results.keys())

    # If no audio files found, just display a message
    if not audio_files:
        st.write("No audio files found.")
        return

    # Select an audio file from the sidebar
    selected_audio = st.sidebar.selectbox("Select an audio file:", audio_files)

    # Main Page
    st.title("Audio Transcription and Summarization")
    st.subheader(selected_audio)

    # Original Transcript
    st.write("### Transcripción directa")
    st.write(results[selected_audio]['original_transcript'])

    # Table-like display with 2 columns: Without Extra Text | With Extra Text
    # Row 1 -> Refined transcripts
    # Row 2 -> Summaries
    st.write("---")
    
    # Create two columns
    col1, col2 = st.columns(2)

    # Row 1: Transcripciones refinadas
    with col1:
        st.write("#### Transcripción")
        st.write(results[selected_audio]['refined_transcript'])
    with col2:
        st.write("#### Transcripción (con Extra)")
        st.write(results[selected_audio]['refined_transcript_withImagination'])

    st.write("---")

    # Create two columns again for summaries
    col3, col4 = st.columns(2)

    # Row 2: Summaries
    with col3:
        st.write("#### Resumen")
        st.write(results[selected_audio]['summary_transcript'])
    with col4:
        st.write("#### Resumen con Imaginación")
        st.write(results[selected_audio]['summary_transcript_withImagination'])


if __name__ == "__main__":
    main()