
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
Từ bộ dữ liệu Daily Financial News for 6000+ Stocks([Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests))  :   
    
-   Lọc các tiêu đề bài báo từ năm 2014 đến năm 2015. 
-   Lọc các tiêu đề bài báo không đủ dữ kiện (NULL, NAN)
-   Lọc các cổ phiếu có ít tiêu đề bài báo(<=24).
Gộp thông tin giá cổ phiếu từ bộ dữ liệu Huge Stock Market Dataset([Kaggle](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)) với dữ liệu tiêu đề bài báo theo : 

-   Date
-   Stock



Yêu cầu bài toán là phân tích xu hướng của cổ phiếu. Do đó để đơn giản hóa bài toán, ta sẽ đưa bài toán về dạng phân loại. Ta sẽ cần các thông tin :

-   News headlines
-   Trend (Up/Down) : Xu hướng của cổ phiếu trong ngày hôm đó. Với :

        Trend = “Up” if (Close Price of Stock – Open Price of stock) > 0 else “Down”

### 2. Training model [(Colab)](https://colab.research.google.com/drive/1gfu4gA9XeqTKWVjxvCsKVZdMJinoFvto?usp=sharing)

Fine-tuning BERT với Pytorch và sử dụng pre-trained “bert-base-uncased” để huấn luyện mô hình phân loại.

### 3. Create Simple API [(Github)](https://github.com/DuyLocHoang/stocktrendprediction/blob/master/run.py)
Tạo 1 api đơn giản sử dụng FastAPI. Đầu vào gồm tiêu đề văn bản. Đầu ra bao gồm tiêu đề văn bản và xu hướng của cổ phiếu.

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
Traing với 30000 news headlines, 3 epochs. Kết quả thu nhận được có kết quả rất thấp.
- Accuracy: 0.53
- Average training loss: 0.69
- Validation Loss: 0.69


Ta tiến hành xử lý, cải thiện dữ liệu training, loại bỏ các thông tin không cần thiết trong news headlines [(Github)](https://github.com/DuyLocHoang/stocktrendprediction/blob/master/Data/prepare_data_2.py):
- Loại bỏ các những ký tự đặc biệt và số chỉ giữ lại [a-zA-Z]
- Loại bỏ stop words

Before :
```bash
Glenview Shows New ~4.6M Share Stake in Agilent Tech
```
After :
```bash
Glenview Shows New Share Stake Agilent Tech
```


Tuy nhiên do thời gian có hạn nên em chỉ mới xử lý dữ liệu và chưa thể training để biết được kết quả liệu có cải thiện.

## References
- https://arxiv.org/ftp/arxiv/papers/1607/1607.01958.pdf
- https://www.tutorialspoint.com/python/python_reg_expressions.htm
- https://github.com/huggingface/transformers/tree/5bfcd0485ece086ebcbed2d008813037968a9e58#quick-tour-of-the-fine-tuningusage-scripts
.
