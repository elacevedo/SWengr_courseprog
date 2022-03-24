import sys
import os
import re
from statistic import Statistic

def getResult(command, cmd, old_word, new_word):
   command.setReplacementWords(old_word, new_word)
   command.setCommand(cmd)
   result = command.getStatistic()
   word_list = command.getWordList()
   return result, word_list

def printResult(command, cmd, text, outfile, old_word, new_word):
   if cmd == "frequency":
      result, word_list = getResult(command, cmd, old_word, new_word)
      print(text)
      with open(outfile, 'a') as ofile:
         print(text, file = ofile)
      for i in range(0, len(word_list)):
         print("\"{}\" frequency is {}".format(word_list[i], result[i]))
         with open(outfile, 'a') as ofile:
            print("\"{}\" frequency is {}".format(word_list[i], result[i]), file = ofile)
   elif cmd == "replace":
      result = getResult(command, cmd, old_word, new_word)[0]
      print(text)
      print(result)
      with open(outfile, 'a') as ofile:
         print(text, file = ofile)
         print(result, file = ofile)

def main(argv):
   infile = ''    #input file path
   outfile = ''   #output file path
   cmd = ''       #command to be performed(frequency, replace...)
   new_word = ''  #new word to replace old word for replace command
   old_word = ''  #old word to be replaced by new word for replace command

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
      text = file.read()           #string read from file

   command = Statistic(text)       #class object
   getResult(command, cmd, old_word, new_word)
   printResult(command, cmd, text, outfile, old_word, new_word)

if __name__=="__main__":
   main(sys.argv)
