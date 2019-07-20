"""
Hydra API Vocab - Hydra Ecosystem Flock Demo."""

flock_doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "expectsHeader": "hydra:expectsHeader",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "manages": "hydra:manages",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readable": "hydra:readable",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "returnsHeader": "hydra:returnsHeader",
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://localhost:8080/api/vocab#",
        "writeable": "hydra:writeable"
    },
    "@id": "http://localhost:8080/api/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the server side system",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:State",
            "@type": "hydra:Class",
            "description": "Class for drone state objects",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "State not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "State Returned"
                        }
                    ],
                    "returns": "vocab:State",
                    "returnsHeader": [],
                    "title": "GetState"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "ture",
                    "required": true,
                    "title": "Speed",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": true,
                    "required": true,
                    "title": "Position",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Property",
                    "readable": true,
                    "required": true,
                    "title": "Direction",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readable": true,
                    "required": true,
                    "title": "Battery",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": true,
                    "required": true,
                    "title": "SensorStatus",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": true,
                    "required": true,
                    "title": "DroneID",
                    "writeable": true
                }
            ],
            "title": "State"
        },
        {
            "@id": "vocab:Command",
            "@type": "hydra:Class",
            "description": "Class for drone commands",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Command not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Command Returned"
                        }
                    ],
                    "returns": "vocab:Command",
                    "returnsHeader": [],
                    "title": "GetCommand"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Command",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "Command added"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "AddCommand"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "Command deleted"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "DeleteCommand"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": true,
                    "required": true,
                    "title": "DroneID",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readable": true,
                    "required": true,
                    "title": "State",
                    "writeable": true
                }
            ],
            "title": "Command"
        },
        {
            "@id": "vocab:Message",
            "@type": "hydra:Class",
            "description": "Class for messages received by the GUI interface",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Message not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Message returned"
                        }
                    ],
                    "returns": "vocab:Message",
                    "returnsHeader": [],
                    "title": "GetMessage"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Message deleted"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "DeleteMessage"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Text",
                    "readable": true,
                    "required": true,
                    "title": "MessageString",
                    "writeable": true
                }
            ],
            "title": "Message"
        },
        {
            "@id": "vocab:Area",
            "@type": "hydra:Class",
            "description": "Class for Area of Interest of the server",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Area",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Area of interest changed"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "UpdateArea"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Area of interest not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Area of interest returned"
                        }
                    ],
                    "returns": "vocab:Area",
                    "returnsHeader": [],
                    "title": "GetArea"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": true,
                    "required": true,
                    "title": "TopLeft",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": true,
                    "required": true,
                    "title": "BottomRight",
                    "writeable": true
                }
            ],
            "title": "Area"
        },
        {
            "@id": "vocab:Datastream",
            "@type": "hydra:Class",
            "description": "Class for a datastream entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Data not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Data returned"
                        }
                    ],
                    "returns": "vocab:Datastream",
                    "returnsHeader": [],
                    "title": "ReadDatastream"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Datastream",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Data updated"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "UpdateDatastream"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Data deleted"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "DeleteDatastream"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/QuantitativeValue",
                    "readable": true,
                    "required": true,
                    "title": "Temperature",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": true,
                    "required": true,
                    "title": "DroneID",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": true,
                    "required": true,
                    "title": "Position",
                    "writeable": true
                }
            ],
            "title": "Datastream"
        },
        {
            "@id": "vocab:Drone",
            "@type": "hydra:Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Drone",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Drone updated"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "SubmitDrone"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Drone",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Drone added"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "CreateDrone"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Drone not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Drone Returned"
                        }
                    ],
                    "returns": "vocab:Drone",
                    "returnsHeader": [],
                    "title": "GetDrone"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Drone not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Drone successfully deleted"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "DeleteDrone"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readable": true,
                    "required": true,
                    "title": "DroneState",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/name",
                    "readable": true,
                    "required": true,
                    "title": "name",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readable": true,
                    "required": true,
                    "title": "model",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": true,
                    "required": true,
                    "title": "MaxSpeed",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readable": true,
                    "required": true,
                    "title": "Sensor",
                    "writeable": true
                }
            ],
            "title": "Drone"
        },
        {
            "@id": "vocab:LogEntry",
            "@type": "hydra:Class",
            "description": "Class for a log entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 404,
                            "title": "Log entry not found"
                        },
                        {
                            "description": "",
                            "statusCode": 200,
                            "title": "Log entry returned"
                        }
                    ],
                    "returns": "vocab:LogEntry",
                    "returnsHeader": [],
                    "title": "GetLog"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:LogEntry",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "Log entry created"
                        }
                    ],
                    "returns": null,
                    "returnsHeader": [],
                    "title": "AddLog"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": true,
                    "required": false,
                    "title": "DroneID",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/UpdateAction",
                    "readable": false,
                    "required": false,
                    "title": "Update",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/ReplyAction",
                    "readable": false,
                    "required": false,
                    "title": "Get",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/SendAction",
                    "readable": false,
                    "required": false,
                    "title": "Send",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readable": false,
                    "required": false,
                    "title": "State",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Datastream",
                    "readable": false,
                    "required": false,
                    "title": "Data",
                    "writeable": true
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Command",
                    "readable": false,
                    "required": false,
                    "title": "Command",
                    "writeable": true
                }
            ],
            "title": "LogEntry"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": null,
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": null,
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": null,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "vocab:CommandCollection",
            "@type": "hydra:Class",
            "description": "A collection of command",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:command_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Command entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:CommandCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:command_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Command entity",
                    "expects": "vocab:Command",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the Command entity was created successfully."
                        }
                    ],
                    "returns": "vocab:Command",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The command",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "CommandCollection"
        },
        {
            "@id": "vocab:StateCollection",
            "@type": "hydra:Class",
            "description": "A collection of state",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:state_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all State entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:StateCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:state_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new State entity",
                    "expects": "vocab:State",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the State entity was created successfully."
                        }
                    ],
                    "returns": "vocab:State",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The state",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "StateCollection"
        },
        {
            "@id": "vocab:MessageCollection",
            "@type": "hydra:Class",
            "description": "A collection of message",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:message_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Message entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:MessageCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:message_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Message entity",
                    "expects": "vocab:Message",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the Message entity was created successfully."
                        }
                    ],
                    "returns": "vocab:Message",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The message",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "MessageCollection"
        },
        {
            "@id": "vocab:DroneCollection",
            "@type": "hydra:Class",
            "description": "A collection of drone",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:drone_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Drone entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DroneCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:drone_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Drone entity",
                    "expects": "vocab:Drone",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the Drone entity was created successfully."
                        }
                    ],
                    "returns": "vocab:Drone",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The drone",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "DroneCollection"
        },
        {
            "@id": "vocab:LogEntryCollection",
            "@type": "hydra:Class",
            "description": "A collection of logentry",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:logentry_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all LogEntry entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:LogEntryCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:logentry_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new LogEntry entity",
                    "expects": "vocab:LogEntry",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the LogEntry entity was created successfully."
                        }
                    ],
                    "returns": "vocab:LogEntry",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The logentry",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "LogEntryCollection"
        },
        {
            "@id": "vocab:DatastreamCollection",
            "@type": "hydra:Class",
            "description": "A collection of datastream",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:datastream_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Datastream entities",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DatastreamCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:datastream_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Datastream entity",
                    "expects": "vocab:Datastream",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "",
                            "statusCode": 201,
                            "title": "If the Datastream entity was created successfully."
                        }
                    ],
                    "returns": "vocab:Datastream",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The datastream",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": true,
                    "required": false,
                    "title": "members",
                    "writeable": true
                }
            ],
            "title": "DatastreamCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://schema.org/FindAction",
                    "description": "The APIs main entry point.",
                    "expects": null,
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": "vocab:EntryPoint",
                    "returns": null,
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Area Class",
                    "hydra:title": "area",
                    "property": {
                        "@id": "vocab:EntryPoint/Area",
                        "@type": "hydra:Link",
                        "description": "Class for Area of Interest of the server",
                        "domain": "vocab:EntryPoint",
                        "label": "Area",
                        "range": "vocab:Area",
                        "supportedOperation": [
                            {
                                "@id": "updatearea",
                                "@type": "http://schema.org/UpdateAction",
                                "description": null,
                                "expects": "vocab:Area",
                                "expectsHeader": [],
                                "label": "UpdateArea",
                                "method": "POST",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "Area of interest changed"
                                    }
                                ],
                                "returns": null,
                                "returnsHeader": []
                            },
                            {
                                "@id": "getarea",
                                "@type": "http://schema.org/FindAction",
                                "description": null,
                                "expects": null,
                                "expectsHeader": [],
                                "label": "GetArea",
                                "method": "GET",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 404,
                                        "title": "Area of interest not found"
                                    },
                                    {
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "Area of interest returned"
                                    }
                                ],
                                "returns": "vocab:Area",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The CommandCollection collection",
                    "hydra:title": "commandcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/CommandCollection",
                        "@type": "hydra:Link",
                        "description": "The CommandCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "CommandCollection",
                        "range": "vocab:CommandCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:command_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Command entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:CommandCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:command_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Command entity",
                                "expects": "vocab:Command",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the Command entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:Command",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The StateCollection collection",
                    "hydra:title": "statecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/StateCollection",
                        "@type": "hydra:Link",
                        "description": "The StateCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "StateCollection",
                        "range": "vocab:StateCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:state_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all State entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:StateCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:state_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new State entity",
                                "expects": "vocab:State",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the State entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:State",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The MessageCollection collection",
                    "hydra:title": "messagecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/MessageCollection",
                        "@type": "hydra:Link",
                        "description": "The MessageCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "MessageCollection",
                        "range": "vocab:MessageCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:message_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Message entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:MessageCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:message_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Message entity",
                                "expects": "vocab:Message",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the Message entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:Message",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The DroneCollection collection",
                    "hydra:title": "dronecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DroneCollection",
                        "@type": "hydra:Link",
                        "description": "The DroneCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DroneCollection",
                        "range": "vocab:DroneCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:drone_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Drone entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:DroneCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:drone_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Drone entity",
                                "expects": "vocab:Drone",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the Drone entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:Drone",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The LogEntryCollection collection",
                    "hydra:title": "logentrycollection",
                    "property": {
                        "@id": "vocab:EntryPoint/LogEntryCollection",
                        "@type": "hydra:Link",
                        "description": "The LogEntryCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "LogEntryCollection",
                        "range": "vocab:LogEntryCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:logentry_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all LogEntry entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:LogEntryCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:logentry_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new LogEntry entity",
                                "expects": "vocab:LogEntry",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the LogEntry entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:LogEntry",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                },
                {
                    "hydra:description": "The DatastreamCollection collection",
                    "hydra:title": "datastreamcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DatastreamCollection",
                        "@type": "hydra:Link",
                        "description": "The DatastreamCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DatastreamCollection",
                        "range": "vocab:DatastreamCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:datastream_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Datastream entities",
                                "expects": null,
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:DatastreamCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:datastream_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Datastream entitity",
                                "expects": "vocab:Datastream",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "If the Datastream entity was created successfully."
                                    }
                                ],
                                "returns": "vocab:Datastream",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": true,
                    "required": null,
                    "writeable": false
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "API Doc for the server side API"
}