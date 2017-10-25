from peewee import PostgresqlDatabase, Model, CharField, BooleanField, IntegerField

psql_db = PostgresqlDatabase("class", user="rodgers")


class MyUser(Model):
    age = IntegerField(4)
    username = CharField(20)
    password = CharField(10)
    email = CharField()

    is_beautiful = BooleanField(default=False)

    class Meta:
        database = psql_db


if __name__ == '__main__':
    MyUser.create_table(fail_silently=True)
