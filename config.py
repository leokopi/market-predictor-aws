# config file for data collection pipeline project
# keeping setting centralized for more maintainable code base

S3_BUCKET_NAME = "market-predictor-leo-2026"
# name of my s3 bucket
# thought of as my top level folder that holds all my project data
# globally unique
S3_RAW_DATA_PREFIX = "raw-data/"
# the path where raw uprocessed data is to be stored
# s3 doesn't have folders - prefixes
S3_PROCESSED_DATA_PREFIX = "processed-data/" 
# 'folder' path for analyzed within s3
# seperating raw and unprocessed data as a best practice


TICKERS = {
    "BTC-USD"
    "ETH-USD"
    "VOO"
    "QQQ"
    "SMH"
}
#list of ticker symbols i want to track, from yahoo finance

DATA_PERIOD = "1mo"
# 1 month is enough time to make some meaningful analysis
# doesn't hold too much data
# overall good balance