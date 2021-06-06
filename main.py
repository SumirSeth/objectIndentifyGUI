import json
from tkinter import *

#terminal functions, to run the program in terminal
def check(obj):
    found = ""
    with open("data.json") as f:
        datasets = json.load(f)
    for dataset in datasets.keys():
        if obj in datasets[dataset]:
            found = f"Found in {dataset}"
    if found == "":
        add_data(data=obj, datasets=datasets)
    else:
        print(found)
def add_data(data, datasets):
    print("Not found in any dataset!\nAdding it into a new one....\n")
    dataset = input(f"What type of object is '{data}'? ").lower()
    if dataset == "exit":
        print("Ok Exiting!")
        return
    else:
        if dataset in datasets.keys():
            datasets[dataset].append(f"{data}")
        else:
            datasets.update({f"{dataset}":[f"{data}"]})
        with open("data.json", "w") as f:
            json.dump(datasets, f)
def start():
    while True:
        obj = input().lower().strip()
        check(obj)

#gui functions, to run the program in gui
counter = 0
def checkNew():
    global counter
    obj = str(field.get(1.0, "end-1c")).lower().strip()
    found = ""
    with open("data.json") as f:
        datasets = json.load(f)
    for dataset in datasets.keys():
        if obj in datasets[dataset]:
            found = f"\nFound in {dataset}\n"
    if found == "":
        if counter ==0:
            add_dataNew(data=obj, datasets=datasets)
            counter =1
    else:
        print(found)
        l.config(text=found,font=("Courier", "30"))
        l.pack()
def add_dataNew(data, datasets):
    global counter

    def add():
        global counter
        h = inp.get(1.0, "end-1c")
        dataset = str(h).lower().strip()
        if dataset == "exit":
            l.config(text="\nOk Exiting!\n",font=("Courier", "30"))
            l.pack()
            inp.destroy()
            confirm.destroy()
            counter = 0
            return
        else:
            if dataset in datasets.keys():
                datasets[dataset].append(f"{data}")
                counter = 0
            else:
                datasets.update({f"{dataset}":[f"{data}"]})
                counter = 0
            with open("data.json", "w") as f:
                json.dump(datasets, f)
            inp.destroy()
            confirm.destroy()

    l.config(text=f"\nNot found in any dataset!\nAdding it into a new one....\nWhat type of object is '{data}'?\n", font=("Courier", "20"))
    l.pack()
    #add a input text field
    inp = Text(root,font=("Sans","25"),foreground="blue", width="32", height="2")
    inp.pack()
    confirm = Button(root, text=f"Confirm", border=4, command=add, height=2, width=10, font=("Sans", 15), foreground="#363636", background="#9c9a9a")
    confirm.pack()
def startGUI():
    global root, field, l, get
    root = Tk()
    root.title("Sumir's Object Identifier")

    field = Text(root,font=("Sans","25"),foreground="red", width="32", height="2")
    field.pack()

    get = Button(root, font=("Bold", 12),text="Get object info!", border=4, command=checkNew, height=2, width=15, foreground="#363636", background="#9c9a9a")
    get.pack()


    l = Label(root, text="")


    root.mainloop()


startGUI()