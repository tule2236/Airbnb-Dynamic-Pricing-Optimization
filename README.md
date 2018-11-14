# Twitter-and-ClickStream-analysis-with-SparkStreaming
Analyze streaming tweets and clickstream data in real-time with Spark Streaming, Spark SQL, and Spark MLLib.

### Analyze streaming tweets in real-time
Important Code files Directory
```
TwitterStream_Analysis/
    scr/
        com/
            tule/
                sparkstreaming/
                    AverageTweetLength.scala
                    PopularHashtags.scala
                    PrintTweets.scala
                    SaveTweets.scala
```

### Analyze logging Clickstream data in real-time
Important Code files Directory
```
ClickStream_Analysis/
    scr/
        com/
            tule/
                sparkstreaming/
                    LogAlarmer.scala
                    LogParser.scala
                    LogSQL.scala
                    Sessionizer.scala
                    StructuredStreaming.scala
```
### Machine Learning in Spark Streaming
#### 1. Unsupervised Learning
```
MLLib_Spark_Streaming/
    Streaming_KMeans/
        scr/
            com/
                tule/
                    sparkstreaming/
                        StreamingKMeans.scala
                        kmeans-train.txt
                        kmeans-test.txt
```
#### 2.Regression
```
 Streaming_Linear_Regression/
        scr/
            com/
                tule/
                    sparkstreaming/
                        StreamingRegression.scala
                        regression.txt