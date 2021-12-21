from model.client import ClientLine
from model.port import PortLine
from model.rateFcl import RateFclLine

dataBasePath = "dataBase.db"
tableName_RatesFcl = "ratesFcl"
tableName_Clients = "clients"


def get_Fcl_Row_As_Object(newFclRateXlRow) -> RateFclLine:
    """
    :param newFclRateXlRow: (portName, portCode, region, state, carrier, dv20_Ashdod, dv40_Ashdod, hq40_Ashdod, dv20_Haifa, dv40_Haifa, hq40_Haifa, validStart, validEnd)
                             Based on the rows from HelperAdd XL file. at upload new FCL rate sheet.
    :return: new Object of type RateFclLine
    """
    helperNewRateFclDict = {
        'portName': newFclRateXlRow[0],
        'portCode': newFclRateXlRow[1],
        'region': newFclRateXlRow[2],
        'state': newFclRateXlRow[3],
        'carrier': newFclRateXlRow[4],

        'dv20_Ashdod': newFclRateXlRow[5],
        'dv40_Ashdod': newFclRateXlRow[6],
        'hq40_Ashdod': newFclRateXlRow[7],

        'dv20_Haifa': newFclRateXlRow[8],
        'dv40_Haifa': newFclRateXlRow[9],
        'hq40_Haifa': newFclRateXlRow[10],

        'validStart': newFclRateXlRow[11],
        'validEnd': newFclRateXlRow[12]
    }
    return RateFclLine(helperNewRateFclDict)


def get_Client_As_Object(newClientXlRow) -> ClientLine:
    """
    :param newClientXlRow: (firstName, lastName, email, phone, deltaFcl, deltaLcl, deltaAir, relevantPorts, info)
                             Based on the rows from HelperAdd XL file. at upload new FCL rate sheet.
    :return: new Object of type ClientLine
    """
    helperNewClientDict = {
        'firstName': newClientXlRow[0],
        'lastName': newClientXlRow[1],
        'email': newClientXlRow[2],
        'phone': newClientXlRow[3],

        'deltaFcl': newClientXlRow[4],
        'deltaLcl': newClientXlRow[5],
        'deltaAir': newClientXlRow[6],

        'relevantPorts': newClientXlRow[7],
        'info': newClientXlRow[8]
    }
    return ClientLine(helperNewClientDict)


def get_Port_As_Object(portXlRow) -> PortLine:
    """
    :param portXlRow: (portName, portCode, portState, PortAliases)
    :return: new Object of type PortLine
    """
    helperNewPortlDict = {
            'portName': portXlRow[0],
            'portCode': portXlRow[1],
            'portState': portXlRow[2],
            'PortAliases': portXlRow[3],
    }
    return PortLine(helperNewPortlDict)
