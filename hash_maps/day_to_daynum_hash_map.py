"""
    Built in python dictionary is used for hash_map problems
   """

def map_day_to_daynum():
    """
    In this problem each day is mapped with a day number. 
    Sunday is considered as a first day.
    """

    day_dayNum = {"Sunday":1, "Monday":2, "Tuesday":3, "Wednesday":4,
            "Thursday":5, "Friday":6, "Saturday":7}

    
    #Display method 1:
    print (day_dayNum)

    #Display method 2
    
    for key, value in day_dayNum.items():
        print (key, value)

    #Display method 3

    print (day_dayNum["Sunday"])

    #Add elements:
    day_dayNum["NewDay"]="Noday"
    print (day_dayNum)

    #Remove elements:
    del day_dayNum["NewDay"]
    print (day_dayNum)


    #Remove with exception:

    try:
        del day_dayNum["Monday"]
    except KeyError as ex:
        print("No such key")
    print (day_dayNum)

    try:
        del day_dayNum["Monday"]
    except KeyError as ex:
        print("No such key")
    print (day_dayNum)


map_day_to_daynum()
    
