import requests
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
MQTT_PORT = 1883
TOPIC = "savonia/iot/temperature"

# Replace these with your real Telegram bot token and chat ID
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

THRESHOLD = 28.0


def send_telegram(message: str) -> None:
    if TOKEN == "YOUR_TELEGRAM_BOT_TOKEN" or CHAT_ID == "YOUR_CHAT_ID":
        print("Telegram token/chat ID not configured yet.")
        print("Telegram alert message would be:", message)
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("Telegram alert sent successfully.")
    except requests.RequestException as error:
        print("Failed to send Telegram alert:", error)


def on_message(client, userdata, msg) -> None:
    try:
        temperature = float(msg.payload.decode().strip())
    except ValueError:
        print("Invalid temperature received:", msg.payload.decode(errors="ignore"))
        return

    print("Temperature:", temperature)

    if temperature > THRESHOLD:
        alert = f"ALERT: High temperature {temperature} °C"
        print(alert)
        send_telegram(alert)


def main() -> None:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(BROKER, MQTT_PORT)
    client.subscribe(TOPIC)

    print(f"Subscribed to topic: {TOPIC}")
    print(f"Alert threshold: {THRESHOLD} °C")
    client.loop_forever()


if __name__ == "__main__":
    main()
