
from flask import Flask, jsonify, request

app = Flask(__name__)

events = [
    {"id": 1, "name": "Tech Fest", "date": "2026-11-15"},
    {"id": 2, "name": "Cultural Night", "date": "2026-11-20"},
    {"id": 3, "name": "Coding Workshop", "date": "2026-11-25"}
]

registrations = []


@app.route("/")
def home():
    return jsonify({
        "application": "CampusConnect",
        "message": "Welcome to Campus Event Registration",
        "available_events": len(events)
    })


@app.route("/events")
def get_events():
    return jsonify(events), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip()
    event_id = data.get("event_id")

    if not name or event_id is None:
        return jsonify({
            "error": "Name and event_id are required"
        }), 400

    event = next(
        (e for e in events if e["id"] == event_id),
        None
    )

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    registrations.append({
        "name": name,
        "event_id": event_id
    })

    return jsonify({
        "message": "Registration successful",
        "student": name,
        "event": event["name"]
    }), 201


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
