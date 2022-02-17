import tweepy
import config

auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

"""""
users = client.get_users(usernames=['cartesiproject'])
#for user in users:
print(users)
"""""


tweets = client.get_users_tweets(id=config.EXCL_USER_ID, tweet_fields=['lang'])

for tweet in tweets.data:
    print(tweet.id)
    print(tweet.text)
    print(tweet.lang)

print(" ")

#users who follow the channel
def get_user_followers(id):
    users = client.get_users_followers(id=id)
    followers = 0
    for user in users.data:
        print("ID: " + str(user.id))
        print("Username: " + user.username)
        followers = followers + 1
    print("Followers: " + str(followers))

#who user follows by user ID
def following_user(id):
    users = client.get_users_following(id=id)
    following = 0
    for user in users.data:
        following = following + 1
        print("ID: " + str(user.id))
        print("Username: " + user.username)
    print("Following: " + str(following))

#get user who liked a tweet by tweet ID
def get_liked_user(id):
    users = client.get_liking_users(id=id)
    count = 0
    for user in users.data:
        count = count + 1
        print("ID: " + str(user.id))
        print("Username: " + user.username)
    print("Liked Users: " + str(count))

def retweet_a_tweet(id):
    users = client.get_retweeters(id=id)
    count = 0
    for user in users.data:
        count = count + 1
        print("ID: " + str(user.id))
        print("Username: " + user.username)
    print("Retweets: " + str(count))

if __name__ == '__main__':
    tweet_id = '1488361822113652743'
    get_liked_user(tweet_id)

    print(" ")
    print("following users")
    following_user(config.EXCL_USER_ID)

    print(" ")
    print("Who user Follows")
    get_user_followers(config.EXCL_USER_ID)

    print(" ")
    print("Who retweets a tweet")
    retweet_a_tweet(tweet_id)