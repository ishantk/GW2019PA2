import pandas as pd

Teams = ["Rajasthan Royals",
         "Deccan Chargers",
         "Chennai Super Kings",
         "Chennai Super Kings",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Sunrisers Hyderabad",
         "Mumbai Indians",
         "Chennai Super Kings",
         "Mumbai Indians"
         ]

Ranks = [2, 3, 3, 5, 1, 6, 1, 1, 3, 4, 4, 5]

Years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

data = {"Team":Teams, "Rank":Ranks, "Year":Years}

frame = pd.DataFrame(data)
print("------------------------------")
print(frame)
print("------------------------------")

print()

print("---------Group By Teams----------")
teamGroups = frame.groupby("Team")
print(teamGroups.groups)
print("------------------------------")

print()

print("---------Group By Teams and Ranks----------")
teamRankGroups = frame.groupby(["Team", "Rank"])
print(teamRankGroups.groups)
print("------------------------------")

print()

print("---------Iterate in Groups----------")

teamGroups = frame.groupby("Team")
for teamName, grp in teamGroups:
    print(teamName)
    print("--------------")
    print(grp)

print("------------------------------")

print()

print("---------Fetch a Single Group Item----------")

teamGroups = frame.groupby("Team")

print(teamGroups.get_group("Mumbai Indians"))

print("------------------------------")