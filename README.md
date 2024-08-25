# Flask Line Bot API Project

This project is a Flask-based web server that integrates with the Line Messaging API and Dify service. It handles incoming webhook events from Line and processes them using the Dify service.

## Prerequisites

- Python 3.6+
- Flask
- Requests
- Python-dotenv
- Line-bot-sdk

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables:

    ```env
    IFY_API_KEY=your_dify_api_key
    LINE_ACCESS_TOKEN=your_line_access_token
    LINE_CHANNEL_SECRET=your_line_channel_secret
    ```

## Running the Application

1. Set the `FLASK_APP` environment variable to `app.py`:

    ```bash
    export FLASK_APP=app.py
    ```

2. Run the Flask development server:

    ```bash
    flask run
    ```

3. To expose your local server to the internet using ngrok:

    ```bash
    ./ngrok http 5000
    ```

4. ngrok will provide you with a public HTTPS URL. Use this URL to set up your Line webhook.

## Project Structure
