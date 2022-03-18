import sys
import os
import re
from statistic import Statistic

def printResult(stat, result, words, outfile):
   if stat == "frequency":
      for i in range(0, len(words)):
         print("\"{}\" frequency is {}".format(words[i], result[i]))
         with open(outfile, 'a') as ofile:
            print("\"{}\" frequency is {}".format(words[i], result[i]), file = ofile)

def main(argv):
   infile = ''
   outfile = ''
   stat = ''

   try:
      infile = argv[1]
      outfile = argv[2]
      stat = argv[3]
   except:
      print("Arguments Error")
      print("python run.y <INFILE> <OUTFILE> <STATISTIC>")
      sys.exit(2)

   with open(infile, 'r') as file:
      str = file.read()

   statistic = Statistic(str, stat)
   result = statistic.getStatistic()
   word_list = statistic.getWordList()

   printResult(stat, result, word_list, outfile)

if __name__=="__main__":
   main(sys.argv)
