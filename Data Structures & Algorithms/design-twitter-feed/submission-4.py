#have a map of person : following
#have another map of person : list 
#when you do getNewsFeed check if their following list is empty 
#if not combine thier list of their own + following and sort, 
#create lists [time, tweetid]

class Twitter:

    def __init__(self):
        self.time = 0 
        self.following_map = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-1 * self.time, tweetId])
        self.time += 1
        # print(self.tweets)
    def getNewsFeed(self, userId: int) -> List[int]:
        print(userId)
        print(self.following_map[userId])
        combined_tweets = self.tweets[userId].copy()
        res = []
        if self.following_map[userId]:
            #iterate through all of it's followings and combine the tweets into one array 
            for f in self.following_map[userId]:
                combined_tweets.extend(self.tweets[f])


        heapq.heapify(combined_tweets)
        print(combined_tweets)
        if len(combined_tweets) >= 10:
            for i in range(10):
                curr = heapq.heappop(combined_tweets)
                res.append(curr[1])
        else:
            while combined_tweets:
                curr = heapq.heappop(combined_tweets)
                print(curr)
                res.append(curr[1])        
        return res 




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)