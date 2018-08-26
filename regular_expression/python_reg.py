#In this program I work on some basic regular expression examples.

import re


def main():
    R =myREGexp()
    string = 'Am example word:cat and the word:cat!!'
    pattern = r'word:\w\w\w'#in Python r (means 'raw') is not strictly required but it is a good practice to write
    R.pattern_search(pattern, string)
    
    string1 = 'It was great meeting with Dr. Xyz!!'
    pattern1 = r'Dr.\s\w\w\w'
    R.pattern_search(pattern1, string1)

   #Special Characters
    string2 ="My birthday is 12/17-1988"
    pattern2 = r'\d\d\/\d\d\-\d\d\d\d'
    R.pattern_search(pattern2, string2)

    #Repaeatition

    string3= "Thiiis"
    pattern3= r"i+"
    R.pattern_search(pattern3, string3)

    #One or more white spaces:
    R.pattern_search(r'\d\s*\d\s*\d', 'xx12  3xx')#  String found, match.group() == "12  3"

    #Start of string:
    R.pattern_search(r'^b\w+', 'foobar') # String  not found, match == None
    R.pattern_search(r'^b\w+', 'bfoobar') # String  not found, match == None

    #Search just an email address
    R.pattern_search(r'\s\w+\@\w+\.\w+', 'This is my email address: apple@ball.com please use this means for communication ')
    R.pattern_search(r'[\w.-]+@[\w.-]+', 'This is my email address: apple.b@ball.com please use this means for communication ')


    #Pattern search with groups:
    R.pattern_group_search(r'([\w.-]+)@([\w.-]+)', 'This is my emali: alice-b@google.com Always use it')



    #Using findall
    R.pattern_findall(r'[\w\.-]+@[\w\.-]+', 'This is my email alice-b@google.com but hers is a.b.c@gmali.net')



    #Read file and find pattern in file. Read myEmailFile.txt
    myfile = open('myEmailFile.txt', 'r')
    R.pattern_search_in_file(r'[\w\.-]+@[\w\.-]+',myfile)


    #Substtution of pattern
    R.pattern_substitution(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', 'purple alice@google.com, and  bob@abc.com the real terminator')
class myREGexp():
    
    def __init__(self):
        pass

    def pattern_search(self,pattern,string):
        match = re.search(pattern, string)
        # If-statement if search is succeed or not
        if match:
            print ('Pattern found: '+ match.group())
        else:
            print ('Pattern did not find')

    def pattern_group_search(self,pattern,string):
        match = re.search(pattern, string)
        # If-statement if search is succeed or not
        if match:
            print ("Whole match: ",match.group())   ## 'alice-b@google.com' (the whole match)
            print ("First group: ",match.group(1))  ## 'alice-b' (the username, group 1)
            print ("Second group: ",match.group(2))  ## 'google.com' (the host, group 2)



    def pattern_findall(self,pattern,string):
        emails= re.findall(pattern, string)
        # If-statement if search is succeed or not
        if emails:
            print("Following is the list of email addresses:\n")
            for email in emails:
                print (email)

    def pattern_search_in_file(self,pattern,myfile):
        emails = re.findall(pattern, myfile.read())

        if emails:
            print("Following is the list of email addresses:\n")
            for email in emails:
                print (email)


    def pattern_substitution(self,pattern1, pattern2, string):
        newString= re.sub(pattern1,pattern2,string)
        print(string)
        print(newString)
if __name__=="__main__":
    main()
