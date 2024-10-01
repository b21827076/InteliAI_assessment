class UtilMethods:
    def __init__(self,array):
        self.array = array

    def findMinAndMaxValue(self):
        minimumNumber = self.array[0]
        maximumNumber = self.array[0]

        for i in self.array:
            if i > maximumNumber:
                maximumNumber = i
            elif i < minimumNumber:
                minimumNumber = i

        result = "Minimum number in array: {0} \nMaximum number in array: {1}".format(minimumNumber, maximumNumber)
        return result


    def findMeanValue(self):
        temp = 0

        for i in self.array:
            temp += i

        meanValue = format(temp/len(self.array),".2f")
        result = "Mean value of array: {0}".format(meanValue)
        return result

    def findNearestValue(self,number):
        nearestValue = self.array[0]
        distance = abs(number - nearestValue)

        for i in self.array:
            newDistance = abs(number - i)
            if(distance > newDistance):
                distance = newDistance
                nearestValue = i

        result = "The closest value in array to the given number: {0}".format(nearestValue)
        return result

"""
p1 = UtilMethods([10,60,240,60,130,70])
print(p1.findMinAndMaxValue())
print(p1.findMeanValue())
print(p1.findNearestValue(200))
"""