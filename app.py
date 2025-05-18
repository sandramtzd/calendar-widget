from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route('/')
def home():
    return "Calendar API is running!"

@app.route('/calendar', methods=['GET'])
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

    response = requests.get(url, params=params)
    return jsonify(response.json())