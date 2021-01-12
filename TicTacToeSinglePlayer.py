# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tkinter import *
from tkinter import messagebox

clicked = True
count = 0
def b_click(B):
	global clicked,count
	if B["text"] == " " and clicked == True:
		txt = "X"
		B["text"] = txt
		check_win(b)
		clicked = False
		count += 1
	elif B["text"] == " " and clicked == False:
		txt = "O"
		B["text"] = txt
		check_win(b)
		clicked = True
		count += 1
	else:
		messagebox.showerror("Tic Tac Toe","Invalid Move: Chose Another Box")

def disable_all(b):
		for i in range(0,3):
			for j in range(0,3):
				b[i][j].config(state = DISABLED)

def check_win(b):
	global winner
	winner = False

	#Check all rows
	i = 0
	for i in range(0,3):
		if (b[i][0]["text"] == "X" and b[i][1]["text"] == "X" and b[i][2]["text"] == "X"):
			b[i][0].config(bg = "green")
			b[i][1].config(bg = "green")
			b[i][2].config(bg = "green")
			disable_all(b)
			winner = True
			messagebox.showinfo("Tic Tac Toe","X WINS !")
		if (b[i][0]["text"] == "O" and b[i][1]["text"] == "O" and b[i][2]["text"] == "O"):
			b[i][0].config(bg = "green")
			b[i][1].config(bg = "green")
			b[i][2].config(bg = "green")
			disable_all(b)
			winner = True
			messagebox.showinfo("Tic Tac Toe","O WINS !")

	#Check all columns
	i = 0
	for i in range(0,3):
		if (b[0][i]["text"] == "X" and b[1][i]["text"] == "X" and b[2][i]["text"] == "X"):
			b[0][i].config(bg = "green")
			b[1][i].config(bg = "green")
			b[2][i].config(bg = "green")
			disable_all(b)
			winner = True
			messagebox.showinfo("Tic Tac Toe","X WINS !")
		if (b[0][i]["text"] == "O" and b[2][i]["text"] == "O" and b[2][i]["text"] == "O"):
			b[0][i].config(bg = "green")
			b[1][i].config(bg = "green")
			b[2][i].config(bg = "green")
			disable_all(b)
			winner = True
			messagebox.showinfo("Tic Tac Toe","O WINS !")

	#For Diagonal Cases
	if(b[0][0]["text"] == "X" and b[1][1]["text"] == "X" and b[2][2]["text"] == "X"):
		b[2][2].config(bg = "green")
		b[0][0].config(bg = "green")
		b[1][1].config(bg = "green")
		disable_all(b)
		winner = True
		messagebox.showinfo("Tic Tac Toe","X WINS !")

	if(b[0][0]["text"] == "O" and b[1][1]["text"] == "O" and b[2][2]["text"] == "O"):
		b[2][2].config(bg = "green")
		b[0][0].config(bg = "green")
		b[1][1].config(bg = "green")
		disable_all(b)
		winner = True
		messagebox.showinfo("Tic Tac Toe","O WINS !")

	if(b[2][0]["text"] == "O" and b[1][1]["text"] == "O" and b[0][2]["text"] == "O"):
		b[2][0].config(bg = "green")
		b[0][2].config(bg = "green")
		b[1][1].config(bg = "green")
		disable_all(b)
		winner = True
		messagebox.showinfo("Tic Tac Toe","O WINS !")

	if(b[2][0]["text"] == "X" and b[1][1]["text"] == "X" and b[0][2]["text"] == "X"):
		b[2][0].config(bg = "green")
		b[0][2].config(bg = "green")
		b[1][1].config(bg = "green")
		disable_all(b)
		winner = True
		messagebox.showinfo("Tic Tac Toe","X WINS !")

	if (count == 8 and winner == False):
		disable_all(b)
		messagebox.showinfo("Tic Tac Toe","The Game is a Tie!")


root = Tk()
root.title('Tic Tac Toe Game')
txt = " "
#Position Buttons
b1 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b1) )
b2 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b2) )
b3 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b3) )
b4 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b4) )
b5 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b5) )
b6 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b6) )
b7 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b7) )
b8 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b8) )
b9 = Button(root, text = txt, font = ("Helvetica",18), height = 3, width = 6, bg = "white", command = lambda:b_click(b9) )


#Grig Butttons
row = 0
col = 0
i = 0

b1.grid(row = 0,column = 0)
b2.grid(row = 0,column = 1)
b3.grid(row = 0,column = 2)
b4.grid(row = 1,column = 0)
b5.grid(row = 1,column = 1)
b6.grid(row = 1,column = 2)
b7.grid(row = 2,column = 0)
b8.grid(row = 2,column = 1)
b9.grid(row = 2,column = 2)

b = [[b1,b2,b3],[b4,b5,b6],[b7,b8,b9]]

root.mainloop()