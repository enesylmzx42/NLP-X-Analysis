# Tweet Analysis
<br>

![dd](https://github.com/enesylmzx42/CNN-LetterRecognition-JS-Flask/assets/117593621/8e83be33-d02d-4a68-a99e-7c79d0bf84d3)

<br>
<br>
<br>
In this project, using a database created with data pulled from Twitter, the ownership of an alternative Tweet can be estimated as a percentage.
<br>
<br>

## Use Cases of the Project
- The likelihood of a tweet having been shared by someone before can be calculated.
- It can predict which user might have written a tweet that has not been shared before.
<br/><br/><br/>

## Fetching Data from Twitter
The `snscrape` library in Python was used for data scraping.<br/> This library is essentially the software-implemented version of Twitter's `Advanced Search` feature.

```
query = "(from:netflixturkiye) until:2023-01-01 since:2021-01-01"
```

In the given example, a query is shown where we want to see all tweets from the Twitter account with the username `netflixturkiye` between the dates `01.01.2021 - 01.01.2023`.
<br/> Subsequently, the fetched data is transferred to a CSV file, making it ready for processing.
<br/><br/>

## Processing the Data
The imported data in another Python file undergoes a cleaning function.
<br>
<br>
![nlp](https://github.com/enesylmzx42/NLP-X-Analysis/assets/117593621/652bccef-3161-49b7-9783-72813ddb8d26)

<br>
<br/> In this cleaning function, numbers and some words in the data are removed as they do not convey any meaningful information.
<br/> Then, the tweets, also stripped of punctuation marks, are written under the `clean` column.
<br/> For our algorithm to work correctly, we need to label the tweets.
<br/>

```
* Acun Ilıcalı: 0
* Rasim Ozan Kütahyalı: 1
* Webtekno: 2
* Netflix: 3
```

<br/> We label our data according to the labeling above.
<br/>

![Screenshot_4](https://user-images.githubusercontent.com/78226423/210455971-670e4385-9498-47ed-b119-8e375de1fd02.png)
<br/>
<br>
<br>

We use `TF-IDF`, `Bayes theorem`, and `Decision Tree` algorithms for the analysis we will obtain from the data.
<br/> Our project is now completed and can effectively estimate to which of the 4 users a given Tweet might belong.
<br/>

![Screenshot_5](https://user-images.githubusercontent.com/78226423/210456303-2c421dbb-0a9c-4570-afe2-7e68a7041f48.png)
<br>
<br>
<br>

Finally, we input Netflix's old Tweet `önerdiğim diziyi izledin mi diyorum bana nau nau diyor` into our project, and it gives us the following results.
<br/>

```
* Acun Ilıcalı: %0.56
* Rasim Ozan Kütahyalı: %6.95
* Webtekno: %4.92
* Netflix: %87.57
```
