import os
from pymongo import MongoClient

class LalaBot:
    
#creamos una constante que contiene las frases
    MENSAJES = [
        {
            "dict":{
                "type": "section",
                "text":{
                    "type":"mrkdwn",
                    "text" : "Buenas Tardes!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text":{
                    "type":"mrkdwn",
                    "text" : "Stay whit me mayonakanadoa o tadaki"
                }
            }
        },{
            "dict":{
                "type": "section",
                "text":{
                    "type":"mrkdwn",
                    "text" : "Kaeranaide to naita"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text":{
                    "type":"mrkdwn",
                    "text" : "ano kisetsu ga ima-me no mae"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text":{
                    "type":"mrkdwn",
                    "text" : "kuchiguse o iinagara"
                }
            }
        }
    ]
    #Miki Matsubara - Stay With Me

    #constructor por defecto
    def __init__ (self, channel):
        self.channel = channel
        self.client = MongoClient(os.environ.get("MONGO_PORT"))
        self.db = self.client.mensajes
        self.mensajes = self.db.mensajes
        self.mensajes.insert_many(self.MENSAJES)

    #selecciona un mensaje random de la base de datos creada
    def _choose_message(self):
        return self.mensajes.aggregate([{ "$sample": {"size": 1} }]).next()["dict"]
             
   # craft and return the entire message payload as a dictionary
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._choose_message()
            ]
        }


