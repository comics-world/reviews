from flask import Flask, jsonify
from reviews.model import db, Album

app = Flask(__name__)


@app.before_request
def db_connect():
    db.connect()


@app.after_request
def db_disconnect(response):
    db.close()
    return response


@app.route("/")
def hello():
    albums = list(Album.select())
    albums = {album.id: album.title for album in albums}
    return jsonify(albums), 201, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(port=7777)
