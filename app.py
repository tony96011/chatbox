# app.py
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    "++al8e/Oq1912ElMIKDdudgg1DVtY5bQhVmDCuNC8i5/mUSZRDXe42DHbb//Tdpv5NawwsnhJ4CPWK+MUAF440A9V7Ry/oaPXKhr4a9f5UXXRZfihJe712p2x8mvljN5fe7mibxDKrciF5RXqivO2QdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("9b8392432efef9d28bba91a5bb95f15b")


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
    app.run()
