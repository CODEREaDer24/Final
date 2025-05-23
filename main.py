from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

listings = []
bids = {}

@app.route("/")
def home():
    return "Welcome to GAREANIT — The Garage Sale Arena!"

@app.route("/list", methods=["POST"])
def create_listing():
    data = request.json
    data["timestamp"] = datetime.utcnow().isoformat()
    data["status"] = "open"
    listings.append(data)
    return jsonify({"message": "Listing created", "listing": data}), 201

@app.route("/bids/<int:listing_id>", methods=["POST"])
def place_bid(listing_id):
    bid_data = request.json
    bid = {
        "amount": bid_data["amount"],
        "user": bid_data["user"],
        "timestamp": datetime.utcnow().isoformat()
    }
    if listing_id not in bids:
        bids[listing_id] = []
    bids[listing_id].append(bid)
    return jsonify({"message": "Bid placed", "bids": bids[listing_id]}), 200

@app.route("/listings", methods=["GET"])
def get_listings():
    return jsonify(listings)