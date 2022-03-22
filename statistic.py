import re

class Statistic:

   def __init__(self, text, cmd, oldword, newword):
      self.text = text
      self.split_text = text
      self.cmd = cmd
      self.word_list = []
      self.new_word = newword
      self.old_word = oldword

   def separator(self):
      punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      for ele in self.split_text:
         if ele in punc:
            self.split_text = self.split_text.replace(ele, ' ')
      self.split_text = re.split('\n|\t| ', self.split_text)

      while('' in self.split_text):
         self.split_text.remove('')

   def stringList(self):
      for i in self.split_text:
         if i not in self.word_list:
            self.word_list.append(i)

   def statistic(self):
      self.separator()
      self.stringList()
      if self.cmd == 'frequency':
         result = self.calcFrequency()
      elif self.cmd == 'replace':
         result = self.replaceWords()
      return result

   def calcFrequency(self):
      word_freq = []
      for i in range(0, len(self.word_list)):
         word_freq.append(self.split_text.count(self.word_list[i]))
      return word_freq

   def replaceWords(self):
      new_text = self.text.replace(self.old_word, self.new_word)
      return new_text
   
   def getWordList(self):
      return self.word_list

   def getStatistic(self):
      return self.statistic()

   def getText(self):
      return self.text
