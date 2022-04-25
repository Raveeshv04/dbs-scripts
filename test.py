import os 

class sample:
    def __init__(self, uname, passw):
        self.uname = uname
        self.passw = passw
        self.__token = ""
        self.__get_token()

    def __get_token(self):
        self.__token = self.uname + self.passw
        return self.uname + self.passw

    
if __name__ == '__main__':
    samp = sample("harsh" , "123")
    print(samp.token)
    #print(samp.get_token())
    
    