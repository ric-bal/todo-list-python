import customtkinter as ctk

#functions
#global checkbox

def add_todo():
    todo = entry.get()
    if todo == "":
        return
    
    new_frame = ctk.CTkFrame(scrollable_frame, width=400, height=50)
    new_frame.pack()

    checkbox = ctk.CTkCheckBox(new_frame, text=todo, width=350) # width=350,
    checkbox.pack(side = ctk.RIGHT, anchor = ctk.W)

    star_checkbox = ctk.CTkCheckBox(new_frame, text="", 
                                    border_color="orange", 
                                    border_width=0.6, 
                                    hover=False,
                                    checkmark_color="orange", 
                                    fg_color="orange", 
                                    checkbox_height=15,
                                    checkbox_width=15) # width=350,
    
    star_checkbox.pack(side = ctk.LEFT, anchor = ctk.E)

    entry.delete(0, ctk.END)


def remove_todo():
    to_delete = []

    for child in scrollable_frame.children.values():
        if isinstance(child, ctk.CTkFrame):
            for grandchild in child.children.values():
                if isinstance(grandchild, ctk.CTkCheckBox):
                    if grandchild._check_state == True and grandchild._text != "":
                        to_delete.append(child)

    for i in range(0, len(to_delete)):
        to_delete[i].destroy()


def clear_todo():
    to_delete = []

    for child in scrollable_frame.children.values():
        if isinstance(child, ctk.CTkFrame):
            to_delete.append(child)

    for i in range(0, len(to_delete)):
        to_delete[i].destroy()


def save_todo():
    file = open("listItems_2.txt", "w")

    for child in scrollable_frame.children.values():
        if isinstance(child, ctk.CTkFrame):

            for grandchild in child.children.values():
                if isinstance(grandchild, ctk.CTkCheckBox):
                    starState = None
                    if grandchild._text == "":
                        if grandchild._check_state == True:
                            starState = "True"
                        elif grandchild._check_state == False:
                            starState = "False"
                    else:
                        checkboxName = grandchild._text
                        if grandchild._check_state == True:
                            checkboxState = "True"
                        elif grandchild._check_state == False:
                            checkboxState = "False"
                    
                    if starState != None:
                        file.write(starState + "\n")
                    else:
                        file.write(checkboxName + "\n" + checkboxState + "\n")
    file.close()


def load_todo():
    file = open("listItems_2.txt", "r")

    recordNumber = 1
    while True:
        record = file.readline()
        if record == "":
            file.close()
            break

        record = record.strip()
        
        if recordNumber == 1:
            new_frame = ctk.CTkFrame(scrollable_frame, width=400, height=50)
            new_frame.pack()

            checkbox = ctk.CTkCheckBox(new_frame, text=record, width=350) # width=350,
            checkbox.pack(side = ctk.RIGHT, anchor = ctk.W)

        elif recordNumber == 2:
            if record == "True":
                checkbox.select()

        elif recordNumber == 3:
            print("esrjkhwd")
            star_checkbox = ctk.CTkCheckBox(new_frame, text="", 
                                            border_color="orange", 
                                            border_width=0.6, 
                                            hover=False,
                                            checkmark_color="orange", 
                                            fg_color="orange", 
                                            checkbox_height=15,
                                            checkbox_width=15) # width=350
            star_checkbox.pack(side = ctk.LEFT, anchor = ctk.E)

            if record == "True":
                star_checkbox.select()

            recordNumber = 0


        recordNumber += 1

    file.close()



# loading data, defining widgets

root = ctk.CTk() 
root.geometry("500x500")
root.title("Todo App")

title_label = ctk.CTkLabel(root, text="Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(20, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=400, height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add Task")
entry.pack(fill="x")

add_button = ctk.CTkButton(root, text="Add", width=400, command=add_todo)
add_button.pack(pady=(20, 0))

remove_button = ctk.CTkButton(root, text="Remove completed", width=400, command=remove_todo)
remove_button.pack(pady=(10, 0))

clear_button = ctk.CTkButton(root, text="Remove all", width=400, command=clear_todo)
clear_button.pack(pady=(10, 0))

save_button = ctk.CTkButton(root, text="Save", width=400, command=save_todo)
save_button.pack(pady=(30, 0))

load_todo()

root.mainloop()
