import tkinter                           
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
   
def add_task():  
    task_string = task_field.get()   
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()  
        task_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():  
    clear_list()  
    for task in tasks:   
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():
    try:  
   
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:   
            tasks.remove(the_value)    
            list_update()    
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to clear the list  
def clear_list():   
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():   
    print(tasks)   
    guiWindow.destroy()  
  

# main function  
if __name__ == "__main__":  
    guiWindow = Tk()  
    guiWindow.title("To-Do List ")   
    guiWindow.geometry("665x400+550+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  
  
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
  
    tasks = []      
    functions_frame = Frame(guiWindow, bg = "black")  
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    task_label = Label( functions_frame,text = "Enter the Task:",  
        font = ("arial", "14", "bold"),  
        background = "black", 
        foreground="white"
    )  
    task_label.place(x = 20, y = 30)  
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 180, y = 30)  
  

    add_button =Button(  
        functions_frame,  
        text = "Add Task",  
        width = 15,
        bg='#D4AC0D',font=("arial", "14", "bold"),
        command = add_task,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command = delete_task,  
    )  
   
    exit_button = Button(  
        functions_frame,  
        text = "Exit",  
        width = 52,
        bg='#D4AC0D',  font=("arial", "14", "bold"),
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)   
    exit_button.place(x = 17, y = 330)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = Listbox(  
        functions_frame,  
        width = 57,  
        height = 7,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#D4AC0D",  
        selectforeground="BLACK"
    )   
    task_listbox.place(x = 17, y = 140)  
  
    list_update()  
     
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()