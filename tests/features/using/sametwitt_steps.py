from lettuce import *
from pytwitt.core import Twitter, User

@step(r'Given username (\S+) and password (\S+)')
def given_username_and_password(step, username, password):
	world.twitter = Twitter(username, password)

@step(r'When post the same tweet "(.*)"')
def when_post_the_same_twitt(step, twitt):
	user = world.twitter.user
	
	world.result = user.twitt(twitt)

@step(r'Then twitter should return (.*)')
def then_twitter_should_return(step, str_boolean):
	user = world.twitter.user
	
	expected = True if str_boolean == 'True' else False
	
	assert world.result == expected, 'got %s' % world.result
