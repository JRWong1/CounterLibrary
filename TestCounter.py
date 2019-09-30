import unittest
from Counter import Counter

class TestCounter(unittest.TestCase):

    def setUp(self):
        #Default Constructor Counter
        self.defaultCounter = Counter()

    def test_constructor(self):
        c = Counter(32, 10, 61, True)
        expected = [8, 10, 1, True]
        cValues = [c.getHour(), c.getMinute(), c.getSecond(), c.getFormat()]
        self.assertEqual(cValues, expected)
        
    def test_display2Digits(self):
        c = Counter(12, 10, 15, True)
        expected = "12:10:15 PM"
        self.assertEqual(c.displayCounter(), expected)
    def test_display1Digit(self):
        c = Counter(1, 2, 3, True)
        expected = "01:02:03 AM"
        self.assertEqual(c.displayCounter(), expected)

    def test_displayMilitary(self):
        c = Counter(23, 1, 15, False)
        expected = "23:01:15"
        self.assertEqual(c.displayCounter(), expected)

    #Test Second Changes

    def test_incrementSecond(self):
        self.defaultCounter.incrementSecond()
        expected = 1
        self.assertEqual(self.defaultCounter.getSecond(), expected)
    def test_incrementSecondRollover(self):
        for i in range(0, 60):
            self.defaultCounter.incrementSecond()
        expected = 0
        self.assertEqual(self.defaultCounter.getSecond(), expected)
    def test_decrementSecond(self):
        c = Counter(12, 10, 15, True)
        c.decrementSecond()
        expected = 14
        self.assertEqual(c.getSecond(), expected)
    def test_decrementSecondRollunder(self):
        self.defaultCounter.decrementSecond()
        expected = 59
        self.assertEqual(self.defaultCounter.getSecond(), expected)




    #Test Hour Changes

    def test_incrementHour(self):
        self.defaultCounter.incrementHour()
        expected = 1
        self.assertEqual(self.defaultCounter.getHour(), expected)
    def test_incrementHourRollover(self):
        for i in range(0, 24):
            self.defaultCounter.incrementHour()
        expected = 0
        self.assertEqual(self.defaultCounter.getHour(), expected)
    def test_decrementHour(self):
        c = Counter(12, 10, 15, True)
        c.decrementHour()
        expected = 11
        self.assertEqual(c.getHour(), expected)
    def test_decrementHourRollunder(self):
        self.defaultCounter.decrementHour()
        expected = 23
        self.assertEqual(self.defaultCounter.getHour(), expected)


    #Test Minute Changes

    def test_incrementMinute(self):
        self.defaultCounter.incrementMinute()
        expected = 1
        self.assertEqual(self.defaultCounter.getMinute(), expected)
    def test_incrementMinuteRollover(self):
        for i in range(0, 60):
            self.defaultCounter.incrementMinute()
        expected = 0
        self.assertEqual(self.defaultCounter.getMinute(), expected)
    def test_decrementMinute(self):
        c = Counter(12, 10, 15, True)
        c.decrementMinute()
        expected = 9
        self.assertEqual(c.getMinute(), expected)
    def test_decrementMinuteRollunder(self):
        self.defaultCounter.decrementMinute()
        expected = 59
        self.assertEqual(self.defaultCounter.getMinute(), expected)



    #Test Full Day Roll Under / Over
        
    def test_dayRollunder(self):
        self.defaultCounter.decrementSecond()
        expected = [23, 59, 59]
        cValues = [self.defaultCounter.getHour(), self.defaultCounter.getMinute(), self.defaultCounter.getSecond()]
        self.assertEqual(cValues, expected)

    def test_dayRollover(self):
        c = Counter(23, 59, 59, True)
        c.incrementSecond()
        expected = [0, 0, 0]
        cValues = [c.getHour(), c.getMinute(), c.getSecond()]
        self.assertEqual(cValues, expected)

    


if __name__ == "__main__":
    unittest.main()
