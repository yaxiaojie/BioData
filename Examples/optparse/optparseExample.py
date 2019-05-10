#######################################################
# Created on: 2016-04-04
# author: H.Wang
# Update: 2016-4-4
#######################################################


from optparse import OptionParser

########################################################################
class DoSomething:
    """
    This is just a example class to show how the optparse is working
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
    
    #----------------------------------------------------------------------    
    def eat(self, food):
        """"""
        print("Eat " + food)
        return
    
    #----------------------------------------------------------------------
    def sleep(self, time):
        """"""
        print("Sleep %d"%(time))
        return        
    
    #----------------------------------------------------------------------
    def work(self, work):
        """"""
        output = "The work is %s"%(work)
        print(output)
        return  
    
    #----------------------------------------------------------------------
    def nothing2do(self):
        """"""
        print("You have nothing to do!")
        return         
    
def main(): 
    """
    Show how the main entry using class optparse to regulate the users' input.
    This function will work only when this python code is used directly, but not users 
    call the code using other python code.
    """
    # Construct the usage of class DoSomething.
    usage = "usage: %prog [options] arg"  
    parser = OptionParser(usage)  
    parser.add_option("-e", "--eat", dest="food", default="apple",
                      help="Input any food name.")  
    parser.add_option("-s", "--sleep", type="int", dest="time", default=30,
                      help="Input how many minutes you want to sleep.")  
    parser.add_option("-w", "--work",  dest="work", default="coding",
                      help="Input what kind of work you want to do.")  
    # Parse the options and args input by users.
    (options, args) = parser.parse_args()  
    # Check the correction of users input and call the fuctions of class DoSomething.
    if options.time < 20:  
        parser.error("Your sleep is too short!")
    ds = DoSomething()
    ds.eat(options.food)
    ds.sleep(options.time)
    ds.work(options.work)
 
      
if __name__ == "__main__":  
    main()  

    