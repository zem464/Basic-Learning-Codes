class TV:
    # Constructor: initialize the TV's starting state
    def __init__(self, channel=1, volume=1):
        self.channel = channel  # current TV channel
        self.volume = volume    # current volume level
        self.is_on = False      # TV is off by default

    # Turn the TV on
    def turn_on(self):
        self.is_on = True

    # Turn the TV off
    def turn_off(self):
        self.is_on = False

    # Return the current channel
    def get_channel(self):
        return self.channel

    # Change the channel only if the TV is on and the value is valid
    def set_channel(self, channel):
        if self.is_on and 1 <= channel <= 120:
            self.channel = channel

    # Return the current volume
    def get_volume(self):
        return self.volume

    # Change the volume only if the TV is on and the value is valid
    def set_volume(self, volume):
        if self.is_on and 1 <= volume <= 7:
            self.volume = volume

    # Move to the next channel
    def channel_up(self):
        if self.is_on and self.channel < 120:
            self.channel += 1
        return self.channel

    # Move to the previous channel
    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel -= 1
        return self.channel

    # Increase the volume by one level
    def volume_up(self):
        if self.is_on and self.volume < 7:
            self.volume += 1
        return self.volume

    # Decrease the volume by one level
    def volume_down(self):
        if self.is_on and self.volume > 1:
            self.volume -= 1
        return self.volume
