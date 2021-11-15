box=[]
data = youtube.commentThreads().list(part='snippet', videoId=ID, maxResults='100', textFormat="plainText").execute()
# response format :https://developers.google.com/youtube/v3/docs/commentThreads/list
for i in data["items"]:

    name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
    comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
    published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
    likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
    replies = i["snippet"]['totalReplyCount']

    box.append([name, comment, published_at, likes, replies])

    totalReplyCount = i["snippet"]['totalReplyCount']

    if totalReplyCount > 0:

        parent = i["snippet"]['topLevelComment']["id"]
#les replies 
        data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                        textFormat="plainText").execute()

        for i in data2["items"]:
            name = i["snippet"]["authorDisplayName"]
            comment = i["snippet"]["textDisplay"]
            published_at = i["snippet"]['publishedAt']
            likes = i["snippet"]['likeCount']
            replies = ""

            box.append([name, comment, published_at, likes, replies])

while ("nextPageToken" in data):

    data = youtube.commentThreads().list(part='snippet', videoId=ID, pageToken=data["nextPageToken"],
                                         maxResults='100', textFormat="plainText").execute()

    for i in data["items"]:
        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
        likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
        replies = i["snippet"]['totalReplyCount']

        box.append([name, comment, published_at, likes, replies])

        totalReplyCount = i["snippet"]['totalReplyCount']

        if totalReplyCount > 0:

            parent = i["snippet"]['topLevelComment']["id"]

            data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                            textFormat="plainText").execute()

            for i in data2["items"]:
                name = i["snippet"]["authorDisplayName"]
                comment = i["snippet"]["textDisplay"]
                published_at = i["snippet"]['publishedAt']
                likes = i["snippet"]['likeCount']
                replies = ''

                box.append([name, comment, published_at, likes, replies])

--
*******************************************************************

#scrappy from research

query = 'Messi'

query_results = youtube.search().list(
        part = 'snippet',
        q = query,
        order = 'relevance', # You can consider using viewCount
        maxResults = 20,
        type = 'video', # Channels might appear in search results
        relevanceLanguage = 'en',
        safeSearch = 'moderate',
        ).execute()

video_id = []
channel = []
video_title = []
video_desc = []
for item in query_results['items']:
    video_id.append(item['id']['videoId'])
    channel.append(item['snippet']['channelTitle'])
    video_title.append(item['snippet']['title'])
    video_desc.append(item['snippet']['description'])

--
*******************************************************************
