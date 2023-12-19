from tkinter import *
from tkinter import messagebox #paziņojumi
mansLogs=Tk()#loga objekts
mansLogs.title("TicTacToe")
global winner, speletajsX, count
count=0
speletajsX=True
winner=False

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title("Info par programmu")
    jaunsLogs.geometry("1100x565")
    apraksts=Label(jaunsLogs,text="Spele piedalas 2 speletaji: viens spele ar X simbolu un otrs ar 0 simbolu.", font="Helvica 16", bg="#97BFB4")
    apraksts.grid(row=0,column=0)
    apraksts=Label(jaunsLogs,text="Gajienus veic pamišus, sakot ar X speletaju. Gajienu drikst veikt tikai tukšajos laucinos.", font="Helvica 16", bg="#97BFB4")
    apraksts.grid(row=1,column=0)
    apraksts=Label(jaunsLogs,text="Sakotneji laukumu veido 9 tukši laucini, izkartoti 3x3 formata.", font="Helvica 16", bg="#97BFB4")
    apraksts.grid(row=2,column=0)
    apraksts=Label(jaunsLogs,text="Speles merkis ir novietot 3 savus simbolus kolonna, rinda vai pa diognali.", font="Helvica 16", bg="#97BFB4")
    apraksts.grid(row=3,column=0)
    apraksts=Label(jaunsLogs,text="Ja laukums ir aizpildits un neviens no speletajiem nav sasniedzis speles merki, spele beidzas ar neizškirtu rezultatu.", font="Helvica 16", bg="#97BFB4")
    apraksts.grid(row=4,column=0)
    return 

def restart():
    global winner, count, speletajsX
    winner=False
    count=0
    speletajsX=True
    btn1.config(state = NORMAL)
    btn2.config(state = NORMAL)
    btn3.config(state = NORMAL)
    btn4.config(state = NORMAL)
    btn5.config(state = NORMAL)
    btn6.config(state = NORMAL)
    btn7.config(state = NORMAL)
    btn8.config(state = NORMAL)
    btn9.config(state = NORMAL)
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "
    return 

def btnClick(button):
    global speletajsX, count
    if button["text"] == " " and speletajsX == True:
        button["text"] = "X"
        speletajsX = False
        count += 1
        checkWinner()
    elif button["text"] == " " and speletajsX == False:
        button["text"] = "O"
        speletajsX = True
        count += 1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe", "Šeit kāds ir ieklikšķinājis")
    return 

def checkWinner():
    global winner
    winner = False
    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X" or btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X" or btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X" or btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X" or btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X" or btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X" or btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X" or btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"):
        winner = True
        messagebox.showinfo("TicTacToe", "SpeletajsX ir uzvarējis!")
        disableButtons()
    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O" or btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O" or btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O" or btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O"):
        winner = True
        messagebox.showinfo("TicTacToe", "SpeletajsO ir uzvarējis!")
        disableButtons()
    elif count == 9 and winner == False:
        messagebox.showinfo("TicTacToe", "Neizšķirts")
        disableButtons()
    return

btn1=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4") #definē pogas
btn2=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn3=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn4=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn5=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn6=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn7=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn8=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")
btn9=Button(mansLogs, text="", width=6, height=3, font=("Helvica,24"), command=lambda:btnClick(btn1), bd=10, bg="#97BFB4")

galvenaIzvelne=Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)
opcijas=Menu(galvenaIzvelne, tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)
galvenaIzvelne.add_command(label="Par programmu", command=infoLogs) 

opcijas.add_command(label="Jauna spēle", command=restart)
opcijas.add_command(label="Iziet", command=mansLogs.quit)

btn1.grid(row=0, column=0) #pievieno pogas
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)














mansLogs.mainloop()