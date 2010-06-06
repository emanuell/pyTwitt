Feature: Twitter login
	As a registred user
	I want use my twitter account
	So that I can get personal data
	
	Scenario: Auth
		Given username pytwitt2
		And my secret password abc123456
		When I request for access
		Then my user pytwitt2 object should be returned

	Scenario: User information
		Given my user object
		Then my username should be pytwitt2
		And my fullname should be Emanuell Faustino
		And my website should be http://twitter.com/emanuell
		And my bio should be Nothing yet
		And my location should be Recife