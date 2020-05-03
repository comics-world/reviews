import json

from flask import Flask
from peewee import Model, CharField, AutoField, PostgresqlDatabase

app = Flask(__name__)

db = PostgresqlDatabase('reviews', host='localhost', user='postgres')


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    id = AutoField()
    title = CharField()
    title_en = CharField()


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
    return json.dumps(albums)


def create_table_and_data():
    with db:
        db.create_tables(models=[Album])
        album1 = Album(title='hello', title_en='hello')
        album1.save()
        album2 = Album(title='world', title_en='world')
        album2.save()
        db.commit()
        albums = list(Album.select())
        albums = {album.id: album.title for album in albums}
        print(albums)


if __name__ == '__main__':
    app.run(port=7777)
