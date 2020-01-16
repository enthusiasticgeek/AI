#!/usr/bin/env python3

from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

#define math operations
add = 'add'
mul = 'mul'

#define commutative/associative
fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

#define variables
a, b = var('a'), var('b')

#Original pattern (5+a)*b
Original_pattern = (mul, (add, 5, a), b)

#Two Expressions
exp1 = (mul, (add,5,3), 4)
exp2 = (mul, 2, (add, 5, 1))
exp3 = (add, 5, (mul, 8, 1))  #(8*1+5)

#Output
print(run(0, (a,b), eq(Original_pattern, exp1)))
print(run(0, (a,b), eq(Original_pattern, exp2)))
print(run(0, (a,b), eq(Original_pattern, exp3)))
