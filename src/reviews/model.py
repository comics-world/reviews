from peewee import Model, CharField, AutoField, PostgresqlDatabase

db = PostgresqlDatabase('reviews', host='localhost', user='postgres')


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    id = AutoField()
    title = CharField()
    title_en = CharField()


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
