from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import numpy as np
import joblib
import tensorflow as tf
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load models
risk_model = joblib.load("models/xgboost_spoilage_risk_model.pkl")
anomaly_model = tf.keras.models.load_model("models/autoencoder_model.h5")

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        
        # Make predictions
        risk_score = float(risk_model.predict([[temperature, humidity]])[0])
        
        # Normalize input for anomaly detection
        normalized_input = np.array([[temperature, humidity]])
        normalized_input = (normalized_input - normalized_input.mean()) / normalized_input.std()
        
        # Detect anomalies
        reconstruction = anomaly_model.predict(normalized_input)
        anomaly_score = np.mean(np.power(normalized_input - reconstruction, 2))
        
        return jsonify({
            'status': 'success',
            'risk_score': round(risk_score, 2),
            'anomaly_score': round(float(anomaly_score), 4),
            'is_anomaly': bool(anomaly_score > 0.1),
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
