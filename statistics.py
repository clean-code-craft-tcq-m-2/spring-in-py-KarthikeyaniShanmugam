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
