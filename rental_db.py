from peewee import PostgresqlDatabase, Model, CharField, BooleanField, IntegerField, DateTimeField
import datetime

rental_db = PostgresqlDatabase("rental_db", user="rodgers")


class DvdRental(Model):
    movie_name = CharField()
    rental_date = DateTimeField(default=datetime.datetime.now)
    renter_name = CharField()
    return_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = rental_db

if __name__ == '__main__':
    DvdRental.create_table(fail_silently=True)
