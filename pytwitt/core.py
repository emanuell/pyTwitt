
import twitter as internal

class NotAuthenticated(Exception): pass

class User(object):

	def __init__(self, username=None, password=None):
		self.username = username
		self.__password = password
		
		self.__api = internal.Api(username, password, None)
		
		try:
			self.__user = self.__api.GetUser(username)
		except Exception:
			raise NotAuthenticated()
		
		self.name = username
		self.fullname = self.__user.name
		self.website = self.__user.url
		self.bio = self.__user.description
		self.location = self.__user.location
		self.id = self.__user.id
		
		if self.__user.status != None:
			self.status = self.__user.status.text
		else:
			self.status = None
		
		self._set_timeline()
	
	def clean_timeline(self):
		real_timeline = self.__api.GetUserTimeline()
		for status in real_timeline:
			self.__api.DestroyStatus(status.id)
	
	def tweet(self, msg):
		try:
			msg = str(msg)
			user_status = self.__api.PostUpdate(msg)
		except Exception, e:
			return False
		
		if user_status:
			self.status = user_status.text
			self.__timeline.insert(0, self.status)
		
		
		return True
	
	def last_tweet(self):
		return self.status
	
	def _set_timeline(self):
		timeline = self.__api.GetUserTimeline(self.username)
		self.__timeline = []
		
		for status in timeline:
			self.__timeline.append(status.text)
		
	
	def timeline(self):
		timeline_copy = self.__timeline[:]
		return timeline_copy
	

class Twitter(object):

	def __init__(self, username, password):
		self.user = User(username, password)
	
