import requests
import ast



api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YzUzM2U3NWFhNmM5MWZhMTg0MjBmMDczMDMwZTIyZCIsIm5iZiI6MTc4ODA4NDk5NS4xMiwic3ViIjoiNmE5NDAzMDM2NzkwYjY3NDFkZGQxNjQxIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.1YaqCF0SwU4ZZlh2cITcTyaZ4EZYF2ZG51FtB8JhiqE"

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}
response = requests.get(url, headers=headers)



# requete qui renvoie tout les genres cinématographiques

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

list_genre = [""]
genre_list =[]
dict_genre_id= {}

#nettoyage pour ne garder que la liste des genres et un dictionnaire comprenant comme valeur l id du genre:

for key in dict_genre : 
    for value in dict_genre[key]:
        value = str(value)
        value=value.split("'")
        dict_genre_id.update({value[5] : value[2]})
        genre_list.append(value[5])


# function qui met tout les clés en minuscules

def lower_dict(d):
    new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
    return new_dict


dict_genre_id = lower_dict(dict_genre_id)

# normalisation de la list (enleve les minuscules)

genre_list= str(genre_list)
genre_list = genre_list.lower()
genre_list = genre_list.replace("'" , "")
genre_list = genre_list.replace("[" , "")
genre_list = genre_list.replace("]" , "")
genre_list = genre_list.replace(" ","")
genre_list = genre_list.split(",")
genre_list[14]= "science fiction"
genre_list[15]= "tv movie"


# avoir la liste avec les id de tout les films dasn tel catagegoris puis tirer au hhasrad un id 

choice_genre = input(f"write the type of movie you want to watch : \n  {genre_list} \n")



# permet de determiner le numero du genre (id)
def determine_id (choice_genre):
    cpt= 0
    for w in genre_list :
        print(genre_list[cpt])
        if choice_genre != genre_list[cpt]:
            cpt+=1
        else:
            x= dict_genre_id.get(genre_list[cpt])
            x=x.replace(":","")
            x=x.replace(",","")
            return x
    return "pas dans la genre_list"

 
id=determine_id(choice_genre)

print(id)




# urle= f"https://api.themoviedb.org/3/discover/movie?with_genres={determine_id(choice_genre)}"

# headers = {
#     "accept": "application/json",
#     "Authorization":  f"Bearer {api_key}"
# }
        
# responses = requests.get(urle, headers=headers)



# print(responses.text)
        




