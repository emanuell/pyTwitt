from lettuce import *
from nose.tools import *
from pytwitt.core import Twitter, User

@step(r'Given username (\S+) and password (\S+)')
def given_username_and_password(step, username, password):
	world.twitter = Twitter(username, password)

@step(r'When tweet "(.*)"')
def when_twitt_msg1(step, msg):
	user = world.twitter.user
	
	posted = user.tweet(msg)
	assert_true(posted)

@step(r'And tweet "(.*)"')
def and_twitt_msg2(step, msg):
	user = world.twitter.user
	
	posted = user.tweet(msg)
	assert_true(posted)

@step(r'Then timeline should be "(.*)" first')
def then_timeline_should_be_msg2_first(step, msg2):
	user = world.twitter.user
	
	assert_not_equals(user.timeline(), None)
	assert_equals(user.timeline()[0], msg2)

@step(r'And "(.*)" should be second')
def and_group1_should_be_second(step, msg1):
	user = world.twitter.user
	
	assert_equals(user.timeline()[1], msg1)