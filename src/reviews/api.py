import json

from flask import Flask, request, jsonify
from reviews.model import db, Album, Reader, Reviews

app = Flask(__name__)


@app.before_request
def db_connect():
    db.connect()


@app.after_request
def db_disconnect(response):
    db.close()
    return response


@app.route("/albums", methods=["GET"])
def get_albums():
    albums = list(Album.select())
    albums = {album.id: album.title_en for album in albums}
    return jsonify(albums), 201, {"Content-Type": "application/json"}


@app.route("/albums", methods=["POST"])
def post_albums():
    album_request = json.loads(request.data)
    album = Album(**album_request)
    album.save()
    return jsonify({"album_id": album.id}), 201, {'Content-Type': 'application/json'}


@app.route("/readers", methods=["GET"])
def get_readers():
    readers = list(Reader.select())
    readers = {reader.id: reader.first_name for reader in readers}
    return jsonify(readers), 201, {"Content-Type": "application/json"}


@app.route("/readers", methods=["POST"])
def post_readers():
    reader_request = json.loads(request.data)
    reader = Reader(**reader_request)
    reader.save()
    return jsonify({"reader_id": reader.id}), 201, {'Content-Type': 'application/json'}


@app.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = list(Reviews.select())
    reviews = {review.id: review.rating for review in reviews}
    return jsonify(reviews), 201, {"Content-Type": "application/json"}


@app.route("/reviews", methods=["POST"])
def post_reviews():
    reviews_request = json.loads(request.data)
    review = Reviews(**reviews_request)
    review.save()
    return jsonify({"review_id": review.id}), 201, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(port=7777)
