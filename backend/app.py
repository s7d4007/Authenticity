import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY")
GOOGLE_API_URL = f"https://safebrowsing.googleapis.com/v5/uris:search?key={API_KEY}"

# 2. Setup the Flask App
app = Flask(__name__)
CORS(app)

# 3. The Check Route
@app.route('/api/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url_to_check = data.get('url')

    if not url_to_check:
        return jsonify({"error": "URL is required"}), 400

    # Prepare the payload for Google Safe Browsing v5 (Updated on 16th March 2026)
    payload = {
        "uri": url_to_check,
        "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"]
    }

    try:
        # Send request to Google
        response = requests.post(GOOGLE_API_URL, json=payload)
        response_data = response.json()
        
        # Check if there are threats
        # v5 API returns threat information in the response
        threats = response_data.get('threats', [])

        if threats:
            # THREAT FOUND
            threat_type = threats[0].get('threatType', 'UNKNOWN')
            return jsonify({
                "status": "dangerous",
                "title": "Dangerous Link Detected",
                "message": f"This URL is flagged as {threat_type.replace('_', ' ')}. Do not visit."
            })
        else:
            # SAFE
            return jsonify({
                "status": "safe",
                "title": "No Threats Found",
                "message": "Google Safe Browsing has not flagged this URL as dangerous."
            })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            "status": "error",
            "title": "Server Error",
            "message": "Could not connect to the security database."
        }), 500

# 4. Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)