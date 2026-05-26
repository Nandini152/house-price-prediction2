from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Form values
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])

    # DataFrame create
    data = pd.DataFrame({
        "Area_sqft": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms]
    })

    # Prediction
    prediction = model.predict(data)

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

# Run app
if __name__ == "__main__":
    app.run(debug=True)