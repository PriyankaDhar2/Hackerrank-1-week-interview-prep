def timeConversion(s):
    hour = int(s[:2])
    
    if s[-2:] == "AM":
        if hour == 12:
            return "00" + s[2:-2]
        else:
            return s[:-2]
    elif s[-2:] == "PM":
        if hour == 12:
            return s[:-2]
        else:
            return str(hour + 12).zfill(2) + s[2:-2]



result = timeConversion("07:45:30PM")
print(result)
