import twitter
import pandas as pd

'''
    This script will parse several public lists on Twitter which contain the usernames
    aka Twitter handles of members of the U.S Congress, from both the Republican and
    Democratic parties.

    It will also store this information in a .csv format at:
    './Generated Data/CongressMemberTwitterHandles.csv'
'''
if __name__ == "__main__":
    api = twitter.Api(consumer_key='O1TcM1r6K0hKZ7bnpjslpxaG5',
                  consumer_secret='4gSL38BmKvs63PU3lucl7e4Gz60sTWPnnoxQ3IBO2vEjFxJI9U',
                  access_token_key='1331694691256070144-nks9sd74IiAyt8e4CCHktQwUNTDBor',
                  access_token_secret='iCwbCbaHfBHpJ2fs7Hov0LCGBbAQov0nEiSVbs2bgXnUV')

    # https://twitter.com/TheDemocrats/lists/house-democrats/members
    house_democrats = api.GetListMembers('110250128')
    # https://twitter.com/TheDemocrats/lists/senate-democrats/members
    senate_democrats = api.GetListMembers('110247863')
    # https://twitter.com/HouseGOP/lists/house-republicans/members
    house_republicans = api.GetListMembers('817470159027929089')
    # https://twitter.com/SenateGOP/lists/senate-republicans/members
    senate_republicans = api.GetListMembers('559315')
    
    democrats_screen_names = []
    for user in house_democrats:
        democrats_screen_names.append(user.screen_name)
    for user in senate_democrats:
        democrats_screen_names.append(user.screen_name)

    republicans_screen_names = []
    for user in house_republicans:
        republicans_screen_names.append(user.screen_name)
    for user in senate_republicans:
        republicans_screen_names.append(user.screen_name)

    output_data = pd.DataFrame([democrats_screen_names, republicans_screen_names]).transpose()
    output_data.columns = ['Democrats','Republicans']
    output_data.to_csv('./Generated Data/CongressMemberTwitterHandles.csv',index=False)
    
    
