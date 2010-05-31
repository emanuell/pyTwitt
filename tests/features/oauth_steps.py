#!/usr/bin/env python
# encoding: utf-8

from lettuce import *
from pytwitt.twitter import *

@before.all
def init():
	world.keys = {}

@step('Given consumer key (\S+)')
def given_consumer_key(step, consumer_key):
	world.keys['consumer'] = consumer_key
	
@step('And consumer secret (\S+)')
def and_consumer_secret(step, consumer_secret):
	world.keys['secret'] = consumer_secret
	
@step('When request for request token')
def when_request_for_request_token(step):
	world.request_token = OAuthApi(world.keys['consumer'], world.keys['secret'])

@step('Then request token should be returned')
def then_request_token_should_be_returned(step):
	assert world.request_token