import tkinter as tk

def go_to_first():
    f1.pack()
    f2.pack_forget()

def go_to_second():
    f1.pack_forget()
    f2.pack()

master = tk.Tk()

# first frame - without f1.pack()
f1 = tk.Frame(master)
l1 = tk.Label(f1, text="First Frame")
l1.pack()
b1 = tk.Button(f1, text="Go to Second", command=go_to_second)
b1.pack()

# second frame - without f2.pack()
f2 = tk.Frame(master)
l2 = tk.Label(f2, text="Second Frame")
l2.pack()
b2 = tk.Button(f2, text="Go to First", command=go_to_first)
b2.pack()

# show first frame
f1.pack()

master.mainloop()