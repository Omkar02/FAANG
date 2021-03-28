# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def t(n):
    head = '+' * 10
    print(f'{head} {n} {head}')


class Twitter:
    def __init__(self):
        self.users_post = {}
        self.followers = {}
        self.mostRecent = 0

    def postTweet(self, user_id, post_id):
        self.mostRecent -= 1
        if user_id not in self.users_post:
            self.users_post[user_id] = []
        self.users_post[user_id].append((self.mostRecent, post_id))

    def getNewsFeed(self, user_id):
        return self._newsFeedHelper(user_id)

    def _newsFeedHelper(self, user_id):
        tweets = []
        cnt = 0
        if user_id in self.users_post:
            tweets.extend(self.users_post[user_id])
        if user_id in self.followers:
            # list of all followers
            followees = self.followers[user_id]

            for u_id in followees:
                if u_id in self.users_post:
                    tweets += self.users_post[u_id]

        return [idx for _, idx in sorted(tweets, key=lambda a:a[0])[:10]]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            if followerId not in self.followers:
                self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        else:
            return

    def unfollow(self, followerId, followeeId):
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)


def longStringWithK(string, k):
    t('longest-substring-with-at-most-k-distinct-characters')

    letterPos = {}
    startIdx = temp = 0
    n = len(string)
    currLen, maxLen = 0, float('-inf')
    for i in range(n):
        if string[i] not in letterPos:
            letterPos[string[i]] = 0
        letterPos[string[i]] += 1
        currLen += 1
        if len(letterPos) > k:
            while letterPos[string[startIdx]] != 0:
                currLen -= 1
                letterPos[string[startIdx]] -= 1
                temp += 1
            del letterPos[string[startIdx]]
            startIdx = temp
            temp = endIdx + 1
        endIdx = i

        if currLen > maxLen:
            maxLen = currLen
            res = [startIdx, endIdx]
    return maxLen, string[res[0]:res[1] + 1]


string = 'aaabcccca'
k = 1
print(longStringWithK(string, k))
