#strptime vs strftime (parse(string to date) vs format(date to string))
#datetime

from datetime import datetime
var1 = datetime.strptime("23-07-1993","%d-%m-%Y")
print(var1.strftime("%y/%m/%d"))