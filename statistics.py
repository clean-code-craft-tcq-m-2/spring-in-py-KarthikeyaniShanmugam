
from cmath import nan

def calculateStats(numbers):
  output = {}
  if len(numbers):
    output["avg"] = sum(numbers)/len(numbers)
    output["min"] = min(numbers)
    output["max"] = max(numbers)   
  else:    
    output["avg"] = output["min"] = output["max"] = nan

  return output


class EmailAlert():
  emailSent = False
class LEDAlert():
  ledGlows = False
class StatsAlerter():
  def __init__(self,maxThreshold, setList):
      self.maxThreshold = maxThreshold
      self.setList = setList
  def checkAndAlert(self,values):
    computedStats = calculateStats(values)
    if computedStats["max"] > self.maxThreshold :
      self.setList[0].emailSent = True
      self.setList[1].ledGlows = True
