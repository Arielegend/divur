import tkinter
import tkinter as tk

from dataBase.myDataBase import MyDataBase

clients_dummy = [
    {"firstName": "yeled", "lastName": "zevel"},
    {"firstName": "yaldat", "lastName": "zevel"},
    {"firstName": "yaldat1", "lastName": "zevel"},
    {"firstName": "yaldat2", "lastName": "zevel"},
    {"firstName": "yaldat3", "lastName": "zevel"},
    {"firstName": "yaldat4", "lastName": "zevel"},
    {"firstName": "yaldat5", "lastName": "zevel"},
    {"firstName": "yaldat6", "lastName": "zevel"},
    {"firstName": "yaldat7", "lastName": "zevel"},
    {"firstName": "yaldat8", "lastName": "zevel"},
    {"firstName": "yaldat9", "lastName": "zevel"},
    {"firstName": "yaldat10", "lastName": "zevel"},
    {"firstName": "yaldat11", "lastName": "zevel"},
    {"firstName": "yaldat12", "lastName": "zevel"},
    {"firstName": "yaldat13", "lastName": "zevel"},
    {"firstName": "yaldat14", "lastName": "zevel"},
    {"firstName": "yaldat15", "lastName": "zevel"},
    {"firstName": "yaldat16", "lastName": "zevel"},
    {"firstName": "yaldat17", "lastName": "zevel"},
    {"firstName": "yaldat18", "lastName": "zevel"},
    {"firstName": "yaldat19", "lastName": "zevel"},
    {"firstName": "yaldat20", "lastName": "zevel"}
]


class FclQuoteWindow:
    def __init__(self, dataBase: MyDataBase):
        self.top = tk.Toplevel()
        top = self.top

        self.clientLabel = tk.Label(top, text="Client")
        self.clientEntry = tk.Entry(top)
        self.clientBrowse = tk.Button(top, text="Clients...", command=lambda: self.Choose_Clients())
        self.allClientsListbox = None

        self.dv20Label = tk.Label(top, text="dv20")
        self.dv20Entry = tk.Entry(top)
        self.dv40Label = tk.Label(top, text="dv40")
        self.dv40Entry = tk.Entry(top)
        self.hq40Label = tk.Label(top, text="hq40")
        self.hq40Entry = tk.Entry(top)

        self.myDataBase = dataBase
        self.Initialize()

    def Initialize(self):
        # ----------- Client -----------
        self.clientLabel.grid(row=0, column=0, padx=10, pady=10)
        self.clientEntry.grid(row=0, column=1, padx=10, pady=10)
        self.clientBrowse.grid(row=0, column=2, padx=10, pady=10)

        # ----------- Containers -----------
        self.dv20Label.grid(row=1, column=0, padx=10, pady=10)
        self.dv20Entry.grid(row=1, column=1, padx=10, pady=10)
        self.dv40Label.grid(row=2, column=0, padx=10, pady=10)
        self.dv40Entry.grid(row=2, column=1, padx=10, pady=10)
        self.hq40Label.grid(row=3, column=0, padx=10, pady=10)
        self.hq40Entry.grid(row=3, column=1, padx=10, pady=10)

    def Choose_Clients(self):
        window_browse_clients = tk.Toplevel()
        window_browse_clients.geometry("300x300")
        self.allClientsListbox = tk.Listbox(window_browse_clients, height=100)

        for client in clients_dummy:
            helper = str(client['firstName'] + " " + client['lastName'])
            self.allClientsListbox.insert(tk.END, helper)
        self.allClientsListbox.pack(pady=50)
        self.allClientsListbox.bind("<<ListboxSelect>>", self.Listbox_Listener)

    def Listbox_Listener(self, event):
        newValue = self.allClientsListbox.get(tk.ACTIVE)
        if self.clientEntry != newValue:
            self.clientEntry.delete(0, tk.END)
            self.clientEntry.insert(0, newValue)


def Fcl_Quote(dataBase):
    FclQuoteWindow(dataBase=dataBase)
