import constants

def add_time(start, duration, first_day = ""):
  #Init values
  hours = int(start.split(" ")[0].split(":")[0])
  minutes = int(start.split(" ")[0].split(":")[1])
  am_pm = start.split(" ")[1]

  #Add duration
  hours += int(duration.split(":")[0])
  minutes += int(duration.split(":")[1])

  #Check if AM/PM change
  if hours > 12:
    if am_pm == "AM":
      am_pm = "PM"
    else:
      am_pm = "AM"
    hours -= 12

  #Check if day change
  
  #Format result
  new_time = str(hours) + ":" + str(minutes).zfill(2) + " " + am_pm

  return new_time