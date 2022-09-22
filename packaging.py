
import json
from datetime import datetime


true = True
false = False

class Event():

    def __init__(self):
        self.values = []
        self.payloads  = []
        self.sourceKeys = []
        self.sourceSemIdKeys = []
        self.observableRefKeys = []
        self.observableSemIdKeys = []
        self.events = []


    def generate_event(self, submodelElement, submodelElementEvent):
        self.events = []
        self.generate_value(submodelElement)
        self.generate_payload()
        self.generate_source(submodelElementEvent)
        self.generate_source_semId(submodelElementEvent)
        self.generate_observable_semId(submodelElementEvent)
        self.generate_observable_ref(submodelElementEvent)
        self.generate_timestamp()
        dict = {"Payloads": self.payloads, "Source": self.source, "SourceSemanticId": self.sourceSemId, "ObservableReference": self.observableRef, "ObservableSemanticId": self.observableRef, "Timestamp": self.timestamp}
        self.event = dict
        self.events.append(self.event)


    def generate_payload(self):
        self.payload = {"$type": "AasPayloadUpdateValue", "Values": self.values}
        self.payloads.append(self.payload)


    def generate_value(self, subModelElement):
        path_dict = {"type": subModelElement.category, "local": subModelElement.local, "value": subModelElement.idShort, "index": subModelElement.index, "idType": subModelElement.idType}
        path = path_dict
        self.value = {"Path": [path], "Value": str(subModelElement.value)}
        self.values.append(self.value)


    def generate_source(self, subModelEvent):
        dict = {"type": subModelEvent.type, "local": subModelEvent.local, "value": subModelEvent.idShort, "index": subModelEvent.index, "idType": subModelEvent.idType}
        self.sourceKey = dict
        self.sourceKeys.append(self.sourceKey)
        self.source = {"keys": self.sourceKeys}

    def generate_source_semId(self, subModelEvent):
        dict = {"type": subModelEvent.semIdType, "local": subModelEvent.semIdLocal, "value": subModelEvent.semId, "index": subModelEvent.index, "idType": subModelEvent.semIdIdType}
        self.sourceSemIdKey = dict
        self.sourceSemIdKeys. append(self.sourceSemIdKey)
        self.sourceSemId = {"keys": self.sourceSemIdKeys}

    def generate_observable_ref(self, subModelEvent):
        dict = {"type": subModelEvent.observableType, "local": subModelEvent.observableLocal, "value": subModelEvent.observableId, "index": subModelEvent.index, "idType": subModelEvent.observableIdType}
        self.observableRefKey = dict
        self.observableRefKeys.append(self.observableRefKey)
        self.observableRef = {"keys": self.observableRefKeys}


    def generate_observable_semId(self, subModelEvent):
        dict = {"type": subModelEvent.observableSemIdType, "local": subModelEvent.observableSemIdLocal, "value": subModelEvent.observableSemId, "index": subModelEvent.index, "idType": subModelEvent.observableSemIdIdType}
        self.observableSemIdKey = dict
        self.observableSemIdKeys.append(self.observableSemIdKey)
        self.observableSemIdRef = {"keys": self.observableSemIdKeys}

    def generate_timestamp(self):
        self.timestamp = datetime.now()
        self.timestamp = self.timestamp.isoformat()+"Z"


    def clear_events(self):
        self.values = []









