import json

from flask import Flask
from peewee import Model, CharField, AutoField, PostgresqlDatabase

app = Flask(__name__)

db = PostgresqlDatabase('reviews', host='localhost', user='postgres')


class Album(Model):
    id = AutoField()
    title = CharField()
    title_en = CharField()

    class Meta:
        database = db


@app.route("/")
def hello():
    albums = list(Album.select())
    albums = {album.id: album.title for album in albums}
    return json.dumps(albums)


if __name__ == '__main__':
    db.connect()
    db.create_tables(models=[Album])
    album1 = Album(title='hello', title_en='hello')
    album1.save()
    album2 = Album(title='world', title_en='world')
    album2.save()
    db.commit()
    albums = list(Album.select())
    albums = {album.id: album.title for album in albums}
    print(albums)
    app.run(port=7777)
