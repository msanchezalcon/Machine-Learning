
# Hate Speech Detection with Sentiment Analysis
 
 ## What is Sentiment Analysis?
 Sentiment Analysis refers to the use of Natural Language Processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Given a set of texts with an attached sentiment label, the goal of every sentiment analysis task is to predict the sentiment of a given text data.


 ## Problem Statement
 Our goal in this task is to detect hate speech in tweets. We can say a tweet contains hate speech or abusive language if it has a racist or sexist sentiment associated with it. So, the task is to separate racist or sexist tweets from other tweets. Given a training sample of tweets and labels, the label '0' denotes the tweet doesn't contain hate speech and the labels '1', '2' and '3' denote the tweet contain hate or abusive speech in different degrees, being 3 the highest. Our objective is to predict the labels on the test dataset.

  ## Motivation
  Unfortunately, hate speech is common on the Internet nowadays. Social media sites face the problem of identifying and censoring problematic posts while weighing the right to freedom of speech. Therefore, the importance of detecting and moderating hate speech is evident from the strong connection between hate speech and actual hate crimes. The early identification of users promoting hate speech could enable outreach programs that attempt to prevent an escalation from speech to action. These sites have been seeking to actively fight hate speech. Despite these reasons, NLP research on hate speech has been very limited, primarily due to the lack of a general definition of hate speech, an analysis of its demographic influences, and an investigation of the most effective features. Also the difficulty to come to an agreement when annotating hate speech (inter-annotator agreement).
  
  ## Data
  The dataset consists of a csv file with 25000 samples of annotated tweet data. We will process and split this unique file into three subsets: train, validation and test. Given the little amount of data in each remaining subset and the limited lenght of tweets, we already predict that using a neural network for this task won't retrieve the desired results.
  
  ## Pipeline
  We will use Long Short-Term Memory (LSTM). This approach is usually better than a standard RNN because they suffer from the vanishing gradient problem. The steps were initially defined as described below:
  
1. Removing entities (mentions and hashtags), links and tokenize data.
2. Packed padded sequences
3. Pre-trained word embeddings (glove)
4. Bidirectional RNN. The sentiment prediction is made using a concatenation of the last hidden state from the forward RNN - from final word of the sentence. The last hidden state from the backward RNN - obtained from the first word of the sentence.
5. Multi-layer RNN
6. Regularization (dropout). This regularization method works by randomly dropping out (setting to 0) neurons in a layer during a forward pass.
7. Adam optimizer. It adapts the learning rate for each parameter, giving parameters that are updated more frequently lower learning rates and parameters that are updated infrequently higher ones. 
8. Evaluation will be measured with binary accuracy per batch  
  
  ## Final Report
  The accuracy of the model is terrible. We already predicted this could happen, but the results are a disgrace.
  We understand the dataset was not optimal. Not enough tweets from the very beginning, and after splitting in three subsets the amunt was dramatically reduced as well. Given the nature of tweet data, the lenght is always very limited and therefore difficult to extract meaninful features from it.
  
  Initially, we thought of using pre-trained embeddings for the task (GloVe), but as we explained before there was not enough data for it, and the results would have been worse (although being worse is not mathematically possible).
  The features available are, in our opinion, not representative enough for the model to learn from them. Our attempts to fix the data made us modify the pre-processing functions multiple times, and even try different data sets, but the amount of tweets available were similar and no substancial changes were observed.
  
  We therefore conclude that a different method for this task is required, either using a less robust technique or providing the neural network with way more data so it can actually learn something.
  

