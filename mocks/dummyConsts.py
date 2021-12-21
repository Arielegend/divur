from model.detailsFclQuote import DetailsForFclQuoteFob

# def __init__(self, clientName, containerForQuote, ratesForClient, portOrigin, extraTaxes, thc, validEnds,
#              terms, companyName, portDestination):

clientName = {'firstName': 'Yeled', 'lastName': 'Zevel'}
containerForQuote = {'dv20': 3, 'hq40': 5}
ratesForClient = {'dv20': 1000, 'dv40': 1500, 'hq40': 2000}
portOrigin = "Ningbo"
extraTaxes = {
    'x': {'taxName': 'FclTax1', 'value': 1000, 'currency': "NIS"},
    'y': {'taxName': 'FclTax2', 'value': 2000, 'currency': "USD"}
}
thc = {'thc20': 200, 'thc40': 400}
validEnds = "1-2-2022"
terms = "FCL FOB"
companyName = "Zebra Shell Haolamot"
portDestination = "ASHDOD"
detailsFclQuoteDummy = DetailsForFclQuoteFob(clientName=clientName,
                                             containerForQuote=containerForQuote,
                                             ratesForClient=ratesForClient,
                                             portOrigin=portOrigin,
                                             extraTaxes=extraTaxes,
                                             thc=thc,
                                             validEnds=validEnds,
                                             terms=terms,
                                             companyName=companyName,
                                             portDestination=portDestination)
