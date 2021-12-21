import tkinter as tk

from dataBase.myDataBase import MyDataBase
from dataBase.sqlStatements import sql_create_rateFcl_table, sql_create_Client_table, sql_create_ports_table
from myGui.FclQuoteWindow import Fcl_Quote


def Get_Client_Details():
    pass


def Get_Rate_Details():
    pass


class MyApp:
    root = None
    canvas = None
    addFclSection = None
    myDataBase = None

    def __init__(self):
        self.myDataBase = MyDataBase()
        self.root = tk.Tk()

        self.Init_App()

    def Init_App(self):
        # -------------- Initializing DB
        self.myDataBase.Create_Table(sql_create_rateFcl_table)
        self.myDataBase.Create_Table(sql_create_Client_table)
        self.myDataBase.Create_Table(sql_create_ports_table)

        # -------------- Initializing GUI
        self.root.geometry("400x400")
        self.root.title("Main")

        tk.Button(self.root, text='Upload Fcl rates',
                  command=lambda: self.myDataBase.Load_Excel_To_DB(action="AddFclRates")).pack(pady=10)
        tk.Button(self.root, text='Upload Clients',
                  command=lambda: self.myDataBase.Load_Excel_To_DB(action="AddClients")).pack(pady=10)
        tk.Button(self.root, text='Generate & Send Fcl quote', command=lambda: Fcl_Quote(dataBase=self.myDataBase)).pack(pady=10)
        tk.Button(self.root, text='Update Ports DB',  command=lambda: self.myDataBase.Load_Excel_To_DB(action="AddPorts")).pack(pady=10)

        print("MyApp -- Init_App -- Done Initializing App")

    def Main_Loop(self):
        print("MyApp -- Main_Loop -- Entered Main_Loop function")
        self.root.mainloop()
