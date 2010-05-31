#!/usr/bin/env python
# encoding: utf-8

Feature: Twitter OAuth authentication
	As a registred user
	I want authenticate with own username and password
	So that I can use the Twitter
	
	Scenario: Get authenticate_token 
		Given consumer key xxxx
		And consumer secret yyyy
		When request for request token
		Then request token should be returned