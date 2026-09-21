import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import utils



root = tk.Tk()

root.title("A SINGLE RECOMANDATION MoViE !")
root.configure(background="grey")
root.minsize(500, 500)
root.maxsize(1000, 1000)

# Create a text

custom_font = tkFont.Font(family="Arial", size=20)

consigne = tk.Label(root, text=" Select the type of movie you want to watch : \n " ,font=custom_font)
consigne.pack()

# creat frame 

frame = tk.Frame(root, width=800, height=800 , bg='grey')
frame.pack(padx= 0, pady= 0)


#display button of genre 

def display_button_genre (dict_genre):
    row= 0
    column= 0
    for txt in dict_genre:
        display_genre = tk.Button(frame, text= txt , height= 3).grid(row=row , column = column)
        column+=1
        if column == 5: 
            column = 0
            row+=1



display_button_genre( utils.retrieve_dict_genre())









# image_ = ImageTk.PhotoImage(
#     Image.open("C:/Users/PC/Desktop/code/a_single_movie_proposition/bg_2.jpeg")
# )
# label = tk.Label(root, image=image_)
# label.pack()





root.mainloop()
