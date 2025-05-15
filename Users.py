class User:    
    def __init__(self, name=None, email=None, password=None, userDataDir=None, profileName=None, cookie=None):
        self._name = name
        self._email = email
        self._password = password
        self._userDataDir = userDataDir
        self._profileName = profileName
        self._cookie = cookie
    
    def getName(self):
        return self._name
    def getEmail(self):
        return self._email
    def getPassword(self):
        return self._password
    def getUserDataDir(self):
        return self._userDataDir
    def getProfileName(self):
        return self._profileName
    def getCookie(self):
        return self._cookie
