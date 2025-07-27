from tkinter import *
from PIL import ImageTk, Image

# main window object
rpsg = Tk()

# Title of GUI window
rpsg.title('Rock Paper Scissor')

# Size of window
rpsg.geometry('800x680')

# Creating canvas
canvas = Canvas(rpsg, width=800, height=680, bg="light yellow")
canvas.grid(row=0, column=0)

# Creating labels on GUI window
name_var=StringVar()
def submit():
    name = name_var.get()
    print(name)
    name_var.set("")
name_entry = Entry(rpsg,textvariable = name_var, font=('calibre',10,'normal'))
e1 = input("enter player1 name: ")
e2 = input("enter player2 name: ")
l1 = Label(rpsg, text=e1, font=('Algerian', 25),bg= "light yellow")
l2 = Label(rpsg, text=e2, font=('Algerian', 25), bg="light yellow")
l3 = Label(rpsg, text='Vs', font=('Algerian', 40), bg="light yellow")
sub_btn=Button(rpsg,text = 'Submit', command = submit)
# Placing all the labels on window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)
name_entry.grid(row=9,column=3)
# Default image
img_p = Image.open("default.jpg")
img_p = img_p.resize((300, 300))

# Flipping image from left to right
img_c = img_p.transpose(Image.Transpose.TRANSPOSE.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

# Rock image
rock_p = Image.open('rock.jpg')
rock_p = rock_p.resize((300, 300))

# Flipping image from left to right
rock_c = rock_p.transpose(Image.Transpose.TRANSPOSE.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

# Paper image
paper_p = Image.open('paper.jpg')
paper_p = paper_p.resize((300, 300))

# Flipping image from left to right
paper_c = paper_p.transpose(Image.Transpose.TRANSPOSE.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

# Scissor image
scissor_p = Image.open('scissors.jpg')
scissor_p = scissor_p.resize((300, 300))

# Flipping image from left to right
scissor_c = scissor_p.transpose(Image.Transpose.TRANSPOSE.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

# Selection image
img_s = Image.open("bigger+logo.jpg")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

# Putting image on canvas on specific coordinates
canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)


# game function
def game(player):
    def game1(player2):
        select = [1, 2, 3]

       # Setting image for player on canvas
        if player == 1:

        # Puts rock image on canvas
            canvas.create_image(0, 100, anchor=NW, image=rock_p)
        elif player == 2:

        # Puts paper image on canvas
            canvas.create_image(0, 100, anchor=NW, image=paper_p)
        else:

        # Puts scissor image on canvas
            canvas.create_image(0, 100, anchor=NW, image=scissor_p)

    # Setting image for computer on canvas
        if player2 == 1:

        # Puts rock image on canvas
            canvas.create_image(500, 100, anchor=NW, image=rock_c)
        elif player2 == 2:

        # Puts paper image on canvas
            canvas.create_image(500, 100, anchor=NW, image=paper_c)
        else:

        # Puts scissor image on canvas
            canvas.create_image(500, 100, anchor=NW, image=scissor_c)

    # Obtaining result by comparison
        if player == player2:  # Case of DRAW
            res = "It's a draw!"

    # Case of player's win
        elif (player == 1 and player2 == 3) or (player == 2 and player2 == 1) or (player == 3 and player2 == 2):
            res = f' Congrats!! {e1} won'

    # Case of computer's win
        else:
            res = f'Congrats!! {e2} won'

    # Putting result on canvas
        canvas.create_text(390, 600, text=res, fill="black", font=('Algerian', 25), tag='result')

    # Function for clear button

    rock_b1 = Button(rpsg, text='Rock', command=lambda: game1(1))
    rock_b1.place(x=532, y=487)

    # Button for selecting paper
    paper_b1 = Button(rpsg, text='Paper', command=lambda: game1(2))
    paper_b1.place(x=624, y=487)

    # Button for selecting scissor
    scissor_b1 = Button(rpsg, text='Scissor', command=lambda: game1(3))
    scissor_b1.place(x=716, y=487)




# Button for selecting rock
rock_b = Button(rpsg, text='Rock', command=lambda: game(1))
rock_b.place(x=35, y=487)

# Button for selecting paper
paper_b = Button(rpsg, text='Paper', command=lambda: game(2))
paper_b.place(x=128, y=487)

# Button for selecting scissor
scissor_b = Button(rpsg, text='Scissor', command=lambda: game(3))
scissor_b.place(x=220, y=487)



# Function for clear button
def clear():
    # Removes result from canvas
    canvas.delete('result')

    # Puts default image on canvas
    canvas.create_image(0, 100, anchor=NW, image=img_p)
    canvas.create_image(500, 100, anchor=NW, image=img_c)
# Button for clear
clear_b = Button(rpsg, text='Play again', font=('Times', 10, 'bold'),width=10, command=clear, bg="light green").place(x=370, y=28)

rpsg.mainloop()
