# Imports
import datetime

# Set the color theme
class bcolors:
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Create the class Logger
class Logger:
    # Init with a name and a path for the logs
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def getTime(self):
        return datetime.datetime.now()
    
    # Get the log string
    def info(self, head, message):
        string = f"{self.getTime()} [{bcolors.INFO + head + bcolors.ENDC}] {message}"
        self.writeToLog(string + "\n")
        print(string)

    def success(self, head, message):
        string = f"{self.getTime()} [{bcolors.SUCCESS + head + bcolors.ENDC}] {message}"
        self.writeToLog(string + "\n")
        print(string)

    def warning(self, head, message):
        string = f"{self.getTime()} [{bcolors.WARNING + head + bcolors.ENDC}] {message}"
        self.writeToLog(string + "\n")
        print(string)

    def error(self, head, message):
        string = f"{self.getTime()} [{bcolors.ERROR + head + bcolors.ENDC}] {message}"
        self.writeToLog(string + "\n")
        print(string)

    def replace_all(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    # 
    def writeToLog(self, string):
        # Replace the color theme 
        d = { "[94m": "", "[92m": "", "[93m": "", "[91m": "", "[0m": "", "[91m": "", "[94m": ""}
        new = self.replace_all(string, d)
        
        # Write it to file
        f = open(f"{self.path}{self.name}.log", "a")
        f.write(new)
        f.close()