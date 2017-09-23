#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import os
import sl4a
from androidUI import androidUI
from random import seed, choice

class readWords(object):
    """ deals with the game loop """
    def __init__(self, language):
        """ runs the game loop
        @language: language used by the game ('F' or 'E') """
        #--- kick off UI
        mapUI = androidUI.getMappingDict(language)
        hookUI = sl4a.Android()
        UI = androidUI(mapUI, hookUI)
        #--- choose words
        filenames = self.get_files()
        self.filename = filenames[UI.qa("",filenames)]
        self.words = self.get_words(self.filename)
        #--- choose nb of repetitions
        rep = [10,20,50,100]
        self.rep = rep[UI.qa("",rep)]
        #--- start game loop
        seed()
        score = 0
        for i in range(self.rep):
            #UI.message(choice(self.words))
            score += UI.qaYN(choice(self.words))
        UI.message(str(score)+" / "+str(self.rep))
        
    def get_files(self):
        """ retrieves a list of files to choose from """
        word_file = os.listdir(os.path.join(os.path.dirname(__file__),'data'))
        filenames = [os.path.splitext(x) for x in word_file]
        filenames = [name for name,ext in filenames if ext == ".txt"]
        return filenames
        
    def get_words(self,filename):
        """ retrieves a list of words from a file
        @filename: name of the file to extract w/o extension """
        with open(os.path.join(os.path.dirname(__file__),'data/'+filename+'.txt'),'r') as f:
            word_list = f.readlines()
            word_list = [x.strip() for x in word_list]
        return word_list
