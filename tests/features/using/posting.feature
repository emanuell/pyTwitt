Feature: Twitter use
	As a registred twitter user
	I want post twitts
	So that I can update my status and interact with friends
	
	Scenario: Post tweet
		Given my username pytwitt2 and password abc123456
		When post the tweet "Test"
		Then twitter should return True
		And my user status should be changed to "Test"
		And twitt "Test" should be last tweet
	
	Scenario: Timeline
		Given username pytwitt2 and password abc123456
		When tweet "Test2"
		And tweet "Test3"
		Then timeline should be "Test3" first
		And "Test2" should be second
		
	Scenario: Posting same tweet
		Given username pytwitt2 and password abc123456
		When post the same tweet "Test2"
		Then twitter should return False

	