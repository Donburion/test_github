import tkinter as tk
def terminate_this(root):
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    new_button = tk.Button(master = root, text = 'new_button', command = lambda : terminate_this(root))
    new_button.pack()
    root.mainloop()
