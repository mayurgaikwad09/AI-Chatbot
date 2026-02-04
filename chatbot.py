from transformers import pipeline
import re

chatbot_model = None

def load_model():
    global chatbot_model
    if chatbot_model is None:
        chatbot_model = pipeline("text-generation", model="distilgpt2")

def clean(text):
    text = re.sub(r"(User:|Bot:)", "", text)
    text = re.sub(r"\s+", " ", text)
    sentences = list(dict.fromkeys(text.split(".")))
    return ". ".join(sentences[:2]).strip() + "."

def get_response(user_input: str) -> str:
    text = user_input.lower()

    # fast friendly replies
    if "how are you" in text:
        return "I’m doing great 😊 How about you?"

    if "who created you" in text:
        return "I was created by Mayur sir as an internship project 🤖"

    load_model()

    prompt = f"Answer clearly in 1-2 sentences:\nQuestion: {user_input}\nAnswer:"

    result = chatbot_model(
        prompt,
        max_new_tokens=40,
        temperature=0.7,
        repetition_penalty=1.4,
        do_sample=True
    )

    reply = result[0]["generated_text"].replace(prompt, "")
    reply = clean(reply)

    if len(reply) < 5:
        return "Sorry, I couldn’t understand that."

    return reply
