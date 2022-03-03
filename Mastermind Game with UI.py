import tkinter as tk
import random
import collections

class Mastermind:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent)
        self.status = tk.Label(parent)
        self.draw_board()
    def draw_board(self, event=None):
        self.example=['r','o','y','g','b','p']

        self.canvas.destroy()
        self.status.destroy()
        self.canvas = tk.Canvas(self.parent,bg='thistle',width=1050, height=400)
        self.canvas.pack()
        self.bag = {'r':self.canvas.create_oval(960, 0, 1027, 66, fill='red', outline='black'),
                    'o':self.canvas.create_oval(960, 66, 1027, 131, fill='orange', outline='black'),
                    'y':self.canvas.create_oval(960, 131, 1027, 200, fill='yellow', outline='black'),
                    'g':self.canvas.create_oval(960, 200, 1027, 267, fill='green', outline='black'),
                    'b':self.canvas.create_oval(960, 267, 1027, 334, fill='blue', outline='black'),
                    'p':self.canvas.create_oval(960, 334, 1027, 400, fill='purple', outline='black')
                   }
        self.ids = {a:b for b,a in self.bag.items()}
        self.colors = {'r':'red', 'o':'orange', 'y':'yellow',
                       'g':'green', 'b':'blue', 'p':'purple'}
        self.guesses = ['']
        self.status = tk.Label(self.parent)
        self.status.pack()
        self.canvas.bind('<1>', self.check)
        self.parent.bind('<Control-n>', self.draw_board)
        self.parent.bind('<Control-N>', self.draw_board)
        self.pattern=random.sample(self.example,4)
        
        self.counted = collections.Counter(self.pattern)
    def check(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        guess = self.ids[id]
        self.guesses[-1] += guess
        y_offset = (len(self.guesses[-1]) - 1) * 80
        x_offset = (len(self.guesses) - 1) * 80
        self.canvas.create_oval(x_offset, y_offset,
                                x_offset+80, y_offset+80,
                                fill=self.colors[guess],
                                outline='black')
        if len(self.guesses[-1]) < 4:
            return
        guess_count = collections.Counter(self.guesses[-1])
        close = sum(min(self.counted[k], guess_count[k]) for k in self.counted)
        exact = sum(a==b for a,b in zip(self.pattern, self.guesses[-1]))
        close -= exact
        colors = exact*['black'] + close*['white']
        key_coordinates = [(x_offset, 320, x_offset+40, 360),
                           (x_offset, 360, x_offset+40, 400),
                           (x_offset+40, 320, x_offset+80, 360),
                           (x_offset+40, 360, x_offset+80, 400)]
        for color, coord in zip(colors, key_coordinates):
            self.canvas.create_oval(coord, fill=color, outline='black')
        if exact == 4:
            self.status.config(text='YOU ARE A WINNER!')
            self.canvas.unbind('<1>')
        elif len(self.guesses) > 11:
            self.status.config(
                               text='Oops,out of guesses. The required code is {}.'.format(
                                ''.join(self.pattern)))
            self.canvas.unbind('<1>')
        else:
            self.guesses.append('')
        
        
root = tk.Tk()
root.title('Mastermind')
game = Mastermind(root)
root.mainloop()



