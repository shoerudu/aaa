from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SHORT_IO_API_KEY = "pk_Sbb7Is5FppQOdh6E"  # এখানে আপনার Short.io API key দিন
DOMAIN_ID = "waxxsa.short.gy"       # এখানে আপনার ডোমেইন ID দিন

@app.route('/get_stats', methods=['POST'])
def get_stats():
    link_id = request.json.get('link_id')
    url = f"https://api-v2.short.io/statistics/domain/{DOMAIN_ID}/link_clicks"
    headers = {"Authorization": f"Bearer {SHORT_IO_API_KEY}"}
    params = {"ids": link_id}

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
