#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
# return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
    return "off" if day in [0,6] and vacation else "10:00" if vacation or day in [0,6] else "7:00"


print(alarm_clock(1, False)) # → '7:00'
print(alarm_clock(5, False)) # → '7:00'
print(alarm_clock(0, False)) # → '10:00'
print(alarm_clock(6, False)) #→ '10:00'	'10:00'	OK	
print(alarm_clock(0, True)) # → 'off'	'off'	OK	
print(alarm_clock(6, True)) # → 'off'	'off'	OK	
print(alarm_clock(1, True)) # → '10:00'	'10:00'	OK	
print(alarm_clock(3, True)) # → '10:00'	'10:00'	OK	
print(alarm_clock(5, True)) # → '10:00'	'10:00'	OK