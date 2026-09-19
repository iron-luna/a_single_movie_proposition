import requests
import ast
import random

api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YzUzM2U3NWFhNmM5MWZhMTg0MjBmMDczMDMwZTIyZCIsIm5iZiI6MTc4ODA4NDk5NS4xMiwic3ViIjoiNmE5NDAzMDM2NzkwYjY3NDFkZGQxNjQxIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.1YaqCF0SwU4ZZlh2cITcTyaZ4EZYF2ZG51FtB8JhiqE"

def request_api_id ():

    url = "https://api.themoviedb.org/3/authentication"

    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    return response.text


request_api_id()


# requete qui renvoie tout les genres cinématographiques

def dict_movie_genre_id():


    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization":  f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)

    # convert  response : class = str into  Dict

    response = response.text
    response = ast.literal_eval(response)

    dict_genre = response 
    return dict_genre




#nettoyage pour ne garder que la liste des genres et un dictionnaire comprenant comme valeur l id du genre:

def clean_dict(dict):
    dict_temporary = {}
    dict_genre_id ={}
    value = str
    for key in dict : 
        for value in dict[key]:
            value = str(value)
            value=value.split("'")
            dict_temporary.update({value[5] : value[2]})
            dict_movie_genre_id = dict_temporary


    for key in dict_temporary: # garder dans la valeur de la clés que le nbr (filtrer les autre caractere)
        value  =  "".join([char for char in dict_temporary[key] if char.isdigit()])
        value = int(value)
        dict_movie_genre_id.update({key: value})

    return dict_movie_genre_id




# function qui met tout les clés en minuscules

def lower_dict(d):
    new_dict = dict((k.lower(), v) for k, v in d.items())
    return new_dict





# # avoir la liste avec les id de tout les films dasn tel catagegoris puis tirer au hhasrad un id 



def choice_genre ():   # demande a l utilisateur le genre de film voulu

    for key in clean_genre_dict_lower :
        print(key)
        print("\n")
    choice_genre = input("write the type of movie you want to watch : \n ")

    # permet de determiner le numero du genre (id)
    try:
        id = clean_genre_dict_lower [choice_genre]
        return id

    except KeyError:
        id = None
        print(" Genre non trouver dans la liste , erreur lors de la saisie : recommancer ")
        



def display_selection_movie (id):  # affiche la premiere page de selection  du genre de film choisis

     headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}" } 

     url = f"https://api.themoviedb.org/3/discover/movie?with_genres={id}&language=fr-FR"
     request_api_id()
     responses = requests.get(url, headers=headers)

     responses = responses.json()
     dict_movie = responses
     return dict_movie






def random_movie(nbr_p):
     
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}" } 

    random_page= random.randint(1, 500)

    url = f"https://api.themoviedb.org/3/discover/movie?with_genres={id}&language=fr-FR&page={random_page}"
    responses = requests.get(url, headers=headers)

    responses = responses.json()
    dict_movie = responses
    list_movie= dict_movie['results']
    random_number = random.randint(0, 19)
    final_movie = list_movie[random_number]
    
    return final_movie

    # random_ = random.randint(1, len(dict_movie))
    # selection = list(dict_movie.values())[random_ - 1]
    # return selection
 
version_1_dict = dict_movie_genre_id()
clean_dict_genre = clean_dict(version_1_dict)
clean_genre_dict_lower = lower_dict(clean_dict_genre)
id =choice_genre()
dict_movie_selection = display_selection_movie(id)
number_total_of_page = dict_movie_selection["total_results"]
print(number_total_of_page)
print(random_movie(number_total_of_page))




