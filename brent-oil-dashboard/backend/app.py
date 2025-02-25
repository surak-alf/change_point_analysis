# backend/app.py
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='../frontend/build')  # Serve static files
CORS(app)

try:
    oil_price_data = pd.read_csv("data/BrentOilPrices.csv")
    event_data = pd.read_csv("data/world_bank_data.csv")

    oil_price_data['Date'] = pd.to_datetime(oil_price_data['Date'])
    event_data['Date'] = pd.to_datetime(event_data['Date'])

except FileNotFoundError:
    print("Error: Data files not found. Place them in the data directory.")
    exit()

@app.route('/api/oil_prices', methods=['GET'])
def get_oil_prices():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    filtered_data = oil_price_data.copy()

    if start_date:
        filtered_data = filtered_data[filtered_data['Date'] >= start_date]
    if end_date:
        filtered_data = filtered_data[filtered_data['Date'] <= end_date]

    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(event_data.to_dict(orient='records'))

@app.route('/api/event_impact/<event_name>', methods=['GET'])
def get_event_impact(event_name):
    try:
        event = event_data[event_data['Event'] == event_name].iloc[0]
        event_date = event['Time']

        window = pd.Timedelta(days=30)
        impact_data = oil_price_data[
            (oil_price_data['Date'] >= event_date - window) &
            (oil_price_data['Date'] <= event_date + window)
        ]
        return jsonify(impact_data.to_dict(orient='records'))
    except IndexError:  # Handle if the event is not found
        return jsonify({"error": "Event not found"}), 404


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)