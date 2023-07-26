def get_input():
    while True:
        n=input("enter an amount of time")
        unit=input("enter a unit of time; days hours mins secs")
        if n.isdigit() and unit in ["secs","mins","hours","days"]:
            return int(n), unit


def convert_time(n, unit):
    seconds=convert_to_seconds(n, unit)
    days=seconds//(24*60*60)
    hours=seconds%(24*60*60) // (60*60)
    mins=seconds%(24*60*60)%(60*60)//60
    secs=seconds%(24*60*60)%(60*60)%60
    return days, hours, mins, secs

def convert_to_seconds(n, unit):
    if unit=="days":
        return(n*60*60*24)
    if unit=="hours":
        return(n*60*60)
    if unit=="minutes":
        return(n*60)
    if unit=="seconds":
        return n

n, unit=get_input()
days, hours, mins, secs = convert_time(n, unit)
print("hi")