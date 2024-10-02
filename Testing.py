import unittest
import UtilMethods

class Test(unittest.TestCase):

    def setUp(self):
        self.arrays = [[1,2,3,4,5],[10,9,8,7,6],[10,-10,20,0]]
        self.numbers = [7,2,16]

    def testingFindMinAndMaxValue(self):
        results = []
        for i in self.arrays:
            obj = UtilMethods.UtilMethods(i)
            results.append(obj.findMinAndMaxValue())
        self.assertEqual(results,[[1,5],[6,10],[-10,20]])

    def testingFindMeanValue(self):
        results = []
        for i in self.arrays:
            obj = UtilMethods.UtilMethods(i)
            results.append(obj.findMeanValue())
        self.assertEqual(results,[3.0,8.0,5.0])

    def testingFindNearestValue(self):
        results = []
        for i in range(0,3):
            obj = UtilMethods.UtilMethods(self.arrays[i])
            number = self.numbers[i]
            results.append(obj.findNearestValue(number))
        self.assertEqual(results,[5,6,20])



if __name__ == "__main__":
    unittest.main()