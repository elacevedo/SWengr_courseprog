import re
import unittest

class Statistic:

   def __init__(self, text):
      self.text = text        #the original text string
      self.split_text = text  #the text that will be split into individual words
      self.cmd = ''          #the cmd specified by the user to be worked on the text
      self.word_list = []     #list of unique words in the text
      self.new_word = ''      #string that will replace the old string
      self.old_word = ''      #string to be replaced by the new string

   #sets the strings used in replaceWords
   #oldword: old string that will be replaced the new string
   #newword: new string that will replace the old string
   #returns nothing
   def setReplacementWords(self, oldword, newword):
      self.new_word = newword
      self.old_word = oldword

   #sets the specified command
   #command: string that specifies the command given by user
   #returns nothing
   def setCommand(self, command):
      self.cmd = command

   #removes puncuation from given text string
   #returns nothing
   def removePuncuation(self):
      punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      for ele in self.split_text:
         if ele in punc:
            self.split_text = self.split_text.replace(ele, ' ')

   #removes any empty elements that occur when the text string is split
   #returns nothing
   def removeEmpty(self):
      while('' in self.split_text):
         self.split_text.remove('')

   #separates the original text string into a list that contains every word
   #returns nothing
   def separator(self):
      self.removePuncuation()
      self.split_text = re.split('\n|\t| ', self.text)
            self.removeEmpty()

   #puts every unique string into a list
   #returns nothing
   def stringList(self):
      for i in self.split_text:
         if i not in self.word_list:
            self.word_list.append(i)

   def statistic(self):
      if self.cmd == 'frequency':
         self.separator()
         self.stringList()
         result = self.calcFrequency()
      elif self.cmd == 'replace':
         result = self.replaceWords()
      return result

   #counts the number of times a word appears in the given text
   #returns list with word count
   def calcFrequency(self):
      word_freq = []
      for i in range(0, len(self.word_list)):
         word_freq.append(self.split_text.count(self.word_list[i]))
      return word_freq

   #replaces the old word with the new word
   #returns changed text
   def replaceWords(self):
      new_text = self.text.replace(self.old_word, self.new_word)
      return new_text

   def getWordList(self):
      return self.word_list

   def getStatistic(self):
      return self.statistic()

   def getText(self):
      return self.text

class TestStatistic(unittest.TestCase):
   def setUp(self):
      self.text = "New word\nOld word\nNew world\nOld world\n"
      self.command = Statistic(self.text)

   def test_separator(self):
      self.command.setCommand('frequency')
      result = self.command.getStatistic()
      word_list = self.command.getWordList()
      self.assertEqual(word_list, ['New', 'word', 'Old', 'world'])

   def test_frequency(self):
      self.command.setCommand('frequency')
      result = self.command.getStatistic()
      word_list = self.command.getWordList()
      self.assertEqual(result, [2, 2, 2, 2])

   def test_replace(self):
      self.command.setCommand('replace')
      self.command.setReplacementWords('Old', 'New')
      result = self.command.getStatistic()
      self.assertEqual(result, "New word\nNew word\nNew world\nNew world\n")
