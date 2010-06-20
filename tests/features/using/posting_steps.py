from lettuce import *
from pytwitt.core import Twitter, User


@step(r'Given my username (\S+) and password (\S+)')
def given_my_username_and_password(step, username, password):
	world.twitter = Twitter(username, password)

@step(r'When post the tweet "(.*)"')
def when_post_a_twitt(step, twitt):
	user = world.twitter.user
	
	world.result = user.tweet(twitt)

@step(r'Then twitter should return (.*)')
def then_twitter_should_return(step, str_boolean):
	expected = True if str_boolean == 'True' else False
	assert world.result == expected, 'Got %s / same twitt before?' % world.result

@step(r'And my user status should be changed to "(.*)"')
def And_my_user_status_should_be_changed(step, twitt):
	user = world.twitter.user
	assert user.status == twitt, 'got %s' % user.status

@step(r'And tweet "(.*)" should be last tweet')
def and_twitt_should_be_in_timeline(step, twitt):
	user = world.twitter.user
	assert user.last_tweet() == twitt, 'got %s' % user.last_twitt
