# firstName, lastName, email, phone, deltaFcl, deltaLcl, deltaAir, relevantPorts, info

class ClientLine:
    firstName = None
    lastName = None
    email = None
    phone = None

    deltaFcl = None
    deltaLcl = None
    deltaAir = None

    relevantPorts = None
    info = None

    def __init__(self, newClientDict: dict):
        self.firstName = newClientDict['firstName']
        self.lastName = newClientDict['lastName']
        self.email = newClientDict['email']
        self.phone = newClientDict['phone']

        self.deltaFcl = newClientDict['deltaFcl']
        self.deltaLcl = newClientDict['deltaLcl']
        self.deltaAir = newClientDict['deltaAir']

        self.relevantPorts = newClientDict['relevantPorts']
        self.info = newClientDict['info']

