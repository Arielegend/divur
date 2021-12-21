class RateFclLine:
    # portName, portCode, region, state, carrier, dv20_Ashdod, dv40_Ashdod, hq40_Ashdod, dv20_Haifa, dv40_Haifa, hq40_Haifa, validStart, validEnd
    portName = None
    portCode = None
    region = None
    state = None
    carrier = None

    ratesAshDod = None
    ratesHaifa = None

    validStart = None
    validEnd = None

    def __init__(self, rateFclLine: dict):
        self.portName = rateFclLine['portName']
        self.portCode = rateFclLine['portCode']
        self.region = rateFclLine['region']
        self.state = rateFclLine['state']
        self.carrier = rateFclLine['carrier']

        self.ratesAshDod = [int(rateFclLine['dv20_Ashdod']), int(rateFclLine['dv40_Ashdod']), int(rateFclLine['hq40_Ashdod'])]
        self.ratesHaifa = [int(rateFclLine['dv20_Haifa']), int(rateFclLine['dv40_Haifa']), int(rateFclLine['hq40_Haifa'])]


        self.validStart = rateFclLine['validStart']
        self.validEnd = rateFclLine['validEnd']

        # print(self.ratesAshDod)

