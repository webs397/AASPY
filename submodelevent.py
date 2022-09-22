

true = True
false = False

class submodelevent():
    def __init__(self):
        pass

    def generate_dummy(self):
        self.type = "BasicEvent"
        self.local = true
        self.idShort = "testEvent"
        self.index = 0
        self.idType = "IdShort"
        self.semIdType = "ConceptDescription"
        self.semIdLocal = false
        self.semId = "https://admin-shell.io/tmp/AAS/Events/UpdateValueOutwards"
        self.semIdIdType = "IRI"
        self.observableType = "Submodel"
        self.observableLocal = true
        self.observableId = "http://i40.customer.com/instance/1/1/AC69B1CB44F07935"
        self.observableIdType = "IRI"
        self.observableSemIdType = "GlobalReference"
        self.observableSemIdLocal = false
        self.observableSemId = "0173-1#01-AFZ615#016"
        self.observableSemIdIdType = "IRDI"