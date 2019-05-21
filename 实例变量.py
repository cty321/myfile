#!/bin/bash/env python

class Shili:
    a = 0
    def __init__(self):
        Shili.a += 1
    def __del__(self):
        Shili.a -= 1

