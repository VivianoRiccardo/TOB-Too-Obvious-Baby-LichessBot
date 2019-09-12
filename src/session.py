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
        self.titled_users = '/api/users/titled'
        self.users_following = '/api/user/{username}/following'
        self.users_followers = '/api/user/{username}/followers'
        self.export_game = '/game/export/{gameId}'
        self.export_current_game = '/games/export/_ids'
        self.export_game_of_user = '/api/games/user/{username}'
        self.ongoing_games = '/api/account/playing'
        self.tv_games = '/tv/channels'
        self.streaming_game = '/api/bot/game/stream/{gameId}'
        self.perfTypes = ["ultraBullet","bullet","blitz","rapid","classical","chess960","crazyhouse","antichess","atomic","horde","kingOfTheHill","racingKings","threeCheck"]
        self.titles = ["GM","WGM","IM","WIM","FM","WFM","NM","CM","WCM","WNM","LM","BOT"]
        
    
    
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
        return self.session.post(self.users,data=ids)
    
    def getMembersTeam(self,teamIds):
        return self.session.get(self.team[:self.team.find('{')]+teamIds+self.team[self.team.find('}')+1:])
    
    def getLiveStreamer(self):
        return self.session.get(self.live_streamers)
    def getUsersByTitle(self,titles,online):
        return self.session.get(self.titled_users,params={'titles':titles,'online':online})
    def getUserFollowing(self,username):
        return self.session.get(self.users_following[:self.users_following.find('{')]+username+self.users_following[self.users_following.find('}')+1:])
    def getUserFollowers(self,username):
        return self.session.get(self.users_followers[:self.users_followers.find('{')]+username+self.users_followers[self.users_followers.find('}')+1:])
    def getGameById(self,gameIds,move,tags,clocks,evals,opening,literate):
        return self.session.get(self.export_game[:self.export_game.find('{')]+gameIds,params={'move':move,'tags':tags,'clocks':clocks,'evals':evals,'opening':opening,'literate':literate})
    def getGamesByUsr(self,username,since = 0,until = 0,maxs = 0,vs = 0,rated = 0,perfType = 0,color = 0,analysed = 0,ongoing = 0,moves = 0,tags = 0,clocks = 0,evals = 0,opening = 0):
        #return self.session.get(self.export_game_of_user[:self.export_game_of_user.find('{')]+username,params={'since':since,'until':until,'max':maxs,'vs':vs,'rated':rated,'perfType':perfType,'color':color,'analysed':analysed,'ongoing':ongoing,'moves':moves,'tags':tags,'clocks':clocks,'evals':evals,'opening':opening})
        return self.session.get(self.export_game_of_user[:self.export_game_of_user.find('{')]+username)
    def getCurrentGamesById(self,gameIds,moves,tags,clocks,evals,opening):
        return self.session.post(self.export_current_game,data=gameIds)
    def getOngoingGames(self,number):
        return self.session.get(self.ongoing_games,params={'nb':number})
    def getTvGames(self):
        return self.session.get(self.tv_games)
    def getRealTimeGameById(self,ids):
        print(self.streaming_game[:self.streaming_game.find('{')]+ids)
        return self.session.get(self.streaming_game[:self.streaming_game.find('{')]+ids)



