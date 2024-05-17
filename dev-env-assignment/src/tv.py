class tv:
    # A tv will have 120 channels (1 - 120), 7 volumes (1 - 7), and it will 
    # be either on or off. These attributes will be set up in the tv class as
    # 3 private fields that will be validated and initialized in the class's
    # constructor.
    def __init__(self, channel, volume, on):
        # For each field, check if the constructor has been given an errant
        # value. If it has, raise a value error, display the error, and exit.
        # Else, initialize the field.
        try:
            if (channel < 1 or channel > 120):
                    raise ValueError("Channel must be between 1 and 120.")             
        except ValueError as e:
            exit(e)
        else:
            self.__channel = channel

        try:
            if (volume < 1 or volume > 7):
                raise ValueError("Volume must be between 1 and 7.")             
        except ValueError as e:
            exit(e)
        else:
            self.__volume = volume

        try:
            if (on != True and on != False):
                raise ValueError("On must be True or False.")             
        except ValueError as e:
            exit(e)
        else:
            self.__on = on

    def setChannel(self, channel):
        # Set the channel if the tv is on and the specified channel
        # is valid.
        if (self.__on and channel >= 1 and channel <= 120):
            self.__channel = channel
    
    def setVolume(self, volume):
        # Set the volume if the tv is on and the specified volume
        # is valid.
        if (self.__on and volume >= 1 and volume <= 7):
            self.__volume = volume

    def turnOn(self):
        self.__on = True

    def turnOff(self):
        self.__on = False

    def channelUp(self):
        # Increase the channel by 1 if the tv is on and the
        # channel is less than 120.
        if (self.__on and self.__channel < 120):
            self.__channel += 1

    def volumeUp(self):
        # Increase the volume by 1 if the tv is on and the
        # volume is less than 7.
        if (self.__on and self.__volume < 7):
            self.__volume += 1

    def channelDown(self):
        # Decrease the channel by 1 if the tv is on and the
        # channel is greater than 1.
        if (self.__on and self.__channel > 1):
            self.__channel -= 1

    def volumeDown(self):
        # Decrease the volume by 1 if the tv is on and the
        # volume is greater than 1.
        if (self.__on and self.__volume > 1):
            self.__volume -= 1

    def __str__(self):
        return f"TV channel={self.__channel} volume={self.__volume} on={self.__on}"