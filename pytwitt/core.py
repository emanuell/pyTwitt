
import twitter as internal

class NotAuthenticated(Exception): pass

class User(object):

	def __init__(self, username=None, password=None):
		self.username = username
		self.__password = password
		
		self.__api = internal.Api(username, password)
		
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
		self.status = self.__user.status
		self.timeline = []
	
	def twitt(self, msg):
		try:
			msg = str(msg)
			user_status = self.__api.PostUpdate(msg)
		except Exception, e:
			return False
		
		if user_status:
			self.status = user_status.text
			self._set_timeline()
		
		return True
	
	def last_twitt(self):
		return self.status
	
	def _set_timeline(self):
		timeline = self.__api.GetUserTimeline(self.username)
		
		for status in timeline:
			self.timeline.append(status.text)
	

class Twitter(object):

	def __init__(self, username, password):
		self.user = User(username, password)
	
