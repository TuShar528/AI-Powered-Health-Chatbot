from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import nltk

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Load AI Model
nltk.download('punkt')
qa_pipeline = pipeline("question-answering", model="deepset/bert-large-uncased-whole-word-masking-squad2")

# ✅ Medical Context
medical_context = """
Fever is a sign that your body is fighting an infection. It can be caused by viral infections, bacterial infections, or other underlying conditions.
Mild fevers (below 102°F or 39°C) can usually be treated with rest, hydration, and over-the-counter medications.
If a fever is above 102°F (39°C) or lasts for more than three days, medical attention is recommended.
Headaches can result from dehydration, stress, or sinus infections. Drinking water, getting enough sleep, and reducing screen time may help.
Persistent coughing can be due to colds, flu, allergies, or respiratory infections. Staying hydrated and using throat lozenges can provide relief.
Muscle pain in the legs can result from overuse, nerve issues, or circulatory problems. If swelling or numbness occurs, consult a doctor.
"""

# ✅ Define Request Format
class ChatRequest(BaseModel):
    query: str

# ✅ Define Chatbot Route
@app.post("/healthbot")
async def chatbot(request: ChatRequest):
    try:
        response = qa_pipeline(question=request.query, context=medical_context)  # ✅ Fix applied here
        return {"response": response["answer"]}
    except Exception as e:
        return {"response": "⚠️ Sorry, I couldn't process your request. Please try again later."}

# ✅ Run this API using: python -m uvicorn api:app --reload
