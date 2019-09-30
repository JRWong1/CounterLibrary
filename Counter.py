class Counter:


    def __init__(self, hours: int=None, minutes: int=None, seconds: int=None, standardTime: bool=None):
        # The default constructor sets the time to 12:00:00 (hrs, mins, secs) in standard time and 00:00:00 in military time
        # Takes the absolute value of negative numbers and takes the modulus of larger integers

        if standardTime is None:
            self.__standardTime = True
        else:
            self.__standardTime = standardTime
            
        if hours is None:
            self.__hours = 0
        else:
            self.__hours = abs(hours) % 24
            
        if minutes is None:
            self.__minutes = 0
        else:
            self.__minutes = abs(minutes) % 60
            
        if seconds is None:
            self.__seconds = 0
        else:
            self.__seconds = abs(seconds) % 60


    # Getters
    def getSecond(self):
        return self.__seconds
    def getMinute(self):
        return self.__minutes
    def getHour(self):
        return self.__hours
    def getFormat(self):
        return self.__standardTime

    def __getHoursString(self):
        hoursString = ""
        if self.__hours % 12 == 0 and self.__standardTime:
            # 0 corresponds to 12 for standard time
            hoursString = "12"
        elif self.__standardTime:
            hoursString = str(self.__hours % 12)
        else:
            hoursString = str(self.__hours)
            
        if len(hoursString) == 1:
            hoursString = str(0) + hoursString

        return hoursString


    def __getMinutesString(self):
        minutesString = ""

        if self.__minutes < 10:
            minutesString = str(0) + str(self.__minutes)
        else:
            minutesString = str(self.__minutes)

        return minutesString

    def __getSecondsString(self):
        secondsString = ""

        if self.__seconds < 10:
            secondsString = str(0) + str(self.__seconds)
        else:
            secondsString = str(self.__seconds)

        return secondsString
            
        
    def displayCounter(self):
        # 0 hours displays as 12 hours standard time and PM/AM added for standard time
        # Midnight displays as 00:00:00 for military time
        hoursString = self.__getHoursString()
        minutesString = self.__getMinutesString()
        secondsString = self.__getSecondsString()

        timeString = hoursString + ":" + minutesString + ":" + secondsString
        if self.__hours > 11 and self.__standardTime:
            timeString += " PM"
        elif self.__hours <= 11 and self.__standardTime:
            timeString += " AM"
        
        print(timeString)
        return timeString

    def incrementSecond(self):
        if self.__seconds == 59:
            self.__seconds = 0
            self.incrementMinute()
        else:
            self.__seconds += 1
            
    def incrementMinute(self):
        if self.__minutes == 59:
            self.__minutes = 0
            self.incrementHour()
        else:
            self.__minutes += 1

    def incrementHour(self):
        if self.__hours == 23:
            self.__hours = 0
        else:
            self.__hours += 1

    
    def decrementSecond(self):
        if self.__seconds == 0:
            self.__seconds = 59
            self.decrementMinute()
        else:
            self.__seconds = (self.__seconds - 1)
            
    def decrementMinute(self):
        if self.__minutes == 0:
            self.__minutes = 59
            self.decrementHour()
        else:
            self.__minutes = (self.__minutes - 1)

    def decrementHour(self):
        if self.__hours == 0:
            self.__hours = 23
        else:
            self.__hours = (self.__hours - 1)
