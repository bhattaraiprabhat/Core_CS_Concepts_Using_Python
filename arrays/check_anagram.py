#This example shows how to test if a string is anagram of another string. 
#Anagram is defined in Oxford dictionary as:
#"A word or phrase that is made by arranging the letters of another word or phrase in a different order
#An anagram of “Elvis” is “lives.”


#There are two methods to check if the strings are anagrams. 
def main():

    A = Anagram()

    A.anagram_with_python_library("elvis","lives")
    A.anagram_without_python_library("elvis","lives")

    A.anagram_with_python_library("Listen","silent")
    A.anagram_without_python_library("Listen","silent")


    #Based on need you may need to change upper case to lower case (or vice
    #versa) for both strings. 
class Anagram():

    def __init__(self):
        pass

    def anagram_with_python_library(self, string1, string2):
        if sorted(string1.lower())==sorted(string2.lower()):
            print(string1 +" and "+ string2 +" ARE anagrams.")
        else:
            print(string1 +" and "+ string2 +" are NOT anagrams.")


    def anagram_without_python_library(self, string1, string2):

        result = [i for i in string1.lower() if i not in string2.lower()] + [i for i in string2.lower() if i not in string1.lower()]
        
        if not result:
            print(string1 +" and "+ string2 +" ARE anagrams.")
        else:
            print(string1 +" and "+ string2 +" are NOT anagrams.")



if __name__=="__main__":
    main()
