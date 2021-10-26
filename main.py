import matplotlib.pyplot as plt 
import os 

class Lesson(object):
	def __init__(self, name):
		self.name = name
		self.hours = []
		self.days = []

	def update(self, hour, day):
		self.hours.append(hour)
		self.day.append(day)

data_class = {
	"math" : [Lesson("math"), "%s.txt"%"math"],
	"phys" : [Lesson("phys"), "%s.txt"%"phys"],
	"chem" : [Lesson("chem"), "%s.txt"%"chem"],
	"bio" : [Lesson("bio"), "%s.txt"%"bio"],
	"geo" : [Lesson("geo"), "%s.txt"%"geo"],
	"arabic" : [Lesson("arabic"), "%s.txt"%"arabic"],
	"rel":[Lesson("rel"), "%s.txt"%"rel"],
	"farsi":[Lesson("farsi"), "%s.txt"%"farsi"]
}

print("running loading...")
for key, val in data_class.items():
	if not os.path.exists(".\\%s"%data_class[key][1]):
		with open(data_class[key][1], "a") as data:
			data.close()
	else:
		continue;
print("Precautions :\n - the format is fully represented in this example : \n\t lessonName/day/time \n - days should be three word abbriviations like Mon/Tue/Wed/Thu/Fri/Sat/Sun \n - name of the class #lessonName# should be one of below : \n math/phys/chem/bio/geo/rel/farsi \n - and finall hours should be in 24 hour format")

while (userInput := input("command : $  ")) != "quit":
	lesson, day, time = userInput.split("/")
	with open(data_class[lesson][1], "a") as data:
		data.write("\n%s/%s"%(day, time))
		data.close()

