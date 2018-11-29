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
    while (len(followerList)<40):
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
followerList = getFollowerStars()
print(followerList)
mostStarred = ""
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
print(topRepo())
langList = []
sizeList = []

def languages():
    returnList = []
    repoContent = []
    languageList = []
    #Map for file extentions to programing language
    languageDict = {
        'CS' : 'C#',
        'HPP':	'C++',
        'CLASS' : 'Java',
        'CPP' : 'C++',
        'ERB' : 'Ruby',
        'CP' : 'C++',
        'C' : "C",
        'MF' : 'Java',
        'DMD' : 'SQL',
        'JAVA' : 'Java',
        'PY' : 'Python',
        'RES' : 'C++',
        'SWIFT' : 'Swift',
        'XSD' : 'XML',
        'RBW' : 'Ruby',
        'CLW' : 'C++',
        'NCB' : 'C++',
        'SH' : 'Shell',
        'RPY' : 'Python',
        'HH' :	'C++',
        'CC' : 'C++',
        'PYD' : 'Python',
        'R' : 'R',
        'APS' : 'C++',
        'HS' : 'Haskell',
        'JS' : 'JavaScript',
        'HTML' : 'HTML',
        'CSS' : 'CSS',
        'PHP' : 'PHP',
        'PDE' : 'Processing',
        'XML' : 'XML'
    }
    for key, val in languageDict.items():
        #print (key)
        languageList.append(key)
    x = getFollowerStars()
    mostStarred = x[0][0]
    repo = g.get_user(mostStarred).get_repo(topRepo())
    #print(repo)
    repoDetails = { 'Name' : repo.name,
                        'Total' : 0         }
    contents = repo.get_contents('')
    #print(contents)
    for content_file in contents:
        if content_file.type == 'dir':
            contents.extend(repo.get_contents(content_file.path))


    for content_file in contents:
        if "." in content_file.path:
            split = content_file.path.split('.')
            if split[1].upper() in languageDict:
                if split[1].upper()  in langList:
                    index = langList.index(split[1].upper())
                    newTotal = sizeList[index] + content_file.size
                    sizeList[index] = newTotal
                else:
                    langList.append(split[1].upper())
                    sizeList.append(content_file.size)
    #print(langList)
    #print(sizeList)
    #print("this is a list of langs and size of files", langList)
    #returnList.append([langList,sizeList])
    return langList,sizeList
print(languages())
languages()





#if split[1].upper() in langList:
#    langList[langList.index(split[1])]
#langList.append([split[1],content_file.size])
#        print("this is file size", content_file.size)
#        repoContent.append(content_file.path)
#        print(content_file.path)
#    print(contents)




#contents = repo.get_contents('')
##print(contents)
#for content_file in contents:
#    if content_file.type == 'dir':
#        contents.extend(repo.get_contents(content_file.path))
#    for repo in content_file.name:
#        if '.' in repo:
#            split = repo.split('.')
#            if split[1].upper in languageDict:
#                extension_size.update({split[1]: content_file.size})
#                #if split[1] not in extension_size:
#                #    extension_size.update({split[1]: content_file.size})
                #else:
                #    extension_size.setdefault(split[1], )[split[1] += content_file.size]
#    print(extension_size)


#        filesizes.append(content_file.size)
#        repoContent.append(content_file.name)
#        #print(content_file.path)
##    print(repoContent)
#    print(filesizes)
#    for repo in repoContent:
##        if '.'in repo:
#            split = repo.split('.')
#            extensions.append(split[1])
#    print (extensions)
