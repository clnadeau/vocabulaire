# -*- coding: utf-8 -*-

import sl4a
#--- androidHook looks like this: sl4a.Android()

class androidUI(object):
    """ Interface to the android system """
    def __init__(self, mapDict, androidHook):
        """ Initialize the interface between the game and android dialogs
        @mapDict: pointer to a mapping dictionnary at the game level
        @androidHook: pointer to an android system hook instance """
        self.mapDict = mapDict
        self.droid = androidHook
        
    @staticmethod
    def getMappingDict(language):
        """ Initialize a mapping dictionary
        @language: a string indicating the language ('E' or 'F') """
        event2Str = dict()
        if language == 'E':
            event2Str.update({'choose':'Choose what to do.'})
            event2Str.update({'endNoSel':'You need to make at least one selection.'})
        elif language == 'F':
            event2Str.update({'choose':'Choisissez quoi faire.'})
            event2Str.update({'endNoSel':'Vous devez faire une sélection.'})
        return event2Str
        
    def qa(self, question, answers):
        """ Asks a question to the user and provides a list of valid answers
        @question: string for the question asked
        @answers: a list of string for the valid answers """
        self.droid.dialogCreateAlert(question)
        self.droid.dialogSetItems(answers)
        self.droid.dialogShow()
        answer = self.droid.dialogGetResponse().result
        return answer['item']
    
    def message(self, message):
        """ Sends a message to the players 
        @message: message string to be sent """
        self.droid.dialogCreateAlert("", message)
        self.droid.dialogSetPositiveButtonText("OK")
        self.droid.dialogShow()
        response = self.droid.dialogGetResponse().result
        
    def qaYN(self, question, yesText="+1", noText="-1"):
        """ question user with a Yes or No answer
        @question: text for question
        @yesText: text for Yes button
        @noText: text for No button """
        self.droid.dialogCreateAlert("", question)
        self.droid.dialogSetPositiveButtonText(yesText)
        self.droid.dialogSetNegativeButtonText(noText)
        self.droid.dialogShow()
        answer = self.droid.dialogGetResponse().result
        mapFeedback = {'positive':1, 'negative':0}
        return mapFeedback.get(answer['which'],-1)
        
        
    def qa2(self, question):
        """ Asks a question to the user
        @question: string for the question asked """
        answer = self.droid.dialogGetInput(question, "").result
        return answer


