import random
from tkinter import *
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
code = random.sample(num, 4)
guess = 10
f = 0


def tkinter_version():
    root = Tk()
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def Button_Click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def Button_Clear():
        e.delete(0, END)

    def Button_Equal():
        global user_guess
        user_guess = int(e.get())
        e.delete(0, END)
        root.destroy()

    Button_1 = Button(root, text="1", padx=40, pady=20,
                      command=lambda: Button_Click(1))
    Button_2 = Button(root, text="2", padx=40, pady=20,
                      command=lambda: Button_Click(2))
    Button_3 = Button(root, text="3", padx=40, pady=20,
                      command=lambda: Button_Click(3))
    Button_4 = Button(root, text="4", padx=40, pady=20,
                      command=lambda: Button_Click(4))
    Button_5 = Button(root, text="5", padx=40, pady=20,
                      command=lambda: Button_Click(5))
    Button_6 = Button(root, text="6", padx=40, pady=20,
                      command=lambda: Button_Click(6))
    Button_7 = Button(root, text="7", padx=40, pady=20,
                      command=lambda: Button_Click(7))
    Button_8 = Button(root, text="8", padx=40, pady=20,
                      command=lambda: Button_Click(8))
    Button_9 = Button(root, text="9", padx=40, pady=20,
                      command=lambda: Button_Click(9))
    Button_0 = Button(root, text="0", padx=40, pady=20,
                      command=lambda: Button_Click(0))
    # Button_add=Button(root,text="+",padx=40,pady=20,command=Button_Click)
    Button_equal = Button(root, text="=", padx=40,
                          pady=20, command=Button_Equal)
    Button_clear = Button(root, text="C", padx=40,
                          pady=20, command=Button_Clear)

    # put buttons on the screen

    Button_1.grid(row=3, column=0)
    Button_2.grid(row=3, column=1)
    Button_3.grid(row=3, column=2)

    Button_4.grid(row=2, column=0)
    Button_5.grid(row=2, column=1)
    Button_6.grid(row=2, column=2)

    Button_7.grid(row=1, column=0)
    Button_8.grid(row=1, column=1)
    Button_9.grid(row=1, column=2)

    Button_0.grid(row=4, column=1)

    # Button_add.grid(row=5,column=0)
    Button_equal.grid(row=4, column=2)
    Button_clear.grid(row=4, column=0)

    root.mainloop()


def main_code():
    global guess
    global f
    while(guess != 0):
        if(f == 4):
            points = (10*(guess+1))
            if (10-guess == 1):
                print(
                    "You've successfully cracked the code in 1 guess and have recieved 100 points!")
                break
            else:
                print("You've successfully cracked the code in", 10 -
                      guess, "guesses and have recieved", points, "points!")
                break

        f = 0
        if(f != 4):
            tkinter_version()
            user_code = [int(digit) for digit in str(user_guess)]

            for i in range(0, 4):
                if user_code[i] in code:
                    if user_code[i] == code[i]:
                        print(user_code[i], "is correctly placed")
                        f += 1
                    else:
                        print(
                            user_code[i], "is present in the code,but incorrectly placed")
                else:
                    print(user_code[i], "is not in the required code")
        guess -= 1
        print("guesses left:", guess)

    while(guess == 0):
        if(f == 4):
            points = (10*(guess+1))
            if (10-guess == 1):
                print(
                    "You've successfully cracked the code in 1)guess and have recieved 100 points!")
                break
            else:
                print("You've successfully cracked the code in", 10 -
                      guess, "guesses and have recieved", points, "points!")
                break
        else:
            print("you've failed to guess the code, the required code was",
                  code[0], code[1], code[2], code[3])
            break


main_code()
