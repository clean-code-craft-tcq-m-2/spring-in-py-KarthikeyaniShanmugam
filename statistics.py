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

# def calculateStats(numbers):
#   output = {}
#   if len(numbers):
#     minNum = float('-inf')
#     maxNum = float('inf')
#     sumNum = 0
#     for num in numbers:
#       sumNum = sumNum + num
#       if num < minNum:
#         minNum = num
#       if num > maxNum:
#         maxNum = num
#     avgNum = sumNum/len(numbers)
    
    
#     output["avg"] = avgNum
#     output["min"] = minNum
#     output["max"] = maxNum  
#   else:    
#     output["avg"] = output["min"] = output["max"] = nan

  return output
