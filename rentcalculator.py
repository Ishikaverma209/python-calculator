# these are the info needed
#total food ordered by the roommates
#electricity units spent
#charge per unit 
#no of persons living in flat
## output = total amount an individuals have to pay

rent = int(input("enter your flat rent =="))
food = int(input("enter the amount of food rommates ordered == "))
electricity_spent = int(input("enter the total of electricity spent=="))
charge_per_unit_of_electricity = int(input("enter the charge per unit spent=="))
persons = int(input("enter the number of roommates living in flat=="))
total_bill = electricity_spent*charge_per_unit_of_electricity
output = (food+rent+total_bill)//persons
print("Each roommate will pay= ", output)