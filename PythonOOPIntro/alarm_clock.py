class AlarmClock:
  def __init__ (self):
    self.current_time = self.change_current_time()
    self.time_for_alarm = self.set_time_for_alarm()
    self.is_alarm_on = self.turn_alarm_on_off()
    self.time_and_alarm_info = self.clock_info()
  
  def change_current_time (self):
    set_time = input("Please enter the current time in 24 hour format: ") 
    return set_time

  def turn_alarm_on_off (self):
    choice = input("Do you want to turn the alarm on? Please enter - Yes or No: ").lower()
    if choice == "yes" or choice == "y":
      return True
    else:
      return False
    
  def set_time_for_alarm (self):
    set_alarm_time = input("Please enter the time you want the alarm to go off in 24 hour format: ")
    return set_alarm_time

  def clock_info (self):
    return print(f"The current time is: {self.current_time} \nThe alarm is set for: {self.time_for_alarm}")





