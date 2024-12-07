from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
with open("sentiment_analysis_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        if request.method == "POST":
            # Get inputs from the form
            feature1 = request.form.get("feature1", "")
            feature2 = request.form.get("feature2", "")

            # Combine inputs for prediction
            combined_input = feature1 + " " + feature2

            # Transform input using the vectorizer
            transformed_input = vectorizer.transform([combined_input])

            # Get prediction and probabilities
            prediction = model.predict(transformed_input)
            prediction_proba = model.predict_proba(transformed_input)[0]

            # Interpret results
            sentiment = (
                "Positive" if prediction[0] == 1 else
                "Negative" if prediction[0] == -1 else
                "Neutral"
            )
            probabilities = {
                "Positive": round(prediction_proba[1], 2) if len(prediction_proba) > 1 else 0.0,
                "Negative": round(prediction_proba[0], 2),
                "Neutral": round(prediction_proba[2], 2) if len(prediction_proba) > 2 else 0.0,
            }

            # Set notification priority based on sentiment
            notification_priority = "Yes" if sentiment == "Positive" else "No"

            return render_template(
                "index.html",
                sentiment=sentiment,
                probabilities=probabilities,
                notification_priority=notification_priority,
            )
        else:
            return render_template("index.html")

    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    app.run(debug=True)
