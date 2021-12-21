class PortLine:
    portName = None
    portCode = None
    portState = None
    portAliases = None

    def __init__(self, portDict: dict):
        self.portName = portDict['portName']
        self.portCode = portDict['portCode']
        self.portState = portDict['portState']
        self.portAliases = portDict['PortAliases']


