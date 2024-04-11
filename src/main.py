"""Main module for the Flask application"""
from flask import Flask, request, jsonify
from utils.service_utils import get_available_port
from insights_from_audio import get_insights_from_audio_url_using_regex

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_insights_from_resource():
    """Get insights from a resource"""
    try:
        request_body = request.json

       

        interaction_url = request_body['interaction_url']
        trackers = request_body['trackers']
        insights_data = get_insights_from_audio_url_using_regex(interaction_url, trackers)
        return jsonify({"insights":insights_data})
    except Exception:
        return "We had a problem to process the requested url with the given trackers", 500


if __name__ == '__main__' :
    port = get_available_port()
    app.run(port=port)
