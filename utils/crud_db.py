import psycopg2
import requests
from bs4 import BeautifulSoup

db_params=psycopg2.connect(
    database="postgres",
    user="postgres",
    password='postgres',
    host="localhost",
    port="5432"
)

def get_cords(miejscowosc) -> list:
    url: str = f"https://pl.wikipedia.org/wiki/{miejscowosc}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, "html.parser")
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    return [latitude, longitude]

def add_new_to_table(db_params) -> None:
    imie = input('Imie: ')
    nazwisko = input('Nazwisko: ')
    posts = input('Post: ')
    miejscowosc = input('Miejscowosc: ')

    longitude, latitude=get_cords(miejscowosc)

    sql_add_query=f"INSERT INTO public.users(name, surname, posts, location, cords)VALUES ('{imie}', '{nazwisko}', '{posts}', '{miejscowosc}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

# add_new_to_table(db_params)

def show_users(db_params) -> None:
    sql_add_query=f"SELECT * FROM public.users"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    users=cursor.fetchall()
    # print(users)
    # db_params.commit()
    for user in users:
        print(user)

# show_users(db_params)


# DELETE FROM public.users
# 	WHERE id=2


def remove_users(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query=f"DELETE FROM public.users where name='{input('Imie: ')}'; "
    cursor.execute(sql_remove_query)
    db_params.commit()

def get_user_id(db_params) -> None:
    print('Kogo aktualizować? ')
    sql_add_query = f"SELECT * FROM public.users where name='{input('Imie: ')}'"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    id = cursor.fetchall()[0][0]
    return id
# get_user_id(db_params)

def update_users(db_params) -> None:
    cursor = db_params.cursor()
    imie = input('new Imie: ')
    nazwisko = input('new Nazwisko: ')
    posts = input('new Post: ')
    miejscowosc = input('new Miejscowosc: ')

    longitude, latitude = get_cords(miejscowosc)

# update_users(db_params)






