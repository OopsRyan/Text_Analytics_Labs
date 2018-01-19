from nltk.metrics.distance import edit_distance


tweet1 = "@RussellBruce17 #Ophelia's textbook evolution from hurricane to intense post-tropical cyclone, as seen via Air Mass RGB"
tweet2 = "@Beverleyknight Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
tweet3 = "@HelpfulOlive Inspirational, powerful, emotional.......#Axel documentary is excellent right from the start. Beautiful tribute."
tweet4 = "@orourke28 Remember who you are. The Black Panther and Lion King parallel: a amazing aesthetic.#BlackPanther"
tweet5 = "@kalimalana Here's a little something to get you pumped about starting a new week. Let's do this! #MondayMotivation #ACDC"

# spam tweets on tweet2
### changes to username
spam1 = "@@AppVader Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam2 = "@burvill19 Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam3 = "@lucillejp Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam4 = "@gembains Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam5 = "@springviewer Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam6 = "@trendinaliaIE Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam7 = "@Kelticanz #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam8 = "@Sunflower252 Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam9 = "@amy_green Storm #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
spam10 = "@ANGETERRY #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson"
### changes to tiny url
spam11 = "@annemccoy #Ophelia makes its presence felt at Spelga Dam https://youtu.be/6YziZ1FlAWs - Courtesy of Ryan Simpson"
spam12 = "@legendadele #Ophelia makes its presence felt at Spelga Dam https://youtu.be/6YziZ1FlAWs - Courtesy of Ryan Simpson"
spam13 = "@Claudde #Ophelia makes its presence felt at Spelga Dam https://youtu.be/6YziZ1FlAWs - Courtesy of Ryan Simpson"
spam14 = "@Daily_Express #Ophelia makes its presence felt at Spelga Dam https://youtu.be/6YziZ1FlAWs - Courtesy of Ryan Simpson"
spam15 = "@saintbannerman @blondiesaint #Ophelia makes its presence felt at Spelga Dam https://youtu.be/6YziZ1FlAWs - Courtesy of Ryan Simpson"
### add multi hashtags
spam16 = "@TimesTelevision #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson #trndnl"
spam17 = "@SophieOsborne1 #Ophelia makes its presence felt at Spelga Dam  http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson #GeorgeMichael"
spam18 = "@SiobhanHare1 #Ophelia makes its presence felt at Spelga Dam  http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson #GeorgeMichaelFreedom #GeorgeMichael"
spam19 = "@ELGreen93 #Ophelia makes its presence felt at Spelga Dam  http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson  #artist ! #RIP"
spam20 = "@hollie_campbell #Ophelia makes its presence felt at Spelga Dam http://bit.ly/2gJWHvX - Courtesy of Ryan Simpson #Older #faith"

tweet_list = [tweet1, tweet2, tweet3, tweet4, tweet5]
spam_list = [spam1,spam2,spam3,spam4,spam5,spam6,spam7,spam8,spam9,spam10,spam11,spam12,spam13,spam14,spam15,spam16,spam17,spam18,spam19,spam20]
edit_dis = list()

for tweet in tweet_list:
    edit_dis.append([edit_distance(tweet, spam, transpositions=False) for spam in spam_list])
for i in edit_dis:
    for j in i:
        print(j)
    print("==========================")