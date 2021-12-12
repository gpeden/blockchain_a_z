#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:28:32 2021

@author: gpeden
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Create a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

# Part 2 - Mining our Blockchain