listFollowersFile = open('new_followers.txt', 'r+')
listFollowersFileB = open('new_followersB.txt', 'r')

newFollowersA = sorted(set([x.replace('\n', '') for x in listFollowersFile]))
newFollowersB = sorted(set([x.replace('\n', '') for x in listFollowersFileB]))

ultimateList = set(newFollowersB) - set(newFollowersA)

listFollowersFile = open('new_followers.txt', 'w')

for x in sorted(ultimateList):
    listFollowersFile.write(f'{x}\n')

listFollowersFile.close()

# newListFollowersFile = open('my_followers.txt', 'w')

# for x in newFollowers:
#     newListFollowersFile.write(x)
