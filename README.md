# EC601_Project2

## Introduction
This is the project2 of Boston University EC601 which is a social media analyzer. The project includes 2 parts, one is the test programs for Twitter APIs, Botometer and Google NLP APIs. And for each programme there will be explanations.

## Twitter APIs
For testing Twitter APIs, I referenced official doucmentation(https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start/recent-search) which is the programe can return the recent Tweets posted over the last week by one user.
The test programe is TwitterAPI_Test01.py(from https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/main/Recent-Search), which contains two functions, one is authorization and the other is building connection.
### Steps of recent-search
The steps are including using authorization to connect and get access to the most recent Tweets by the specify user(where I used Elon Musk), and then print the result.
One of the important things is building a search query which can be seen as a filter of search, to get what you want as return. In this test programe, I searched Elon Musk and return user id.
### Results
<img width="826" alt="截屏2022-10-05 下午12 38 53" src="https://user-images.githubusercontent.com/48322294/194114821-90a4b131-b6fd-490a-b5b5-8499530397f0.png">
The results of the test programs are including author_id, edit_history_tweet_ids, id and text.
From the official documentationm 
id(Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers)<br>
text(The content of the Tweet)<br>
author_id(Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers)<br>
edit_history_tweet_ids(Unique identifiers indicating all versions of an edited Tweet. For Tweets with no edits, there will be one ID. <br>
For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edit, with the most recent version in the last position of the array)

## Google NLP APIs
For testing Google APIs, I referenced official documentation(https://cloud.google.com/natural-language/docs/reference/libraries).<br>
The program uses analyze_sentiment method from LanguageServiceClient Class (https://cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient), which provides text analysis operations such as sentiment analysis and entity recognition.<br> The test program is GNAPI_Test01.py.

### Results
<img width="398" alt="截屏2022-10-05 下午2 36 13" src="https://user-images.githubusercontent.com/48322294/194136702-622f94e0-ffd1-4076-80c3-c2479667d65a.png">
The result shows the score(relatively positive) and the magnitude(relatively emotional)


## Botometer APIs
The Botometer APIs is based on Rapid API(https://rapidapi.com/hub)
Test endpoint:
<img width="250" alt="截屏2022-10-07 上午11 21 51" src="https://user-images.githubusercontent.com/48322294/194590174-7aeefc53-221a-4b3b-aeeb-8c64277c344d.png">


## User Stories
I, the shop owner, wants to do the statistical review about how people feel about my shop.<br>
I, social science researcher, wants to do my research projects.<br>
I, the investor, wants to know what kind of areas are people intrested in.
