
class StringUtility:

  def __init__ (self, myString):
    self.myString = myString #babble

  def __str__(self):
    return self.myString

  def vowels(self):
    vowelString = "aeiou"
    count = 0

    for char in self.myString: 
      if char == "a" or char =="e" or char == "i"or char =="o" or char == "u":
        count += 1

    if count >= 5:
      return "many"
    else:
      return str(count)

  def bothEnds(self):
    stringSlice = self.myString[0:2] + self.myString[-2:]
    if len(stringSlice) <= 2 :
      return ""
    else:
      return(stringSlice) 

#babble
  def fixStart(self):
    if len(self.myString) <= 1 :
      return self.myString
    self.myString = list(self.myString)
    firstChar = self.myString[0]
    restOfChar = self.myString[1:]

    for i in range(len(restOfChar)):
      if self.myString[i + 1] == firstChar:
        self.myString[i + 1] = '*'
    self.myString =  "".join(self.myString)
    return self.myString

  def asciiSum(self):
    sum = 0 
    for char in self.myString:
      num = ord (char)
      sum += num
    return sum 

  def cipher(self):
    encodedString = ""
    stringLen = len(self.myString)
    for char in self.myString:
      num = ord (char)
      if num == 122 or num == 90: 
        asciiValue = num - 25

      asciiValue = num + stringLen 
      nextChar = chr(asciiValue)
      encodedString += nextChar
    return encodedString

  
      
  

    

  
