#!/usr/bin/env python
# encoding: utf-8

Feature: Calculadora
	In order to calculate
	I can calculate more easy
	
	Scenario: Plus
		Given two numbers 2 and 2
		When plus them
		Then the result should 4
		
	Scenario: Minus
		Given two numbers 5 and 3
		When minus them
		Then the result should be 2