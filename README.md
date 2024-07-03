# Google Places Autocomplete Example using Flask + HTMX

Quick demo how to use the Google Places API with a Flask backend and HTMX for dynamic interactions on the frontend.

This app provides an autocomplete feature for places and fetches detailed information about the selected place.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/bbelderbos/google-places-autocomplete-flask.git
    cd google-places-autocomplete-flask
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables. Create a `.env` file in the project root:

    ```bash
    GOOGLE_MAPS_API_KEY=your_actual_api_key
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to see the application in action.

## Usage

- Type a location in the input field to see autocomplete suggestions.
- Select a place from the suggestions to fetch detailed information about it.

## License

This project is licensed under the MIT License.
