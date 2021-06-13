import re

class analysedText(object):
    """
    A utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods:
    
    1. Constructor - Takes argument 'text', makes it lower case and removes all punctuation.
        Assuming only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?).
        Argument is stored in "fmtText" 
        
    2.freqAll - returns a dictionary of all unique words in the text along with the number of their occurences
    
    3.freqOf - returns the frequency of the word passed in argument. 
    """
# constructor
    def __init__ (self, text):
        temp = re.split('[.!,?]', text.lower());
        fmtText = ''
        fmtText = fmtText.join(temp);
        self.fmtText = fmtText;
    
        
# method
    def freqAll(self):
        temp = self.fmtText;
        tempList = temp.split();
        tempSet = set(tempList);
        i = 0;
        dict = {};
        for element in tempSet:
            for word in tempList:
                if word == element:
                    i = i + 1;
            dict[element] = i;
            i = 0;
        return dict;

# method
    def freqOf(self,word):
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
