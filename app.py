## Import Libraries
# Import Flask fr webserver 
from flask import Flask, request, jsonify
import requests
import json
import os

# Import Dify class 
from services.dify import Dify

from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import re

# Import env
from dotenv import load_dotenv
load_dotenv()

## Start Services
# Dify
d = Dify(os.getenv("DIFY_API_KEY"))
# Line Bot API
line_bot_api = LineBotApi(os.getenv("LINE_ACCESS_TOKEN"))
# Handler for Line Webhook
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

# Start Flask web server
app = Flask(__name__)

# Import Markdown Function
from utils.markdown import remove_emojis, clean_markdown

# API PATH
@app.route('/')
def hello():
    return jsonify({
        'success': True,
        "statusCode": 200,
        "detail": "Success",
        "reason": "OK",

        })

   
# API /POST Receive Line Webhook
@app.route('/api/line', methods=['POST'])
def api_line():
    
    body = request.get_data(as_text=True)
    signature = request.headers['X-Line-Signature']
    
    print(body)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("InvalidSignatureError")

    return 'OK'

# Handler for Line Webhook Response
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    msg = event.message.text
    bot_response = d.sendMessage(msg)
    if (bot_response.get('status') != 400):
       response = bot_response.get('answer')
    else:
       response = "Sorry, Rate Limit Exceeded"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
