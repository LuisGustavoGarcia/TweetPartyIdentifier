import twitter
import pandas as pd

if __name__ == "__main__":
    api = twitter.Api(consumer_key='O1TcM1r6K0hKZ7bnpjslpxaG5',
                  consumer_secret='4gSL38BmKvs63PU3lucl7e4Gz60sTWPnnoxQ3IBO2vEjFxJI9U',
                  access_token_key='1331694691256070144-nks9sd74IiAyt8e4CCHktQwUNTDBor',
                  access_token_secret='iCwbCbaHfBHpJ2fs7Hov0LCGBbAQov0nEiSVbs2bgXnUV',
                    tweet_mode = 'extended')

    csv_filepath = './Generated Data/CongressMemberTwitterHandles.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)

    # Parse List of Democratic Congress Member's Twitter Handles.
    democrat_twitter_handles = []
    for handle in data_frame['Democrats']:
        if handle != '':
            democrat_twitter_handles.append(handle)

    # Find <num_of_tweets_requested> Tweets for each Congress Member and store them.
    democrat_tweets = []
    num_of_tweets_requested = 100
    for handle in democrat_twitter_handles:
        try:
            timeline = api.GetUserTimeline(screen_name=handle, count=num_of_tweets_requested, exclude_replies = True)
            tweets = []
            for status in timeline:
                tweets.append(status.full_text)
            democrat_tweets.append(tweets)
        except:
            continue
    
    output_data = pd.DataFrame([democrat_twitter_handles, democrat_tweets]).transpose()
    output_data.columns = ['Democrat Twitter User','Tweets']
    output_data.to_csv('./Generated Data/DemocratMemberTweets.csv',index=False)
