import tkinter as tk
from tkinter import *

from pandas import DataFrame, read_csv
from pandastable import Table

root = Tk()
root.iconphoto(False, PhotoImage(file="mainIcon.png"))
root.title("Client")


def fitch():
    global clients_table
    global new_df
    new_df = read_csv('clients.csv')
    clients_table = Table(table_frame, dataframe=new_df)
    clients_table.autoResizeColumns()  # resize the columns to fit the data better
    clients_table.clearFormatting()  # clear the current formatting
    clients_table.redraw()
    clients_table.show()
    save()
    return


def search():
    global new_df
    key: str = entry_search.get()
    col, search_key = key.split(':')
    if (new_df[col] == search_key).sum() > 0:
        delete_entry = tk.messagebox.askyesno(title='Item found delete it?',
                                              message=(str(new_df.loc[new_df[col] == search_key])))
        if delete_entry:
            delete_warn = tk.messagebox.askyesno(title='Delete Client',
                                                 message='Are you sure ?')
            if delete_warn:
                new_df = new_df.loc[(new_df[col] != search_key)]
                DataFrame.to_csv(new_df, "clients.csv", index=False)
                fitch()
        return
    else:
        add_new_client = tk.messagebox.askyesno(title='Item not found', message='do you want to add client ?')
        if add_new_client:
            add_client()

    return


# def add():
#     global new_df
#     global clients_table
#     temp = DataFrame(
#         {'Name': input_client.get(), 'Phone Number 1': input_exporter.get(), 'Phone Number 2': input_item.get()})
#     new_df = new_df.append(temp, ignore_index=True)
#     DataFrame.to_csv(new_df, "clients.csv", index=False)
#     fitch()
#     window_addClient.destroy()
#
#     return


def add_client():
    clients_table.addRows(1)
    # global input_client
    # global input_exporter
    # global input_item
    # global window_addClient
    # window_addClient = tk.Toplevel(root)
    # window_addClient.title("Add client")
    # label_client = Label(window_addClient, text="Client")
    # label_client.grid(row=0, column=0, padx=5)
    # input_client = StringVar()
    # entry_client = Entry(window_addClient, textvariable=input_client, width=20)
    # entry_client.grid(row=1, column=0, padx=5, pady=5)
    #
    # label_exporter = Label(window_addClient, text="Exporter")
    # label_exporter.grid(row=0, column=1, padx=5)
    # input_exporter = StringVar()
    # entry_exporter = Entry(window_addClient, textvariable=input_exporter, width=20)
    # entry_exporter.grid(row=1, column=1, padx=5, pady=5)
    #
    # label_item = Label(window_addClient, text="Item")
    # label_item.grid(row=0, column=2, padx=5)
    # input_item = StringVar()
    # entry_item = Entry(window_addClient, textvariable=input_item, width=20)
    # entry_item.grid(row=1, column=2, padx=5, pady=5)
    #
    # button_add_client = Button(window_addClient, text='Add new client', width=15, command=add)
    # button_add_client.grid(row=2, column=1, padx=5, pady=10)
    # return


def save():
    clients_table.doExport("clients.csv")
    temp_df = new_df
    temp_df.drop(temp_df.columns.difference(['client', 'exporter', 'item']), axis=1, inplace=True)
    DataFrame.to_csv(temp_df, "clients.csv", index=False)
    return


class dataFrame:
    global entry_search
    global table_frame
    table_frame = Frame(root)
    table_frame.grid(row=0, column=0, columnspan=4)
    fitch()
    searchIn = StringVar()
    entry_search = Entry(root, textvariable=searchIn, width=20)
    entry_search.grid(row=1, column=1, padx=5, pady=5)
    button_save = Button(root, text='search', width=10, command=search)
    button_save.grid(row=3, column=1, padx=5, pady=5)
    button_add_client = Button(root, text='Add client', width=15, command=add_client)
    button_add_client.grid(row=3, column=2, pady=5)

    button_save = Button(root, text='Save', width=10, command=save)
    button_save.grid(row=3, column=3, padx=5, pady=5)

    root.mainloop()
    save()
