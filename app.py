import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


@app.route("/")
def index():
    return render_template("index.html", api_key=GOOGLE_MAPS_API_KEY)


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    # This endpoint can be used for custom logic if needed
    return jsonify([])


@app.route("/store", methods=["POST"])
def store_place():
    place_id = request.form.get("place_id")
    place_details = get_place_details(place_id)

    if place_details:
        place_name = place_details.get("name")
        place_lat = place_details["geometry"]["location"]["lat"]
        place_lng = place_details["geometry"]["location"]["lng"]

        print(f"Storing Place ID: {place_id}")
        print(f"Place Name: {place_name}")
        print(f"Latitude: {place_lat}")
        print(f"Longitude: {place_lng}")

        return (
            jsonify(
                {
                    "place_id": place_id,
                    "name": place_name,
                    "latitude": place_lat,
                    "longitude": place_lng,
                }
            ),
            200,
        )

    return {}, 204


def get_place_details(place_id: str) -> dict:
    url = (
        "https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={place_id}&key={GOOGLE_MAPS_API_KEY}"
    )
    response = requests.get(url)
    response.raise_for_status()
    result = response.json().get("result")
    return result


if __name__ == "__main__":
    app.run(debug=True)
