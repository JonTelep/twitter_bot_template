# ================================================================
# File Name: lib_tweepy.py
# Created by: Telep IO https://www.telep.io/
# Date: 2/7/2022
# 
# Please go to lib_tweepy_auth.py for steps
# ================================================================

from lib_tweepy_auth import OAuth

# lib_tweepy class to condense common needs with some guard rails in place
class lib_tweepy:
    api = OAuth()

    def __init__(self, status="DONOTTWEET", reply_id = "DONOTREPLY", del_id="false"):
        self.status = status
        self.reply_id = reply_id
        self.del_id = del_id      
    
    def Create_Tweet(self):
        if self.status != "DONOTTWEET":
            response = self.api.update_status(self.status)
            return response.id_str
        else:
            return "Default value was specified"
    
    def Delete_Tweet(self):
        if self.del_id != "false":
            response = self.api.destroy_status(self.del_id)
            return response
        else:
            return "Default value was specified"
        
    def Reply_Tweet(self):
        if self.status != "DONOTREPLY":
            response = self.api.update_status(self.status, in_reply_to_status_id = self.reply_id)
            return response.id_str
        else:
            return "Default value was specified"    
