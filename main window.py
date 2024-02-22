import tkinter as tk
tempclick = 0
def main():
    root = tk.Tk()
    root.title("untitled game")
    root.geometry("300x200")  # Set window dimensions (width x height)

    label = tk.Label(root, text="Hello, world!")
    label.pack(pady=20)  # Add some padding

    button = tk.Button(root, text="click me", command=lambda: buttonclick())
    button.pack()

    root.mainloop()
def buttonclick():
    clicks = 0
    clicks += 1
    print (clicks)




if __name__ == "__main__":
    main()
