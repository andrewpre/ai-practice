from flask import Flask, request

app = Flask(__name__)

# Inbound messages (user → you)
@app.route('/webhooks/inbound', methods=['POST'])
def inbound_sms():
    data = request.form or request.json
    print("Inbound SMS:", data)
    return "OK", 200

# Status updates (Vonage → you about sent messages)
@app.route('/webhooks/status', methods=['POST'])
def message_status():
    data = request.form or request.json
    print("Status update:", data)
    return "OK", 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)