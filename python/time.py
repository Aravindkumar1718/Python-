seconds=int(input("ENTER THE TIME IN SECONDS="))
sec=seconds%60
minutes = seconds // 60
mins=minutes%60
hours = minutes //60
hour=hours%24
days =hours// 24
day=days%30
months = days//30
month=months%12

years = months// 12


print("Y"*len(str(years)),"M"*len(str(month)),"D"*len(str(day)),"H"*len(str(hour)),"M"*len(str(mins)),"S"*len(str(sec)))

print(years,month,day,hour,mins,sec)
