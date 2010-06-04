Feature: Twitter use
	As a registred twitter user
	I want post twitts
	So that I can update my status and interact with friends
	
	Scenario: Post twitt
		Given my user
		When I write a twitt
		Then my user status should be changed
		And twitt should be appear in timeline
