from peewee import (
    Model,
    CharField,
    AutoField,
    PostgresqlDatabase,
    DateField,
    IntegerField,
    TextField,
)

db = PostgresqlDatabase("reviews", host="localhost", user="postgres")


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    id = AutoField()
    title = CharField()
    title_en = CharField()
    magazine_name = CharField()
    date = DateField()


class Reader(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    age = IntegerField()
    phone = CharField()
    email = CharField()


class Reviews(BaseModel):
    id = AutoField()
    album_id = IntegerField()
    reader_id = IntegerField()
    rating = IntegerField()
    details = TextField()
