from lettuce import *
from nose.tools import *
from pytwitt.core import Twitter, User

@step(r'Given my user object')
def given_my_user_object(step):
	username = 'pytwitt2'
	password = 'abc123456'
	world.twitter = Twitter(username, password)

@step(r'Then my username should be (\S+)')
def then_my_username_should_be_pytwitt2(step, username):
	assert_not_equals(world.twitter.user, None)
	assert_equals(world.twitter.user.username, username)

@step(r'And my fullname should be Emanuell Faustino')
def and_my_fullname_should_be_emanuell_faustino(step):
	assert_equals(world.twitter.user.fullname, 'Emanuell Faustino')

@step(r'And my website should be http\:\/\/twitter\.com\/emanuell')
def and_my_website_should_be_http_twitter_com_emanuell(step):
    assert_equals(world.twitter.user.website, 'http://twitter.com/emanuell')

@step(r'And my bio should be Nothing yet')
def and_my_bio_should_be_nothing_yet(step):
    assert_equals(world.twitter.user.bio, 'Nothing yet')

@step(r'And my location should be Recife')
def and_my_location_should_be_recife(step):
    assert_equals(world.twitter.user.location, 'Recife')

