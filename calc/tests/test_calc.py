import unittest
import json
from flask import request, jsonify
from calc import app

app.testing = True

# TODO: Extend these component tests for the calc view
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):
    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "8")

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/div?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "DivisionByZeroError")
    
    
    #test for line 47-54 calculator.py
    def test_sub1(self):
        tested_app = app.test_client()
        
        #Subtracting two positive values: m>n
        reply = tested_app.get("/calc/sub?m=3&n=1").get_json()
        self.assertEqual(reply["result"], "2")
        
        #Subtracting two positive values: m<n
        reply = tested_app.get("/calc/sub?m=1&n=3").get_json()
        self.assertEqual(reply["result"], "-2")

        #Subtracting two negative values: m>n
        reply = tested_app.get("/calc/sub?m=-1&n=-2").get_json()
        self.assertEqual(reply["result"], "1")        

        #Subtracting two negative values: m<n
        reply = tested_app.get("/calc/sub?m=-2&n=-1").get_json()
        self.assertEqual(reply["result"], "-1") 

        #Subtracting a negative value from a positive one
        reply = tested_app.get("/calc/sub?m=2&n=-1").get_json()
        self.assertEqual(reply["result"], "3") 

        #Subtracting a positive value from a negative one
        reply = tested_app.get("/calc/sub?m=-2&n=1").get_json()
        self.assertEqual(reply["result"], "-3") 

    #test for line 34-44 calculator.py
    def test_mul1(self):
        tested_app = app.test_client()

        # Positive result
        reply = tested_app.get("/calc/mul?m=3&n=2").get_json()
        self.assertEqual(reply["result"], "6")
        
        reply = tested_app.get("/calc/mul?m=-3&n=-2").get_json()
        self.assertEqual(reply["result"], "6")

        # Zero result
        # 0 on the right
        reply = tested_app.get("/calc/mul?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "0")

        # 0 on the left
        reply = tested_app.get("/calc/mul?m=0&n=3").get_json()
        self.assertEqual(reply["result"], "0")

        # Negative result
        reply = tested_app.get("/calc/mul?m=-5&n=3").get_json()
        self.assertEqual(reply["result"], "-15")

        reply = tested_app.get("/calc/mul?m=5&n=-3").get_json()
        self.assertEqual(reply["result"], "-15")
