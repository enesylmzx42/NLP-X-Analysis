# Twitter User Prediction Project

This project involves predicting the percentage likelihood of an entered alternative tweet belonging to a specific user using a database created with data collected from Twitter.
<br>
<br>
## Project Applications
- Probability calculation of a tweet being shared by someone else.
- Prediction of which user might have written an unpublished tweet.


## Retrieving Data from Twitter

Data retrieval is performed using the snscrape library available in Python. This library is essentially an implementation of the Advanced Search feature on Twitter within a programming environment.<br><br>
In this example, the query aims to fetch all tweets from the Twitter account with the username "netflixturkiye" between January 1, 2021, and January 1, 2023. Following the data retrieval, the obtained information is exported to a CSV file for further processing.
<br>
<br>



## Data Preprocessing

In another Python script, the imported data undergoes a cleaning process. The cleaning function removes numbers, certain meaningless words, and punctuation from the tweets. The cleaned tweets are then stored in the 'clean' column of the dataset.

To facilitate the proper functioning of our algorithm, we need to label the tweets according to the following scheme:

- Acun Ilıcalı: 0
- Rasim Ozan Kütahyalı: 1
- Webtekno: 2
- Netflix: 3

## Analysis using Machine Learning Algorithms

For the analysis of the data, we employ TF-IDF, Bayes theorem, and Decision Tree algorithms. The project is now completed, and it can accurately proportion the likelihood of a given tweet belonging to one of the four users.
<br>
## Classification Results

As a final step, we provide the project with a tweet from Netflix's past: "önerdiğim diziyi izledin mi diyorum bana nau nau diyor." The results of the classification are as follows:

- Acun Ilıcalı: 0.56%
- Rasim Ozan Kütahyalı: 6.95%
- Webtekno: 4.92%
- Netflix: 87.57%

## Usage

1. Ensure you have the required libraries installed: `snscrape`, `pandas`, `scikit-learn`.
2. Run the data retrieval script.
3. Run the data preprocessing script.
4. Utilize the machine learning algorithms for analysis.

Feel free to explore and adapt the code according to your needs!
