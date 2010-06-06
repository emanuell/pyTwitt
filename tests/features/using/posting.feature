Feature: Twitter use
	As a registred twitter user
	I want post twitts
	So that I can update my status and interact with friends
	
	Scenario: Post twitt
		Given my username pytwitt2 and password abc123456
		When post the twitt "Test"
		Then twitter should return True
		And my user status should be changed to "Test"
		And twitt "Test" should be last twitt
	
	Scenario: Timeline
		Given username pytwitt2 and password abc123456
		When twitt "Test2"
		And twitt "Test3"
		Then timeline should be "Test3" first
		And "Test2" should be second
		
	Scenario: Posting same twitt
		Given username pytwitt2 and password abc123456
		When post the same twitt "Test2"
		Then twitter should return False

	