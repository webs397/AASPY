
true = True
null = None
false = False
coreAAS = {
  "AAS": {
    "hasDataSpecification": [],
    "derivedFrom": null,
    "asset": {
      "keys": [
        {
          "type": "Asset",
          "local": true,
          "value": "http://customer.com/assets/KHBVZJSQKIY",
          "index": 0,
          "idType": "IRI"
        }
      ]
    },
    "submodels": [
      {
        "keys": [
          {
            "type": "Submodel",
            "local": true,
            "value": "http://i40.customer.com/type/1/1/F13E8576F6488342",
            "index": 0,
            "idType": "IRI"
          }
        ]
      },
      {
        "keys": [
          {
            "type": "Submodel",
            "local": true,
            "value": "http.//i40.customer.com/type/1/1/7A7104BDAB57E184",
            "index": 0,
            "idType": "IRI"
          }
        ]
      },
      {
        "keys": [
          {
            "type": "Submodel",
            "local": true,
            "value": "http://i40.customer.com/instance/1/1/AC69B1CB44F07935",
            "index": 0,
            "idType": "IRI"
          }
        ]
      },
      {
        "keys": [
          {
            "type": "Submodel",
            "local": true,
            "value": "http://i40.customer.com/type/1/1/1A7B62B529F19152",
            "index": 0,
            "idType": "IRI"
          }
        ]
      }
    ],
    "conceptDictionaries": [],
    "identification": {
      "idType": "IRI",
      "id": "http://customer.com/aas/9175_7013_7091_9168"
    },
    "administration": null,
    "idShort": "ExampleMotor",
    "category": "CONSTANT",
    "modelType": {
      "name": "AssetAdministrationShell"
    },
    "descriptions": null
  },
  "Asset": {
    "hasDataSpecification": [],
    "assetIdentificationModelRef": {
      "keys": [
        {
          "type": "Submodel",
          "local": true,
          "value": "i40.customer.com/type/1/1/F13E8576F6488342",
          "index": 0,
          "idType": "IRI"
        }
      ]
    },
    "billOfMaterialRef": null,
    "identification": {
      "idType": "IRI",
      "id": "http://customer.com/assets/KHBVZJSQKIY"
    },
    "administration": null,
    "idShort": "ServoDCMotor",
    "category": "",
    "modelType": {
      "name": "Asset"
    },
    "kind": "Instance",
    "descriptions": null
  }
}




# data from /geteventmessages 
event = [
  {
    "Payloads": [
      {
        "$type": "AasPayloadUpdateValue",
        "Values": [
          {
            "Path": [
              {
                "type": "Property",
                "local": true,
                "value": "RotationSpeed",
                "index": 0,
                "idType": "IdShort"
              }
            ],
            "Value": "60"
          }
        ]
      }
    ],
    "Source": {
      "keys": [
        {
          "type": "BasicEvent",
          "local": true,
          "value": "testEvent",
          "index": 0,
          "idType": "IdShort"
        }
      ]
    },
    "SourceSemanticId": {
      "keys": [
        {
          "type": "ConceptDescription",
          "local": false,
          "value": "https://admin-shell.io/tmp/AAS/Events/UpdateValueOutwards",
          "index": 0,
          "idType": "IRI"
        }
      ]
    },
    "ObservableReference": {
      "keys": [
        {
          "type": "Submodel",
          "local": true,
          "value": "http://i40.customer.com/instance/1/1/AC69B1CB44F07935",
          "index": 0,
          "idType": "IRI"
        }
      ]
    },
    "ObservableSemanticId": {
      "keys": [
        {
          "type": "GlobalReference",
          "local": false,
          "value": "0173-1#01-AFZ615#016",
          "index": 0,
          "idType": "IRDI"
        }
      ]
    },
    "Timestamp": "2022-08-23T14:11:45.5357555Z"
  }
]