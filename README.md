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
edit_history_tweet_ids(Unique identifiers indicating all versions of an edited Tweet. For Tweets with no edits, there will be one ID. For Tweets with an edit history, there will be multiple IDs, arranged in ascending order reflecting the order of edit, with the most recent version in the last position of the array)

## Google NLP APIs
