#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(4)]

    half_1 = halfAdder(a, b, s[1], s[2]) # (2)
    half_2 = halfAdder(c, s[1], soma, s[3]) # (3)

    @always_comb
    def comb():
        #soma.next = (a ^ b) ^ c
        #carry.next = ((a ^ b) & c) | (a & b)
        carry.next = s[2] | s[3] # (4)

    return instances()


@block
def adder2bits(x, y, soma, carry):
    vaiUm = Signal(bool(0))
   
    half = halfAdder(x[0], y[0], soma[0], vaiUm)
    full = fullAdder(x[1], y[1], vaiUm, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
