import json
import sqlite3

import pandas as pd

from dataBase.dbUtils import dataBasePath, get_Fcl_Row_As_Object, get_Client_As_Object, get_Port_As_Object
from aifc import Error

from excelOperations.excelOperations import helperAddfilePath, Load_New_Fcl_Rates_From_Excel, Clear_Sheet, \
    Load_New_Clients_From_Excel, Load_Ports_From_Excel
from model.client import ClientLine
from model.port import PortLine
from model.rateFcl import RateFclLine


class MyDataBase:
    con = None
    cursor = None
    dataBasePath = None
    FclRatesDb = None

    def __init__(self, ):
        self.Create_Connection()

    def Create_Connection(self):
        """ create a database connection to a SQLite database """
        try:
            self.con = sqlite3.connect(dataBasePath)
            self.cursor = self.con.cursor()
            self.dataBasePath = dataBasePath
            print("MyDataBase -- Create_Connection -- Done successfully")
        except Error as e:
            print(e)

    def Close_Connection(self):
        self.con.close()

    def Create_Table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
            self.con.commit()
        except sqlite3.OperationalError as e:
            print("Error creating table", e)

    # ------------- Add to table
    def Add_Fcl_Row(self, fclRate: RateFclLine):
        sql = ''' INSERT INTO ratesFcl(portName, portCode, region, state, carrier, ratesAshdod, ratesHaifa, validFrom, validUntil)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
        f = fclRate
        fclForUpload = (
            f.portName, f.portCode, f.region, f.state, f.carrier, json.dumps(f.ratesAshDod), json.dumps(f.ratesHaifa),
            f.validStart, f.validEnd)

        self.cursor.execute(sql, fclForUpload)
        self.con.commit()

    def Add_Client_Row(self, newClient: ClientLine):
        sql = ''' INSERT INTO clients(firstName, lastName, email, phone, deltaFcl, deltaLcl, deltaAir, relevantPorts, info)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
        clientForUpload = (
            newClient.firstName, newClient.lastName, newClient.email, str(newClient.phone), str(newClient.deltaFcl),
            str(newClient.deltaLcl), str(newClient.deltaAir), newClient.relevantPorts, newClient.info)

        self.cursor.execute(sql, clientForUpload)
        self.con.commit()

    def Add_Port_Row(self, port: PortLine):
        sql = ''' INSERT INTO ports(portName, portCode, portState, PortAliases)
                  VALUES(?,?,?,?) '''
        portForUpload = (
            port.portName, port.portCode, port.portState, port.portAliases)

        self.cursor.execute(sql, portForUpload)
        self.con.commit()

    def Update_Fcl_Row_Rates_Ashdod_By_PortName_And_Carrier(self, ratesAshdod, portName, carrier):
        sql = '''UPDATE ratesFcl
                  SET ratesAshdod = ?
                  WHERE portName = ? AND carrier = ?'''

        self.cursor.execute(sql, (ratesAshdod, portName, carrier))
        self.con.commit()

    def Update_Fcl_Row_Rates_Haifa_By_PortName_And_Carrier(self, ratesHaifa, portName, carrier):
        """
        :param ratesHaifa: stringified array [dv20, dv40, hq40], i.e '[1000, 1500, 2000]'
        :param portName:
        :param carrier:
        :return:
        """
        sql = '''UPDATE ratesFcl
                  SET ratesHaifa = ?
                  WHERE portName = ? AND carrier = ?'''

        self.cursor.execute(sql, (ratesHaifa, portName, carrier))
        self.con.commit()

    def Delete_Fcl_Row_By_PortName_And_Carrier(self, portName, carrier):
        """
        :param portName:
        :param carrier:
        :return:
        """
        sql = '''DELETE FROM ratesFcl WHERE portName = ? AND carrier = ?'''
        self.cursor.execute(sql, (portName, carrier))
        self.con.commit()

    def Get_Table(self, tableName: str):
        sql = """SELECT * FROM {0}""".format(tableName)
        self.cursor.execute(sql)
        x = self.cursor.fetchall()
        self.con.commit()

    def Load_Excel_To_DB(self, action: str):
        """
        :param action: "AddFcl" , "AddClient", "AddPorts"
        """
        print(f"MyDataBase -- Load_Excel_To_DB -- action is: {action}")
        if action == "AddFclRates":
            xl = pd.read_excel(helperAddfilePath, sheet_name="FclRates")
            newRatesList = Load_New_Fcl_Rates_From_Excel(xl)
            for newRate in newRatesList:
                rate = get_Fcl_Row_As_Object(newRate)
                self.Add_Fcl_Row(rate)
            Clear_Sheet(sheetName="FclRates")
            return

        elif action == "AddClients":
            xl = pd.read_excel(helperAddfilePath, sheet_name="Clients")
            ClientsList = Load_New_Clients_From_Excel(xl)
            for newClient in ClientsList:
                client: ClientLine = get_Client_As_Object(newClient)
                self.Add_Client_Row(client)
            Clear_Sheet(sheetName="Clients")
            return

        elif action == "AddPorts":
            xl = pd.read_excel(helperAddfilePath, sheet_name="Ports")
            portsList = Load_Ports_From_Excel(xl)
            for port in portsList:
                port: PortLine = get_Port_As_Object(port)
                self.Add_Port_Row(port)
            Clear_Sheet(sheetName="Ports")
            return


