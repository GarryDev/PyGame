class Bot:

    def __init__(self):
        self.__func_array = []

    def Decorator(self, f):
        self.__func_array.append(f)

    def addtofuncs(self, f):
        self.__func_array.append(f)

    def callYourFuncs(self):
        for f in self.__func_array:
            f()

bot = Bot()

#@bot.Decorator
def greeter():
    print("Hello")


#@bot.Decorator
def bye():
    print("Bye!")

bot.addtofuncs(lambda x : "Hello")
bot.addtofuncs(bye)

bot.callYourFuncs()