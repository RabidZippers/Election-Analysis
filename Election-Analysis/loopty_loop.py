x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print ("Hello World")

#How may votes did you get?
my_votes = int(input("How may votes did you get in the election? "))
# Total votes in the election
total_votes = int(input ("what is the total votes in the election? "))
#Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes")