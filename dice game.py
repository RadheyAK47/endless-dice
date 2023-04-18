import random
from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.title("endless dice game")
root.geometry("600x600")
root.configure(background="#FBB917")

img=ImageTk.PhotoImage(Image.open("dice.jpg"))
p1_score=0
p2_score=0

player1=Label(root,bg="#16FAB9",fg="#FA1657",text="player1")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,bg="#16FAB9",fg="#FA1657",text="player2")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score=Label(root,bg="#FF8C00",fg="white")
player1_score.place(relx=0.1,rely=0.5,anchor=CENTER)

player2_score=Label(root,bg="#FF8C00",fg="white")
player2_score.place(relx=0.9,rely=0.5,anchor=CENTER)

dice=Label(root,bg="#024034",fg="white")
dice.place(relx=0.5,rely=0.5,anchor=CENTER)

def player_1():
    global p1_score
    r=random.randint(1, 6)
    dice["text"]="player1 dice no. "+str(r) 
    p1_score = p1_score+r
    player1_score["text"]=str(p1_score)
    

def player_2():
    global p2_score
    ra=random.randint(1,6)
    dice["text"]="player2 dice no. "+str(ra)
    p2_score=p2_score+ra
    player2_score["text"]=str(p2_score)


    
pl1_btn=Button(root,image=img,command=player_1)
pl1_btn.place(relx=0.1,rely=0.7,anchor=CENTER)

pl2_btn=Button(root,image=img,command=player_2)
pl2_btn.place(relx=0.9,rely=0.7,anchor=CENTER)













root.mainloop()