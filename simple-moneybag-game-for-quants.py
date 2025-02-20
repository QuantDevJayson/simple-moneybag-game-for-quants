"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Simple MoneyBag Game For Quants is an interactive investment quiz game 
designed for quantitative finance enthusiasts. Motivated by knowledge 
pursuit penalized with acts of kindness.

@Author: QuantDevJayson
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import streamlit as st
import random
import openai
import speech_recognition as sr
import tempfile

# OpenAI API key (Replace with your own key)
OPENAI_API_KEY = "your-opeai-key"
openai.api_key = OPENAI_API_KEY

def generate_quiz_question():
    prompt = "Generate a multiple-choice investment-related question with four options and the correct answer. Format: Question|Option A|Option B|Option C|Option D|Correct Option"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a finance expert generating investment-related quiz questions."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"].strip().split("|")

def generate_tongue_twister():
    prompt = "Generate a fun and challenging tongue twister."
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a creative language generator."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"].strip()

def validate_audio(audio_file, expected_text):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio_data)
        return expected_text.lower() in transcript.lower()
    except sr.UnknownValueError:
        return False

st.title("Simple MoneyBag Game for Quants")

if "score" not in st.session_state:
    st.session_state.score = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = None
if "target_score" not in st.session_state:
    st.session_state.target_score = None
if "current_round" not in st.session_state:
    st.session_state.current_round = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

if st.session_state.rounds is None or st.session_state.target_score is None:
    st.session_state.rounds = st.number_input("Enter number of rounds you want to play:", min_value=1, step=1)
    st.session_state.target_score = st.number_input("Set your target score:", min_value=10, step=10)
    st.write("Press 'Start Game' when ready!")
    if st.button("Start Game"):
        st.experimental_rerun()

if not st.session_state.game_over:
    quiz_data = generate_quiz_question()
    question = quiz_data[0]
    options = quiz_data[1:5]
    correct_answer = quiz_data[5]
    tongue_twister = generate_tongue_twister()

    st.write(f"**Round {st.session_state.current_round + 1}/{st.session_state.rounds}**")
    st.write(f"**Question:** {question}")
    selected_option = st.radio("Choose an option:", options)

    if st.button("Submit"):
        if selected_option == correct_answer:
            st.success("Correct! 🎉 +10 points")
            st.session_state.score += 10
        else:
            st.error(f"Incorrect. The correct answer was {correct_answer}. -5 points (unless you redeem!)")
            st.write(f"Say the following tongue twister clearly to avoid the penalty: \"{tongue_twister}\"")
            uploaded_file = st.file_uploader("Upload your audio file (WAV format)", type=["wav"])
            if uploaded_file is not None:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                    temp_audio.write(uploaded_file.getbuffer())
                    temp_audio_path = temp_audio.name
                
                if validate_audio(temp_audio_path, tongue_twister):
                    st.success("Well done! No penalty applied.")
                else:
                    st.error("Audio unclear. -5 points applied.")
                    st.session_state.score -= 5
        
        st.session_state.current_round += 1
        if st.session_state.current_round >= st.session_state.rounds:
            st.session_state.game_over = True
        st.experimental_rerun()

if st.session_state.game_over:
    st.write(f"Game over! Your final score: {st.session_state.score}")
    if st.session_state.score < st.session_state.target_score:
        penalty_amount = (st.session_state.target_score - st.session_state.score) * 5
        st.warning(f"You did not reach your target! You must donate ${penalty_amount} to a charitable cause nearby.")
    else:
        st.success("Congratulations! You met your target score! 🎉")
 