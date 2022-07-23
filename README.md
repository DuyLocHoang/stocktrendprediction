
# Stock Trend Prediction Using News Headlines
Use natural-language processing (NLP) to predict trend stock based on news headlines

## Introduction
- Input : News Headline 
- Output : Trend of Stock

## Project Structure
```bash
├── Data
│   └── Datasets
│       ├── Stocks
│       └── analysis_ratings_processed.csv
├── weights
│   └── model30000
│ 
└── Utils
```

## Weights
- Download and store in weights folder
```bash
https://drive.google.com/file/d/1-0PntxoKlI4c5f9q5ZPsEyaoyT_sVwoW/view?usp=sharing
```

## Requirement
- Python 3.8
```bash
pip install -r requirements.txt
```


## Methodology

### 1. Prepare data [(Github)](https://github.com/DuyLocHoang/stocktrendprediction/blob/master/Data/prepare_data.ipynb)
From the Daily Financial News dataset for 6000+ Stocks([Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests))  :   
    
-   We will filter the news headlines from 2014 to 2015..
-   Filter news headlines with insufficient data (NULL, NAN)
-   Filter stocks with few article titles
Combine stock price information from the Huge Stock Market Dataset([Kaggle](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)) with news
headline data by:

-   Day, Month, Year
-   Stock



The problem required is to analyze the trend of stocks. Therefore, to simplify the
problem, we will reduce the problem to a categorical form. We will need the following
information:

-   News headlines
-   Trend (Up/Down) :  The stock's trend for that day

        Trend = “Up” if (Close Price of Stock – Open Price of stock) > 0 else “Down”

### 2. Training model [(Colab)](https://colab.research.google.com/drive/1gfu4gA9XeqTKWVjxvCsKVZdMJinoFvto?usp=sharing)

Fine-tuning BERT with Pytorch and using pre-trained “bert-base-uncased” to train the
classification model

### 3. Create Simple API [(Github)](https://github.com/DuyLocHoang/stocktrendprediction/blob/master/run.py)
Create a simple api using FastAPI. The input includes the news headline. The output includes news headline and stock trends.


## Usage
- Run in the terminal
```bash
python run.py
```
- Test it in browser :
```bash
http://localhost:8000/docs
```

## Results
Traing with 30000 news headlines, 3 epochs. The results obtained are very low.
- Accuracy: 0.53
- Average training loss: 0.69
- Validation Loss: 0.69


We improve the training data, remove unnecessary information in news headlines [(Github)](https://github.com/DuyLocHoang/stocktrendprediction/blob/master/Data/prepare_data_2.py):
- Remove special characters and keep only [a-zA-Z] [a-zA-Z]
- Remove stop words

Before :
```bash
Glenview Shows New ~4.6M Share Stake in Agilent Tech
```
After :
```bash
Glenview Shows New Share Stake Agilent Tech
```


However, due to limited time, I have only processed the data and cannot train to know
if the results have improved.

## References
- https://arxiv.org/ftp/arxiv/papers/1607/1607.01958.pdf
- https://www.tutorialspoint.com/python/python_reg_expressions.htm
- https://github.com/huggingface/transformers/tree/5bfcd0485ece086ebcbed2d008813037968a9e58#quick-tour-of-the-fine-tuningusage-scripts
.
