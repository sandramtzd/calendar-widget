from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://calendar-widget-backend.onrender.com"])

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route('/')
def home():
    return "Calendar API is running!"

# Alias for frontend to fetch from /events (more intuitive)
@app.route('/events', methods=['GET'])
def get_calendar_events():
    calendar_id = request.args.get('calendarId')
    if not calendar_id:
        return jsonify({'error': 'Missing calendarId'}), 400

    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"
    params = {
        'key': GOOGLE_API_KEY,
        'maxResults': 20,
        'orderBy': 'startTime',
        'singleEvents': True,
        'timeMin': '2024-01-01T00:00:00Z'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)