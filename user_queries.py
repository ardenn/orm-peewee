from users_db import MyUser

if __name__ == '__main__':
    for my_user in MyUser.select():
        user_dict = my_user.__dict__["_data"]
        print("Email {username} at {email}".format(**user_dict))
        print("{username} is beautiful: {is_beautiful}".format(**user_dict))

    is_rouma = MyUser.select().where(MyUser.username == "rouma")
    for usr in is_rouma:
        print(
            "Username: {username} Email: {email}".format(
                **usr.__dict__["_data"]))

    not_a_child = MyUser.select().where(MyUser.age > 19)
    for child in not_a_child:
        print(
            "Child: {username} Email: {email}".format(
                **child.__dict__["_data"]))
