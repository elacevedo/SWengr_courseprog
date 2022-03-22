import sys
import os
import re
from statistic import Statistic

def printResult(cmd, text, outfile, old_word, new_word):
   if cmd == "frequency":
      statistic = Statistic(text, cmd, old_word, new_word)
      word_list = statistic.getWordList()
      result = statistic.getStatistic()
      print(statistic.getText())
      with open(outfile, 'a') as ofile:
         print(text, file = ofile)
      for i in range(0, len(word_list)):
         print("\"{}\" frequency is {}".format(word_list[i], result[i]))
         with open(outfile, 'a') as ofile:
            print("\"{}\" frequency is {}".format(word_list[i], result[i]), file = ofile)
   elif cmd == "replace":
      statistic = Statistic(text, cmd, old_word, new_word)
      result = statistic.getStatistic()
      print(statistic.getText())
      print(result)
      with open(outfile, 'a') as ofile:
         print(text, file = ofile)
         print(result, file = ofile)

def main(argv):
   infile = ''
   outfile = ''
   cmd = ''
   new_word = ''
   old_word = ''

   try:
      infile = argv[1]
      outfile = argv[2]
      cmd = argv[3]
      if cmd == 'replace':
         old_word = argv[4]
         new_word = argv[5]
   except:
      print("Arguments Error")
      print("python run.y <INFILE> <OUTFILE> <STATISTIC>")
      sys.exit(2)

   with open(infile, 'r') as file:
      text = file.read()

   printResult(cmd, text, outfile, old_word, new_word)

if __name__=="__main__":
   main(sys.argv)
