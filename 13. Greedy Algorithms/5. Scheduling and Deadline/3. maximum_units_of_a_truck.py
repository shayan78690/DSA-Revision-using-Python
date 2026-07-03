class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        total = 0
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            
            take = min(boxes, truckSize)
            total += take * units
            truckSize -= take
        return total
        




class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        total = 0
        for box, unit in boxTypes:
            if truckSize == 0:
                break
            if box <= truckSize:
                total += (box*unit)
                truckSize -= box
            else:
                total += (truckSize*unit)
                truckSize -= truckSize
        return total
        
