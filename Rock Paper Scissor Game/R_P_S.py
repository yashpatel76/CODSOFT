from tkinter import *
import random
from PIL import Image, ImageTk

userscore = 0
pcscore = 0
game_played = 0

L1=None
pcchose=None

def entergame(event=None):
    maingame()

def reset_game():
    global userscore, pcscore, game_played, L1, pcchose

    userscore=0
    pcscore=0
    game_played=0

    #clearing previous results
    if L1:
        L1.grid_forget()
    if pcchose:
        pcchose.destroy()

    first_screen()

def first_screen():

    global inptitle, inpname, robotname, robottitle, submit
    global nameinp, p1, p2, orange, green, blue, ply1, ply2, images, vs

    def force_uppercase(*args):
        nameinp.set(nameinp.get().upper())

    #Clearing the ain game screen
    for widget in root.winfo_children():
        widget.destroy()

    #heading - "Rock, Paper, Scissor" #ff8a47-Orange #0077ae-blue
    head=Label(root, text='Rock✊ - Paper🖐 - Scissor✌️', font='arial 35 bold', bg='black', fg='#11917b', borderwidth=3, relief=RAISED)
    head.grid(columnspan=3, row=0, ipadx=70, ipady=10, padx=33, pady=10)

    def resize_image(file_path, size=(100,150)):
        img=Image.open(file_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    #Images of Player 1,2,vs
    ply1=resize_image('Player-1.png', size=(100,150))
    ply2=resize_image('Player-2.png', size=(100,150))
    images={'vs':PhotoImage(file='vs.png')}

    #Image of Rock, Paper, Scissor as Orange, Blue, and light green
    orange={'rock':PhotoImage(file='rockO.png'),'paper':PhotoImage(file='paperO.png'),'scissor':PhotoImage(file='scissorO.png')}
    blue={'rock':PhotoImage(file='rockB.png'),'paper':PhotoImage(file='paperB.png'),'scissor':PhotoImage(file='scissorB.png')}
    green={'rock':PhotoImage(file='rockG.png'),'paper':PhotoImage(file='paperG.png'),'scissor':PhotoImage(file='scissorG.png')}

    #FRAME-1
    f1=Frame(root, bg='black')
    f1.grid(row=2, column=0, columnspan=3, pady=5)

    #Img Player1
    p1 = Label(f1, image=ply1, bg='black')
    p1.grid(row=2, column=0, padx=30)

    #Img vs
    vs = Label(f1, image=images['vs'], bg='black')
    vs.grid(row=2, column=1, padx=30)

    #Img Player2
    p2 = Label(f1, image=ply2, bg='black')
    p2.grid(row=2, column=2, padx=50)

    #Player 1 field
    inptitle=Label(root,text='Player 1:',font='arial 15 bold', fg='#ff8a47', bg='black')
    inptitle.grid(row=3,column=0, padx=20)
    nameinp=StringVar()
    nameinp.trace_add("write", force_uppercase)
    inpname=Entry(root, textvar=nameinp, font='arial 10 bold', fg='#ff8a47',borderwidth=3, relief=RAISED)
    inpname.bind('<Return>', entergame)
    inpname.grid(row=4,column=0, padx=20)

    #Player 2 field
    robottitle=Label(root,text='Player 2:',font='arial 15 bold', fg='#0077ae', bg='black')
    robottitle.grid(row=3,column=2, padx=10)
    robotname=Label(root,text='Robot',font='arial 15 bold', fg='#0077ae', bg='black')
    robotname.grid(row=4,column=2, padx=10)

    #start button
    submit=Button(root, text="Hurrahh..! Start", font='arial 15 bold',bg='black', fg='#11917b', command=maingame, borderwidth=3, relief=RAISED)
    submit.grid(row=5, column=0, columnspan=3, pady=10, padx=30)

#Maingame function
def maingame():
    global userscore, pcscore, pcchose, L1, game_played, userlbl, pclbl
    global nameinp, rock, paper, scissor, p1, p2, total_game


    inptitle.destroy()
    inpname.destroy()
    robottitle.destroy()
    robotname.destroy()
    submit.destroy()
    
    def update_status():
        total_game.config(text=f'Game Played: {game_played}')

    #Game Played how many Times
    total_game=Label(root, text='Games Played: 0',font='arial 16 bold', fg='#32c3aa', bg='#727272', borderwidth=3, relief=RAISED)
    total_game.grid(row=1, column=1, pady=8, ipadx=5)

    #Display User Score
    L2=Label(root,text='', bg='#727272', fg='#ff8a47', borderwidth=3, relief=RAISED, font='arial 16 bold', padx=4, pady=2)
    L2.grid(row=1, column=0, pady=8, ipadx=5)
    if nameinp.get():
        L2.config(text=f'{nameinp.get()}\'s Score:{userscore}')
    else:
        L2.config(text=f'Your Score:{userscore}')
    
    #Display Pc Score
    L3=Label(root, text=f'Robot\'s Score:{pcscore}', bg='#727272', fg='#1c14a1', borderwidth=3, relief=RAISED, font='arial 16 bold', padx=4, pady=2)
    L3.grid(row=1, column=2, pady=8, ipadx=5)

    def click(event):
        global userscore, pcscore, pcchose, L1, green, blue, orange, userlbl, pclbl, game_played

        #user's choice
        val=event.widget.cget('text')
        p1.configure(image=orange[val.lower()])
        
        #User opt for Rock/Paper/Scissor
        if nameinp.get():
            userlbl.config(text=f'{nameinp.get()} Choose: {val}')
        else:
            userlbl.config(text=f'You Choose: {val}')

        #Robot's Choice
        pc_opt=random.choice(['Rock', 'Paper', 'Scissor'])
        p2.configure(image=blue[pc_opt.lower()])
        #Displaying Robot's Choice
        pclbl.config(text=f'Robot Choose: {pc_opt}')

        #Result Field
        L1 = Label(root, text='', font='arial 20 bold', bg='#727272', fg='#32c3aa', height=1, width=15, borderwidth=3, relief=RAISED)
        L1.grid(row=4, column=1, columnspan=2, rowspan=2)

        #Logic of Game
        if val == 'Rock' and pc_opt == 'Paper':
            L1.config(text='PC Won...!')
            pcscore += 1
        elif val == 'Rock' and pc_opt == 'Scissor':
            if nameinp.get():
                L1.config(text=f'{nameinp.get()} Win...!')
            else:
                L1.config(text='You Win...!')
            userscore += 1
        elif val == 'Paper' and pc_opt == 'Rock':
            if nameinp.get():
                L1.config(text=f'{nameinp.get()} Win...!')
            else:
                L1.config(text='You Win...!')
            userscore += 1
        elif val == 'Paper' and pc_opt == 'Scissor':
            L1.config(text='PC Won...!')
            pcscore += 1
        elif val == 'Scissor' and pc_opt == 'Rock':
            L1.config(text='PC Won...!')
            pcscore += 1
        elif val == 'Scissor' and pc_opt == 'Paper':
            if nameinp.get():
                L1.config(text=f'{nameinp.get()} Win...!')
            else:
                L1.config(text='You Win...!')
            userscore += 1
        elif val == pc_opt:
            L1.config(text='Match is Tie..!')
            p1.configure(image=green[val.lower()])
            p2.configure(image=green[pc_opt.lower()])

        #Increment of game
        game_played += 1

        #updateing scores
        
        if nameinp.get():
            L2.config(text=f'{nameinp.get()}\'s Score: {userscore}')
        else:
            L2.config(text=f'Your Score:{userscore}')
        
        L3.config(text=f'Robot\'s Score: {pcscore}')

        #Updating Status
        update_status()
        
    #Rock-Button
    rock=Button(root, text='Rock', font='arial 14 bold', fg='#ff8a47', borderwidth=3, relief=RAISED, bg='black', height=1, width=6)
    rock.grid(row=4, column=0, pady=8, ipadx=5)
    rock.bind('<Button-1>', click)
    #Paper-Button
    paper=Button(root, text='Paper', font='arial 14 bold', fg='#ff8a47', borderwidth=3, relief=RAISED, bg='black', height=1, width=6)
    paper.grid(row=5, column=0, pady=8, ipadx=5)
    paper.bind('<Button-1>', click)
    #Scissor-Button
    scissor=Button(root, text='Scissor', font='arial 14 bold', fg='#ff8a47', borderwidth=3, relief=RAISED, bg='black', height=1, width=6)
    scissor.grid(row=6, column=0, pady=8, ipadx=5)
    scissor.bind('<Button-1>', click)

    #User choose
    userlbl=Label(root,text='', font='arial 16 bold', fg='#ff8a47', bg='#727272', borderwidth=3, relief=RAISED)
    userlbl.grid(row=3, column=0, pady=8, ipadx=20, ipady=5)
    if nameinp.get():
        userlbl.config(text=f'{nameinp.get()}')
    else:
        userlbl.config(text=f'You')

    #Robot choose
    pclbl=Label(root,text='Robot', font='arial 16 bold', fg='#1c14a1', bg='#727272', borderwidth=3, relief=RAISED)
    pclbl.grid(row=3, column=2, pady=8, ipadx=20, ipady=5)

    #Exit Button
    Exit=Button(root, text='EXIT', font='arial 14 bold', command=root.quit, fg='#11917b', bg='black', borderwidth=3, relief=RAISED, height=1, width=6)
    Exit.grid(row=6, column=1, pady=8, ipadx=5)

    #Play again 
    ply_gain=Button(root, text='Play Again', font='arial 14 bold', command=reset_game, fg='#11917b', borderwidth=3, relief=RAISED, bg='black', height=1, width=8)
    ply_gain.grid(row=6, column=2, pady=8, ipadx=5)

''' GUI Program Starting '''
root=Tk()
root.title("Rock Paper Scissor Game")
root.configure(bg='Black')
root.resizable(False, False)

first_screen()

root.mainloop()