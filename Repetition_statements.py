# x=0
# while x <=5:
#     print(x)
#     x=x+1

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# counties_dict.keys()
# for county in counties_dict:
#     print(counties_dict[county])

# for voters in counties_dict.values():
#     print(voters)

# for key,value in counties_dict.items():
#     print(key, value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)           

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])

# for key, value in counties_dict.items():
#     print(key,value)

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

for county_dict in voting_data:
     print(county_dict['county'])