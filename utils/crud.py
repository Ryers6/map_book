def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user["name"]} opublikował: {user["posts"]}")

def add_new_user(users: list)->None:
    new_name: str = input("Enter your name: ")
    new_surname: str = input("Enter your surname: ")
    new_posts: str = int(input("Enter your posts: "))
    new_user: dict = {"name": new_name, "surname": new_surname, "posts": new_posts}
    print(new_user)
    users.append(new_user)