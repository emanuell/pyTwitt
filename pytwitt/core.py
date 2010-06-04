
import twitter as internal

class NotAuthenticated(Exception): pass

class User:

	def __init__(self, username=None, fullname=None, website=None, bio=None, location=None):
		self.username = username
		self.name = username
		self.fullname = fullname
		self.website = website
		self.bio = bio
		self.location = location


class Twitter:

	def __init__(self, username, password):
		self.__username = username
		self.__password = password

		self.__api = internal.Api(username, password)
		self.__user = None
		
		try:
			self.__user = self.__api.GetUser(username)
		except Exception:
			raise NotAuthenticated()
		
		self.user = User(self.__user.screen_name, self.__user.name, self.__user.url, self.__user.description, self.__user.location)
	
	def twitt(self, str):
		self.__api.PostUpdate(str)
