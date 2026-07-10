from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

with open('weight_height_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return "Height Predicter Api"

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    weight = data['weight']
    wt = np.array(weight).reshape(-1, 1)

    scaled_weight = scaler.transform(pd.DataFrame(wt))
    # scaled_weight = scaler.transform(pd.DataFrame([[weight]])) #when weight is a single value not list/array
    prediction = model.predict(scaled_weight)

    return jsonify({
        "weight": weight,
        "predicted_height":prediction.tolist()
    })



if __name__ == "__main__":
    app.run(debug=True)