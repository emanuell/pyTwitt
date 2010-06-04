from lettuce import *
from pytwitt.core import Twitter, User

@step(r'Given my user')
def given_my_user(self):
	pass

@step(r'When I write a twitt')
def when_i_write_a_twitt(step):
    pass
	#world.twitter.twitt('testing 332323')

@step(r'Then my user status should be changed')
def then_my_user_status_should_be_changed(step):
    pass
	#assert world.twitter.last_status = 'testing 123', 'Got %s' % world.twitter.last_status

@step(r'And twitt should be appear in timeline')
def and_twitt_should_be_appear_in_timeline(step):
    pass
