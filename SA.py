import re
import numpy as np
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import random

class EmotionalIntelligenceAI:
    def __init__(self):
        model_name = "j-hartmann/emotion-english-distilroberta-base"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)


        self.emotions = [
            "anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"
        ]

        self.responses = {
            "anger": [
                "I'm sorry you're feeling this way. Let me know how I can support you.",
                "It sounds like you're upset. I'm here to help if you need it."
            ],
            "disgust": [
                "That sounds unpleasant. Would you like to talk more about it?",
                "I understand this might be frustrating. How can I assist?"
            ],
            "fear": [
                "It's okay to feel this way sometimes. How can I make you feel safer?",
                "I'm here to support you. Let me know how I can help alleviate your worries."
            ],
            "joy": [
                "That's wonderful to hear! I'm glad things are going well for you.",
                "Your happiness is infectious! Keep up the positivity!"
            ],
            "neutral": [
                "Got it. Let me know if there's anything you'd like to discuss.",
                "I appreciate your honesty. How can I assist you further?"
            ],
            "sadness": [
                "I'm sorry you're feeling this way. I'm here to listen if you want to share more.",
                "It seems like you're feeling down. Is there something I can do to help?"
            ],
            "surprise": [
                "Wow! That sounds unexpected. Tell me more about it.",
                "It seems like something caught you off guard. Let’s talk about it."
            ]
        }

    def preprocess_text(self, text):
        text = re.sub(r"[^a-zA-Z\s]", "", text) 
        text = text.lower().strip() 
        return text

    def detect_emotions(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        scores = outputs[0].detach().numpy()
        probs = np.exp(scores) / np.sum(np.exp(scores), axis=1) 


        emotion_probs = {self.emotions[i]: probs[0][i] for i in range(len(self.emotions))}
        top_emotion = max(emotion_probs, key=emotion_probs.get)

        return emotion_probs, top_emotion

    def generate_response(self, emotion):
        if emotion in self.responses:
            return random.choice(self.responses[emotion])
        return "Thank you for sharing. I'm here to help however I can."

    def analyze(self, text):
        cleaned_text = self.preprocess_text(text)
        emotion_probs, top_emotion = self.detect_emotions(cleaned_text)
        response = self.generate_response(top_emotion)

        return {
            "input_text": text,
            "cleaned_text": cleaned_text,
            "detected_emotion": top_emotion,
            "emotion_probabilities": emotion_probs,
            "response": response
        }


if __name__ == "__main__":
    ei_ai = EmotionalIntelligenceAI()
    user_input = input("How are you feeling today? ")
    analysis = ei_ai.analyze(user_input)
    print(f"Detected Emotion: {analysis['detected_emotion'].capitalize()}")
    print(f"Emotion Probabilities: {analysis['emotion_probabilities']}")
    print(f"Response: {analysis['response']}")
