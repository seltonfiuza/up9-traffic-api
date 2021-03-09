import pandas as pd


def set_data_index(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp')
    return df


def filter_between_dates(df=None, start_date=None, end_date=None):
    if 'timestamp' in df and len(df['timestamp']) > 0:
        try:
            df = set_data_index(df)
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
            data = df[df['timestamp'].isin(pd.date_range(start_date, end_date))]
            return data
        except Exception as e:
            return {'err': e}
    