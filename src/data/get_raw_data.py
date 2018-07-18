import os
from dotenv import find_dotenv,load_dotenv
from requests import session
import logging
payload = {
    'action':'login',
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password':os.environ.get("KAGGLE_PASSWORD")
}

def extract_data(url,file_path):
    with session() as c:
        c.post('https://www.kaggle.com/account/login',data=payload)
        with open(file_path,'wb') as handle:
            response = c.get(url,stream=True)
            for block in response.iter_content(1024):
                handle.write(block)
                
                

def main(project_dir):
    logger=logging.getLogger(__name__)
    logger.info('getting raw data')
    
    train_url='https://storage.googleapis.com/kaggle-competitions-data/kaggle/3136/train.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1531812697&Signature=MSOPySFTrgAMb9d0AjezY0sVQTC3SctlqKJAZEkSofRwf%2Bxs2N1Y4n3%2BbHwCb9g7BdydDGA%2BmbPL9E66ox0iPYSppoNHRgHEaKljrOzqykWPJyUZ0i8x%2FQl78iWXcMvEwx9IVlzqv1DwZPy%2FpPZgSpvo70QQi61BTyjijXEdm9msXJ0i5kFxpA%2BZzlx5Q8vrzFgXQZQCmxyzbUqZUA0Sd7jjTwSMd1qvtZiePQXrrbk88YUiHPS9V%2Fibqwk6QpedOYgdbW4%2FdGliLLQF6n2I8AWRhljmPn2AcKVbm74buGF5GeMUN7AadpbhvoxXbZP9DqT7eGqEAoWWsbHjU16liA%3D%3D'
    test_url='https://storage.googleapis.com/kaggle-competitions-data/kaggle/3136/test.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1531812601&Signature=K61giqhHSRDGY0lsI7O9eJ5rNgS0DWW4mhj6l2%2FmqIe3pmt9eJeC9gAPkxzdZNTe5krl3EdHpu7k%2FqSEwiI9K0ATcX7kIKI2iMf0NbBfSqxplrFl5AJqUt2bH0sP5VMTMk%2FuSvIjhG1HmZ94LLaSl3pW12gBL7MixN0DmKo%2FTadH4Yg0fw8RPg6aMe0mfBVqsDfcZGUGrdPvKC4JPT1b7nIjmzWX2oc6zHdvIUfS4alVJPl6jpdPqePhpL9ILvnwJiduyA9591EeJ4rc8RpjHyTxRit9xyGfGtbltEVS%2B3Gsg5WTtDtVdVa24Qz53Jh2IjgVv0LZfyyER6381hB4jg%3D%3D'
    
    raw_data_path = os.path.join(project_dir,'data','raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')
    
    extract_data(train_url,train_data_path)
    extract_data(test_url,test_data_path)
    logger.info('downloaded raw training & test data')
    
if __name__ == '__main__':
    project_dir=os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)
    log_fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,format=log_fmt)
    dotenv_path=find_dotenv()
    load_dotenv(dotenv_path)
    main(project_dir)
    