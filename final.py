from github import Github

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

#gets basic profile information of the searched user
def getProfileInfo():
    profileInfo = []
    userName = user.name
    userNoFollowers = user.followers
    userAvatar = user.avatar_url
    userBio = user.bio
    profileInfo.append([userName,userNoFollowers, userAvatar, userBio])
    return profileInfo
#print ("This is the profile Information of the logged in user",getProfileInfo())

#returns a sorted list of followers and their respective star counts
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
        followerList.append([follower.login, totalStars])
    followerList.sort(key=lambda x:x[1])
    followerList.reverse()
    #print (followerList)
    return followerList
#print ("these are the followers and their respective stars", getFollowerStars())

#returns the most starred repo by the most starred user
def topRepo():
    topRepoList = []
    maxStar = 0
    x = getFollowerStars()
    mostStarred = x[0][0]                                           #the name of most starred user. 'Conor Gildea'
    #print(mostStarred)
    for repo in g.get_user(mostStarred).get_repos():
        stars = repo.stargazers_count
        topRepoList.append([repo.name, stars])
        if (stars > maxStar):
            maxStar = stars
            repoStars = stars
            maxRepo = repo.name
    #print (maxRepo , maxStar)
    #print (topRepoList)
    return maxRepo

topRepo()
