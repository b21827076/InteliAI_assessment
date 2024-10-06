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

        result = [minimumNumber, maximumNumber]
        return result


    def findMeanValue(self):
        temp = 0

        for i in self.array:
            temp += i

        meanValue = round(temp/len(self.array),1)
        result = meanValue
        return result

    def findNearestValue(self,number):
        nearestValue = self.array[0]
        distance = abs(number - nearestValue)

        for i in self.array:
            newDistance = abs(number - i)
            if(distance > newDistance):
                distance = newDistance
                nearestValue = i

        result = nearestValue
        return result

