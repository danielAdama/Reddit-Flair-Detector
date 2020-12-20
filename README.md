# Reddit-Flair-Detector
Reddit Flair Detection App: An end-to-end Machine Learning Project

**Summary
A flair is a 'label' that can be attached within a sub-reddit to posts shared on the Reddit website. They help users understand the group to which the posts they browse through belong, and hence help them sort out relevant posts depending on their interests.

This web-app i created performs the task of predicting which flair should be alloted to a post. A user just need to paste the link of the reddit post in the search bar. 

**Directory Structure
-I have made a flask app which is hosted on Heroku. The structure can be found here.
Data Collected: India Subreddit data_1.csv-the data i scrapped from India subreddit
Data Collection, Exploratory Data Analysis, Data Preprocessing, Data Visualization and Model Development are all on this file named Reddit Flair Detection project.ipynb

**inference.py: Inference Engine that runs the model and returns the predictions
**app.py:Contains the flask app
Built a multitext Machine Learning model classifier from scratch while scrapping live data from reddit which is then integrated into a web application so that user can submit a subreddit URL
