import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("wokwi/sensor_data")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("\n--- Sensor Readings ---")
        print(f"Temperature: {data['temperature']:.2f} °C")
        print(f"Humidity: {data['humidity']:.2f} %")
        print(f"Heat Index: {data['heatIndex']:.2f} °C")
        print(f"Latitude: {data['latitude']:.6f}")
        print(f"Longitude: {data['longitude']:.6f}")

        if data['temperature'] > 30:
            print("⚠️ WARNING: High Temperature Detected! Take necessary precautions.")
        if data['humidity'] > 80:
            print("⚠️ WARNING: High Humidity Detected! Risk of condensation/mold.")

        print("--- End of Readings ---")
    except json.JSONDecodeError:
        print(f"Received non-JSON message: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883

print(f"Connecting to MQTT broker at {mqtt_broker}:{mqtt_port}")
client.connect(mqtt_broker, mqtt_port, 60)

client.loop_forever()
