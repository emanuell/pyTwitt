
from lettuce import *
from pytwitt.core import Twitter, User

@step('given my username (\S+)')
def given_my_username(step, username):
	world.username = username

@step('And my secret password (\S+)')
def and_my_secret_password(step, password):
	world.password = password

@step('When I request for access')
def when_i_request_for_access(step):
	world.twitter = Twitter(world.username, world.password)
	

@step('Then my user (\S+) object should be returned')
def then_my_user_should_be_returned(step, username):
	twitter = world.twitter
	
	assert twitter
	assert twitter.user, 'Got %s' % twitter.user
	assert username == twitter.user.name, 'Got %s' % twitter.user.name
	
#============================================================================================================

@step(r'Given my user object')
def given_my_user_object(step):
	twitter = Twitter(world.username, world.password)
	world.user = twitter.user

@step(r'Then my username should be (\S+)')
def then_my_username_should_be_pytwitt2(step, username):
	assert world.user.username == username, 'Got %s' % world.user.username

@step(r'And my fullname should be Emanuell Faustino')
def and_my_fullname_should_be_emanuell_faustino(step):
	assert world.user.fullname == 'Emanuell Faustino', 'Got %s' % world.user.fullname

@step(r'And my website should be http\:\/\/twitter\.com\/emanuell')
def and_my_website_should_be_http_twitter_com_emanuell(step):
    assert world.user.website == 'http://twitter.com/emanuell', 'Got %s' % world.user.website

@step(r'And my bio should be Nothing yet')
def and_my_bio_should_be_nothing_yet(step):
    assert world.user.bio == 'Nothing yet', 'Got %s' % world.user.bio

@step(r'And my location should be Recife')
def and_my_location_should_be_recife(step):
    assert world.user.location == 'Recife', 'Got %s' % world.user.location

#==============================================================================================================

