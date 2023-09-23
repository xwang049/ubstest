from typing import Dict, List
def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  # Fill in your solution here and return the correct output based on the given input
  result = {}
  # print('primeKeysInClasses', primeKeysInClasses)
  for key in statements:
    value = findTargetInSea(key, classes)
    result[key] = value
  # print(123)
  # print(result)
  return result

# The most important function
def findTargetInSea(search, Sea):
  target = [""]
  searchToList = search.split('.')
  # print("searchToList", searchToList)
  lenOfSearch = len(searchToList)
  i = 1
  # todo: the following line needs to be modified accordingly when the 
  while i <= lenOfSearch - 1:
    # level start with 0
    level = i - 1
    targetKey = searchToList[i-1]
    if findKeysInClasses(targetKey,Sea,level)[0]:
    # if searchToList[i-1] in primeKeysInClasses:
      keysInClasses = findKeysInClasses(targetKey,Sea,level)[1]
      
      # print('keysInClasses',keysInClasses)
      if i == lenOfSearch - 1:
        # case 1
        if searchToList[lenOfSearch - 1] == '':
          resultBeforeSorted = keysInClasses
        # case 2
        else:
           resultBeforeSorted = [x for x in keysInClasses if x.startswith(searchToList[i])]   
        # print('resultBeforeSorted', resultBeforeSorted)
        if resultBeforeSorted == []:
          resultBeforeSorted = [""]
        target = findSorted_Most5Item(resultBeforeSorted)
      i += 1
    else:
      return target   
  return target

# return a list 
def findKeysInClasses(targetKey,Sea,level):
  flag = False
  keysInClasses = [""]
  if level == 0:
    primeKeysInClasses = []
    for key in Sea:
      primeKeysInClasses.extend(key)
    if targetKey in primeKeysInClasses:
      flag = True
      keysInClasses = Sea[primeKeysInClasses.index(targetKey)][targetKey]
    if keysInClasses == "":
      keysInClasses = [""]
  return [flag,keysInClasses]
  
# return most 5
def findSorted_Most5Item(resultBeforeSorted):
  resultAfterSorted = sorted(resultBeforeSorted)
  lenOfResultAfterSorted = len(resultAfterSorted)
  if lenOfResultAfterSorted > 5:
    # print('resultAfterSorted[:5]',resultAfterSorted[:5])
    return resultAfterSorted[:5]
  else:
    if resultAfterSorted == []:
      return [""]
    return resultAfterSorted
