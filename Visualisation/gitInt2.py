from github import Github
import re
#Returns info about the logged in users profile and repos  as a string

#lets user login
while True:
    username =  "kinanec"                      #input("please enter your username: ")
    password =  "199seven"                #input("please enter your password: ")
    userToSearch = input("which user would you like to examine: ")
    try:
        g = Github(username,password)
        user = g.get_user(userToSearch)
    except:
        print("These details are incorrect. Please re-enter correct details")
        continue
    else:
        break

def getProfileInfo():
    profileInfo = []
    userName = user.name
    userNoFollowers = user.followers
    userAvatar = user.avatar_url
    userBio = user.bio
    profileInfo.append([userName,userNoFollowers, userAvatar, userBio])
    return profileInfo

print ("This is the profile Information of the logged in user",getProfileInfo())

def getFollowerStars():
    followerList = []
    for follower in user.get_followers():
        #followerList.append(follower.name)
        stars = 0
        totalStars = 0
        for repo in follower.get_repos():
            stars = repo.stargazers_count
            totalStars = totalStars+stars
        #followerList.append(totalStars)
        followerList.append([follower.name, totalStars])
    return followerList

def maxRepoStars():
    maxStarRepoName = ""
    followerName = ""
    maxStar = 0
    thisDict = {}
    for follower in user.get_followers():
        for repo in follower.get_repos():
            stars = repo.stargazers_count
            if stars > maxStar:
                maxStarRepoName = repo.name
                followerName = follower.name
                thisDict = {
                    "user1": follower,
                    "user": followerName,
                    "repo": maxStarRepoName
                }
    return thisDict




thisDict = maxRepoStars()
userWithMaxRepo = thisDict.get("user")
maxStarRepoName = thisDict.get("repo")

print ("The follower who has most starred repo is:",userWithMaxRepo, "and the repos name is:",maxStarRepoName)



print ("these are the followers and their respective stars", getFollowerStars())
