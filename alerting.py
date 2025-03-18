import requests

def send_alert(message):
    """
    Send real-time alerts via Slack.
    """
    url = "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL"
    payload = {"text": message}
    requests.post(url, json=payload)

# Example usage
if __name__ == "__main__":
    send_alert("Alert: Suspicious login detected!")
