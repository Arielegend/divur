#
# clientName = {'firstName':'', 'lastName':''}
# containerForQuote = {'dv20':[(count1,weight1)], 'dv40':[(count2, weight2), (count3,weight3)]}
#
class DetailsForFclQuoteFob:
    def __init__(self, clientName, containerForQuote, ratesForClient, portOrigin, extraTaxes, thc, validEnds,
                 terms, companyName, portDestination):
        self.clientName = clientName
        self.containerForQuote = containerForQuote
        self.ratesForClient = ratesForClient
        self.portOrigin = portOrigin
        self.extraTaxes = extraTaxes
        self.thc = thc
        self.validEnds = validEnds
        self.terms = terms
        self.companyName = companyName
        self.portDestination = portDestination
