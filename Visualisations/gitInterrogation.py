from github import Github
#Possible expansion is to get totalstars for each follower then get stars from best repo and then display % of totalstars the best h
starList = []
#takes in login details and asks user which repo theyd like to run the program on
while True:
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    userToSearch = input("which user would you like to examine: ")
    try:
        g = Github(username,password)
        user = g.get_user(userToSearch)
    except:
        print("These details are incorrect. Please re-enter correct details")
        continue
    else:
        break

#gets all the followers of a given repo
def getFollowers():
    followerList = []
    for follower in user.get_followers():
        followerList.append(follower.login)

    return followerList

#gets the total stars of a user by summing all their individual repo stars
def getStars(f):
    stars = 0
    totalStars = 0
    for repo in g.get_user(f).get_repos():
        stars = repo.stargazers_count
        totalStars = totalStars+stars
    starList.append(totalStars)
    #return totalStars

#gets the most amount of stars from starlist
def getMaxStars():
    maxStar=0
    for star in starList:
        if (star>maxStar):
            maxStar = star
    return maxStar

#takes in maxStar and returns the user from the list of followers with the most stars
def identifyMaxUser():
    maxStarName = ""
    bothList = []
    for follower in followerList:
        followerStars = getStars(follower)
        bothList.append([follower, followerStars])
        maxStar = getMaxStars()

        maxStarIndex = starList.index(maxStar)
        maxStarName = followerList[maxStarIndex]
    print("User with most stars:'", maxStarName, "' who has", maxStar, "stars.")
    return maxStarName

#from the most starred user returns their most starred repo
def mostStarredRepo():
    repoNameAndStar = []
    maxUser = g.get_user(maxStarName)
    for repo in maxUser.get_repos():
        repoStars = repo.stargazers_count
        maxRepoName = ""
        maxUserMaxStar = 0
        maxRepoName = ""
        if (repoStars > maxUserMaxStar):
            maxUserMaxStar = repoStars
            maxRepoName = repo.name
    repoNameAndStar = [maxRepoName, maxUserMaxStar]
    return repoNameAndStar

#function calls
followerList = getFollowers()
for follower in followerList:
    getStars(follower)
maxStarName = identifyMaxUser()
bestRepo = mostStarredRepo()
print("The repo with the most stars by", maxStarName, "is", bestRepo)
