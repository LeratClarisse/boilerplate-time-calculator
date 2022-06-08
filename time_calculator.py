import constants

def add_time(start, duration, first_day = ""):
  #Init values
  hours = int(start.split(" ")[0].split(":")[0])
  minutes = int(start.split(" ")[0].split(":")[1])
  am_pm = start.split(" ")[1]
  nb_days = 0

  #Add duration
  hours += int(duration.split(":")[0])
  minutes += int(duration.split(":")[1])

  #Check if day change
  nb_days = hours // 24
  hours = hours % 24
  
  #Check if AM/PM change
  if hours > 12:
    if am_pm == "AM":
      am_pm = "PM"
    else:
      am_pm = "AM"
      nb_days += 1
    hours -= 12

  
  #Format result
  new_time = str(hours) + ":" + str(minutes).zfill(2) + " " + am_pm

  #Format with day change
  if nb_days == 1:
    new_time += " " + constants.NEXT_DAY
  elif nb_days > 1:
    new_time += " (" + str(nb_days) + " " + constants.DAYS_LATER + ")"

  return new_time