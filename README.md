# Dify Line Bot 

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
    DIFY_API_KEY=your_dify_api_key
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

- [`app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/app.py"): Main application file that sets up the Flask server and routes.
- [`services/dify.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2Fservices%2Fdify.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/services/dify.py"): Contains the Dify class for interacting with the Dify API.
- [`utils/markdown.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2Futils%2Fmarkdown.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/utils/markdown.py"): Utility functions for processing markdown.
- [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/.env"): Environment variables file.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/requirements.txt"): List of Python packages required for the project.
- [`README.md`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsekaizato%2Fproject%2Fsupport%2Fpko%2Fbot%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/sekaizato/project/support/pko/bot/README.md"): Project documentation.

## Endpoints

- `/`: A simple endpoint to check if the server is running.
- `/api/line`: Endpoint to handle POST requests from the Line webhook.

## License

This project is licensed under The Project One License. See the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Line Messaging API](https://developers.line.biz/en/docs/messaging-api/)
- [Dify](https://dify.ai/)
- [ngrok](https://ngrok.com/)


