class JamesBot:

    #constructor por defecto
    def __init__ (self, channel):
        self.channel = channel
        

    def _choose_message(self):
        return {"type": "section","text":{"type":"mrkdwn","text" : "buenos dias!"}}

   # craft and return the entire message payload as a dictionary
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._choose_message()
            ]
        }


