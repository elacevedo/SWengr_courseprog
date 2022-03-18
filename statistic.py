import re

class Statistic:

   def __init__(self, str, stat):
      self.string = str
      self.str = str
      self.stat = stat
      self.str_list = []

   def separator(self):
      punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      for ele in self.str:
         if ele in punc:
            self.str = self.str.replace(ele, ' ')
      self.str = re.split('\n|\t| ', self.str)

      while('' in self.str):
         self.str.remove('')

   def stringList(self):
      for i in self.str:
         if i not in self.str_list:
            self.str_list.append(i)

   def statistic(self):
      self.separator()
      self.stringList()
      if self.stat == 'frequency':
         result = self.calcFrequency()
      return result

   def calcFrequency(self):
      word_freq = []
      for i in range(0, len(self.str_list)):
         word_freq.append(self.str.count(self.str_list[i]))
      return word_freq

   def getWordList(self):
      return self.str_list

   def getStatistic(self):
      return self.statistic()
