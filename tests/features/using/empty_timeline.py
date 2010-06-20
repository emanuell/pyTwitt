from lettuce import *
from nose.tools import *
from pytwitt.core import Twitter, User

@step(r'Given a registred user\, (\S+) and (\S+)')
def given_a_registred_user(step, username, password):
	world.twitter = Twitter(username, password)

@step(r'When clean the timeline')
def when_clean_the_timeline(step):
	user = world.twitter.user
	
	user.clean_timeline()

@step(r'Then timeline should be empty')
def then_timeline_should_be_empty(step):
	user = world.twitter.user
	
	assert_equals(len(user.timeline()), 0)
