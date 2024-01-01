from flask import Flask, request, jsonify, make_response, send_file
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import logging
import stripe

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
CORS(app)
bcrypt = Bcrypt(app)

stripe.api_key = "sk_test_51OTRWYAXdYT3W3LFoxV2uHrrbLeelc9k5c8UvTCV21I9wcAJqKkvA0jIrZv9mQP4wPsgHdptOsjmq6JYmBcXCPPO00a0eZwUwA"


@app.route("/v1/payment", methods=['GET'])
def payment():
    intent = stripe.PaymentIntent.create(
        amount=1099,
        currency="usd",
        payment_method="pm_card_visa",
        )
    
    print(intent.client_secret)
    
    return jsonify(intent.client_secret)
    

