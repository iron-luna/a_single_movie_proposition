import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import utils



root = tk.Tk()

root.title("A SINGLE RECOMANDATION MoViE !")
root.configure(background="black")
root.minsize(500, 500)
root.maxsize(1000, 1000)

# Create a text

custom_font = tkFont.Font(family="Arial", size=20)

consigne = tk.Label(root, text=" Select the type of movie you want to watch  (max= 4): \n " ,font=custom_font)
consigne.pack()

# creat frame 

frame = tk.Frame(root, width=800, height=800 , bg='grey')
frame.pack(padx= 0, pady= 0)


frame_1 =tk.Frame(root, width=200, height=400 , bg='yellow')
frame_1.pack(padx= 0, pady= 0)


frame_2 = tk.Frame(root, width=400, height=300 , bg='black')
frame_2.pack(padx= 0, pady= 0)

choice_= []
indication_selection_txt = []
def choice(txt):
    global choice_
    global indication_selection_txt
    temporary = None

    if txt not in choice_  and len(choice_) <= 3:
        choice_.append(txt)
        custom_font_1 = tkFont.Font(family="Georgia", size=13)
    
        temporary = tk.Label(frame_2, text= f"{txt} , "  ,font=custom_font_1)
        temporary.pack(side= "left")
        indication_selection_txt.append(temporary)
    else:
        return

    print(choice_)





def erase_choice():

    global choice_ 
    global frame_2


    frame_2.destroy()
    frame_2 = tk.Frame(root, width=400, height=300 , bg='black')
    frame_2.pack(padx= 0, pady= 0)


    choice_ = []



#display button of genre 

def display_button_genre (dict_genre):
    row= 0
    column= 0
    for txt in dict_genre:
        display_genre = tk.Button(frame, text= txt , height= 3 , command = lambda txt = txt : choice(txt) ).grid(row=row , column = column)
        column+=1
        if column == 5: 
            column = 0
            row+=1



display_button_genre( utils.retrieve_dict_genre())


erase_choce_button = tk.Button(frame_1, text= "EFFACER LA SELECTION" , height= 3 , command = lambda : erase_choice())
erase_choce_button.pack()


print(choice_)
print(indication_selection_txt)




# image_ = ImageTk.PhotoImage(
#     Image.open("C:/Users/PC/Desktop/code/a_single_movie_proposition/bg_2.jpeg")
# )
# label = tk.Label(root, image=image_)
# label.pack()





root.mainloop()
