from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("final_logistic_modelEMOTIONS.pkl")
vectorizer = joblib.load("tfidf_EMOTIONS.pkl")


# Reverse mapping (model output → emotion label)
emotion_map = {
    0: "sadness",
    1: "anger",
    2: "love",
    3: "surprise",
    4: "fear",
    5: "joy"
}

# Emotion prediction function
def predict_emotion(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)[0]

    return emotion_map.get(pred, "Unknown Emotion")

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None

    if request.method == "POST":
        user_text = request.form["text"]
        emotion = predict_emotion(user_text)

    return render_template("index.html", emotion=emotion)

if __name__ == "__main__":
    app.run(debug=True)