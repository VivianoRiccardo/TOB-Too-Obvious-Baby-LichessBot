from rauth import OAuth2Service
from requests_oauthlib import OAuth2Session
import json
import pickle


class IdSession:
    
    def __init__(self, id_file):
        f = open(id_file,"rb")
        self.session = pickle.load(f)
        f.close()
        self.account_inf = '/api/account'
        self.account_email = '/api/account/email'
        self.account_preferences = '/api/account/preferences'
        self.account_kid_status = '/api/account/kid'
        self.account_user_status = '/api/users/status'
        self.top_ten_players = '/player'
        self.leaderboard = '/player/top/'
        self.public_data = '/api/user/'
        self.rating_history = '/api/user/{username}/rating-history'
        self.usr_activity = '/api/user/{username}/activity'
        self.puzzle_activity = '/api/user/puzzle-activity'
        self.users = 'api/users'
        self.team = '/team/{teamId}/users'
        self.live_streamers = '/streamer/live'
        self.perfTypes = ["ultraBullet","bullet","blitz","rapid","classical","chess960","crazyhouse","antichess","atomic","horde","kingOfTheHill","racingKings","threeCheck"]
        
    
    
    def getStatusCode(self,response_obj):
        return response_obj.status_code
    
    def getContent(self,response_obj):
        return json.loads(str(response_obj.content.decode('utf-8')))    
    
    def getDictParams(self,response_obj):
        return response_obj.__dict__
    
    def getHtmlContent(self,response_obj):
        return response_obj.content.decode('utf-8') #for getTopTenPlayers,getPuzzleActivity
        
    def getAccountInformation(self):
        return self.session.get(self.account_inf)
    def getAccountEmail(self):
        return self.session.get(self.account_email)
    def getAccountPreferences(self):
        return self.session.get(self.account_preferences)
    def getAccountKidStatus(self):
        return self.session.get(self.account_kid_status)
    def setAccountKidStatus(self):
        return self.session.post(self.account_kid_status, params={'v':'true'})
    def getUserStatus(self,ids):
        return self.session.get(self.account_user_status, params={'ids':ids})
    def getTopTenPlayers(self):
        return self.session.get(self.top_ten_players)
    def getLeaderboard(self,nb,perfType):
        s = str(nb)+'/'+str(perfType)
        return self.session.get(self.leaderboard+s)
    def getPublicData(self,username):
        return self.session.get(self.public_data+username)
    def getRatingHistory(self,username):
        return self.session.get(self.rating_history[:self.rating_history.find('{')]+username+self.rating_history[self.rating_history.find('}')+1:])
    def getUserActivity(self,username):
        return self.session.get(self.usr_activity[:self.usr_activity.find('{')]+username+self.usr_activity[self.usr_activity.find('}')+1:])
    def getPuzzleActivity(self,count):
        if(count == 0):
            return self.session.get(self.puzzle_activity)
        else:
            return self.session.get(self.puzzle_activity,params={'max':str(count)})
    def getUsersById(self,ids):
        return self.session.post(self.users,params=ids)
    
    def getMembersTeam(self,teamIds):
        return self.session.get(self.team[:self.team.find('{')]+teamIds+self.team[self.team.find('}')+1:])
    
    def getLiveStreamer(self):
        return self.session.get(self.live_streamers)

session = IdSession("bottest2.bin")
r = session.getAccountInformation()
ids = session.getContent(r)["id"]
usr = session.getContent(r)["username"]
r = session.getUserActivity(usr)
r = session.getLiveStreamer()
print(session.getStatusCode(r))

