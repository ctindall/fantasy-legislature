#!/usr/bin/env python3

import unittest
import json

from ButtonApiModels import Button, Theater
import ButtonApiUtility as Utility

class TestButton(unittest.TestCase):
    
    def testInit(self):
        with self.assertRaises(TypeError):
            aButton = Button()
        
        aButton = Button(10,11)
        self.assertIsInstance(aButton, Button)

        self.assertEqual(aButton.row, 10)
        self.assertEqual(aButton.seat, 11)
        self.assertEqual(aButton.on, False)

    def testStringReprestation(self):
        aButton = Button(10,11)
        self.assertEqual(str(aButton), "button is OFF @ row: 10, seat: 11")
        aButton.turnOn()
        self.assertEqual(str(aButton), "button is ON @ row: 10, seat: 11")

    def testTurnOnAndOff(self):
        aButton = Button(10,11)

        aButton.turnOn()
        self.assertEqual(aButton.on, True)

        aButton.turnOff()
        self.assertEqual(aButton.on, False)

    def testToggle(self):
        aButton = Button(10,11)

        aButton.toggle()
        self.assertEqual(aButton.on, True)

        aButton.toggle()
        self.assertEqual(aButton.on, False)

    def testUpdate(self):
        aButton = Button(10,11)

        aButton.update(True)
        self.assertEqual(aButton.on, True)

        aButton.update(False)
        self.assertEqual(aButton.on, False)
        
    def testToJson(self):
        aButton = Button(10,11)

        aButton.turnOn()
        self.assertEqual(aButton.tojson(), '{"on": true, "row": 10, "seat": 11}')

        aButton.turnOff()
        self.assertEqual(aButton.tojson(), '{"on": false, "row": 10, "seat": 11}')
        
class TestTheater(unittest.TestCase):

    def testInit(self):
        #we should raise an error when initialized without rows and buttons_per_row
        with self.assertRaises(TypeError):
            aTheater = Theater()
        
        aTheater = Theater(20,10)
        self.assertIsInstance(aTheater, Theater)

        for button in aTheater.buttons:
            self.assertEqual(button.on, False)

    def testGetButton(self):
        aTheater = Theater(20,10)
        self.assertEqual(aTheater.getButton(15,9).row, 15)
        self.assertEqual(aTheater.getButton(15,9).seat, 9)

        with self.assertRaises(IndexError):
            aTheater.getButton(100, 100)

    def testTurnOnAndOff(self):
        aTheater = Theater(20,10)
        aTheater.turnOn(5, 6)
        self.assertEqual(aTheater.getButton(5, 6).on, True)

        aTheater.turnOff(5, 6)
        self.assertEqual(aTheater.getButton(5, 6).on, False)
            
    def testToggle(self):
        aTheater = Theater(20,10)
        aTheater.toggle(5, 6)
        self.assertEqual(aTheater.getButton(5, 6).on, True)

        aTheater.toggle(5, 6)
        self.assertEqual(aTheater.getButton(5, 6).on, False)

    def testUpdate(self):
        aTheater = Theater(20,10)
        aTheater.update(5, 6, True)
        self.assertEqual(aTheater.getButton(5, 6).on, True)

        aTheater.update(5, 6, False)
        self.assertEqual(aTheater.getButton(5, 6).on, False)

    def testToJson(self):
        aTheater = Theater(20,10)
        theJson = aTheater.tojson()
        
        self.assertIsInstance(theJson, str)

        theObj = json.loads(theJson)
        
        self.assertIsInstance(theObj, list)

    def testCoerceToBool(self):
        
        self.assertEqual(Utility.coerceToBool(False), False)
        self.assertEqual(Utility.coerceToBool(True), True)

        self.assertEqual(Utility.coerceToBool("false"), False)
        self.assertEqual(Utility.coerceToBool("true"), True)

        self.assertEqual(Utility.coerceToBool("0"), False)
        self.assertEqual(Utility.coerceToBool("1"), True)

        with self.assertRaises(ValueError):
            Utility.coerceToBool("TRUE")
            
        with self.assertRaises(ValueError):
            Utility.coerceToBool("FALSE")
            
        with self.assertRaises(ValueError):
            Utility.coerceToBool("True")
            
        with self.assertRaises(ValueError):
            Utility.coerceToBool("False")
            
        with self.assertRaises(ValueError):
            Utility.coerceToBool("Sean Bean")

        
if (__name__ == '__main__'):
    unittest.main()
