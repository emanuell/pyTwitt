#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append('/Users/emanuellfaustino/Documents/Projects/pytwitt')

from lettuce import *
from pytwitt.math import Calculadora

@before.all
def init():
	world.calc = Calculadora()


@step('Given two numbers (\d+) and (\d+)')
def two_numbers(step, n1, n2):
	world.n1 = int(n1)
	world.n2 = int(n2)
	
@step('plus them')
def plus_them(step):
	world.result = world.calc.add(world.n1, world.n2)
	
@step('Then the result should (\d+)')
def the_result_should_be_4(step, resultado):
	assert int(resultado) == world.result