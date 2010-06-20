
from lettuce import *
from nose.tools import *
from pytwitt.core import Twitter, User

@step(r'Given username (\S+)')
def given_my_username(step, username):
	world.username = username

@step(r'And my secret password (\S+)')
def and_my_secret_password(step, password):
	world.password = password

@step(r'When I request for access')
def when_i_request_for_access(step):
	world.twitter = Twitter(world.username, world.password)

@step(r'Then my user (\S+) object should be returned')
def then_my_user_should_be_returned(step, username):
	twitter = world.twitter
	
	assert twitter
	assert_not_equals(twitter.user, None)
	assert_equals(username, twitter.user.name)
