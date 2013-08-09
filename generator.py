# WallFly data generator
# Generate 5 Agents - record their user_ids
# For each Agent generate
# 	5 owners (and 5 tenants)
#		for each owner
#			generate 5 properties
#
#
#
#


import random
import copy

class User():
	def __init__(self, first_name, last_name, emailaddress, password, type):
		self.first_name = first_name
		self.last_name = last_name
		self.emailaddress = emailaddress
		self.password = password
		self.type = type

	def __eq__(self, other):
		return self.emailaddress == other.emailaddress 	

	def __str__(self):
		return self.emailaddress

	def sql(self):
		return "INSERT INTO `USERS` (email_address, first_name, last_name, type, password, salt) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', 'blah');".format(self.emailaddress, self.first_name, self.last_name, self.type, self.password)

class UserList():
	
	def __init__(self):
		self.userlist = [User(None, None, None, None, None)] #starting from 1

	def add(self, new):
		for existing in self.userlist:
			if existing == new:
				return 0
			break
		self.userlist.append(new)
		return len(self.userlist)
	
	def retr(self, index):
		return self.userlist[index]

class Property():
	def __init__(self, number, streetname, stype, suburb, postcode, state):
		self.number = number
		self.streetname = streetname
		self.stype = stype
		self.suburb = suburb
		self.postcode = postcode
		self.state = state

	def __str__(self):
		return "{0} {1} {2}, {3}, {4}, {5}".format(self.number, self.streetname, self.stype, self.suburb, self.postcode, self.state)

	def __eq__(self, other):
		return self.__str__() == other.__str__()
	
	def sql(self):
		return "INSERT INTO `PROPERTIES` (address, suburb, state) VALUES ('{0} {1} {2}', '{3}', '{4}');".format(self.number, self.streetname, self.stype, self.suburb, self.state)



class PropertyList():
	def __init__(self):
		self.propertylist = [Property(None, None, None, None, None, None)]

	def add(self, new):
		for existing in self.propertylist:
			if existing == new:
				return 0
			break
		self.propertylist.append(new)
		return len(self.propertylist)
	
	def retr(self, index):
		return self.propertylist[index]



global userList
userList = UserList()
global propertyList
propertyList = PropertyList()

global names 
names = "Harry, Jack, Oliver, Charlie, James, George, Thomas, Ethan, Jacob, William, Daniel, Joshua, Max, Noah, Alfie, Samuel, Dylan, Oscar, Lucas, Aidan, Isaac, Riley, Henry, Benjamin, Joseph, Alexander, Lewis, Leo, Tyler, Jayden, Zac, Freddie, Archie, Logan, Adam, Ryan, Nathan, Matthew, Sebastian, Jake, Toby, Alex, Luke, Liam, Harrison, David, Jamie, Edward, Luca, Elliot, Aaron, Finley, Michael, Zachary, Mason, Sam, Muhammad, Connor, Ben, Reuben, Theo, Rhys, Arthur, Caleb, Dexter, Rory, Jenson, Evan, Gabriel, Ewan, Callum, Seth, Felix, Austin, Owen, Leon, Cameron, Jude, Harley, Blake, Harvey, Tom, Hugo, Finn, Bobby, Hayden, Kyle, Jasper, Tommy, Eli, Kian, Andrew, John, Louie, Dominic, Joe, Elijah, Kai, Frankie, Stanley".split(", ")
global suburbs 
suburbs = [' Acacia Ridge', ' Albion', ' Alderley', ' Algester', ' Annerley', ' Anstead', ' Archerfield', ' Ascot', ' Ashgrove', ' Aspley', ' Auchenflower', ' Bald Hills', ' Balmoral', ' Banks Creek', ' Banyo', ' Bardon', ' Bellbowrie', ' Belmont', ' Berrinba', ' Boondall', ' Bowen Hills', ' Bracken Ridge', ' Bridgeman Downs', ' Brighton', ' Brisbane', ' Brookfield', ' Bulimba', ' Burbank', ' Calamvale', ' Camp Hill', ' Cannon Hill', ' Capalaba West', ' Carina', ' Carina Heights', ' Carindale', ' Carole Park', ' Carseldine', ' Chandler', ' Chapel Hill', ' Chelmer', ' Chermside', ' Chermside West', ' Chuwar', ' Clayfield', ' Coopers Plains', ' Coorparoo', ' Corinda', ' Darra', ' Deagon', ' Doolandella', ' Drewvale', ' Durack', ' Dutton Park', ' Eagle Farm', ' East Brisbane', ' Eight Mile Plains', ' Ellen Grove', ' England Creek', ' Enoggera', ' Enoggera Reservoir', ' Everton Park', ' Fairfield', ' Ferny Grove', ' Fig Tree Pocket', ' Fitzgibbon', ' Forest Lake', ' Fortitude Valley', ' Gaythorne', ' Geebung', ' Gordon Park', ' Graceville', ' Grange', ' Greenslopes', ' Gumdale', ' Hamilton', ' Hawthorne', ' Heathwood', ' Hemmant', ' Hendra', ' Herston', ' Highgate Hill', ' Holland Park', ' Holland Park West', ' Inala', ' Indooroopilly', ' Jamboree Hts', ' Jindalee', ' Kangaroo Point', ' Karana Downs', ' Karawatha', ' Kedron', ' Kelvin Grove', ' Kenmore', ' Kenmore Hills', ' Keperra', ' Kholo', ' Kuraby', ' Lake Manchester', ' Larapinta', ' Lota', ' Lutwyche', ' Lytton', ' Macgregor', ' Mackenzie', ' Manly', ' Manly West', ' Mansfield', ' Mcdowall', ' Middle Park', ' Milton', ' Mitchelton', ' Moggill', ' Moorooka', ' Moreton Island', ' Morningside', ' Mt Coot-tha', ' Mt Gravatt', ' Mt Gravatt East', ' Mt Ommaney', ' Mt Crosby', ' Murarrie', ' Nathan', ' New Farm', ' Newmarket', ' Newstead', ' Norman Park', ' Northgate', ' Nudgee', ' Nudgee Beach', ' Nundah', ' Oxley', ' Paddington', ' Pallara', ' Parkinson', ' Pinjarra Hills', ' Pinkenba', ' Port of Brisbane', ' Pullenvale', ' Ransome', ' Red Hill', ' Richlands', ' Riverhills', ' Robertson', ' Rochedale', ' Rocklea', ' Runcorn', ' Salisbury', ' Sandgate', ' Seven Hills', ' Seventeen Mile Rocks', ' Sherwood', ' Shorncliffe', ' Sinnamon Park', ' South Brisbane', ' Spring Hill', ' St Lucia', ' Stafford', ' Stafford Heights', ' Stretton', ' Sumner', ' Sunnybank', ' Sunnybank Hills', ' Taigum', ' Taringa', ' Tarragindi', ' Tennyson', ' The Gap', ' Tingalpa', ' Toowong', ' Upper Brookfield', ' Upper Kedron', ' Upper Mt Gravatt', ' Virginia', ' Wacol', ' Wakerley', ' Wavell Heights', ' West End', ' Westlake', ' Willawong', ' Wilston', ' Windsor', ' Wishart', ' Woolloongabba', ' Wooloowin', ' Wynnum', ' Wynnum West', ' Yeerongpilly', ' Yeronga', ' Zillmere']
global street_ending 
street_ending= ["Street", "Court", "Close", "Drive", "Road", "Circuit"]

def generateProperty():
	result = 0
	while True:
		stype = street_ending[random.randint(0, len(street_ending)-1)] 
		number = random.randint(0,250)
		streetname = names[random.randint(0, len(names)-1)]
		suburb = suburbs[random.randint(0,len(suburbs)-1)]
		postcode = random.randint(4000,4999)
		state = "QLD"
		property = Property(number, streetname, stype, suburb, postcode, state)
		result = propertyList.add(property)
		if result == 0:
			pass
		else:
			break
	return result-1

#generateProperties(properties, 4)




def generateUser(type):
	result = 0
	while True:
		first_name = names[random.randint(0, len(names)-1)]
		last_name = names[random.randint(0, len(names)-1)]
		emailaddress = first_name+last_name+str(random.randint(0,99))+"@example.com"
		password = "password" #lol security
		user = User(first_name, last_name, emailaddress, password, type)
		result = userList.add(user)
		if result == 0:
			pass
		else:
			break
	return result-1


def generateData(agents, owners, properties):
	#agents is how many base agents
	#all agents have specified number of owners
	#all owners have specified number of properties
	for a in range(agents):
		agentid = generateUser("Agent")
		print userList.retr(agentid).sql()
		for o in range(owners):
			ownerid = generateUser("Owner")
			print userList.retr(ownerid).sql()
			for p in range(properties):
				propertyid = generateProperty()
				print propertyList.retr(propertyid).sql()
				tenantid = generateUser("Tenant")
				print userList.retr(tenantid).sql()
				ownership = "INSERT INTO `ownership` (property_id, owner_id, notify_structural, notify_electrical, notify_plumbing, notify_security) VALUES ({0}, {1}, 1, 1, 1, 1);".format(propertyid, ownerid)
				print ownership

				tenancy = "INSERT INTO `tenancy` (property_id, tenant_id, start_date, end_date) VALUES ({0}, {1}, '12/8/13', '12/8/14');".format(propertyid, tenantid)
				print tenancy			


				management = "INSERT INTO `management` (property_id, agent_id) VALUES ({0}, {1});".format(propertyid, agentid)
				print management
			

generateData(10,10,5)


