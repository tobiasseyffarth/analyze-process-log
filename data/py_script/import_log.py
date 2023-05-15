import pandas as pd
import pm4py

def get_Event_Log(path):
    df = pd.read_csv(path, sep=";")
    event_log = pm4py.format_dataframe(df, case_id='Case', activity_key='Event_Name', timestamp_key='Timestamp')
    event_log['time:timestamp'] = pd.to_datetime(event_log['time:timestamp'], format='%Y-%m-%dT%H:%M:%S.%Z')

    cleaned_log = event_log.copy()
    #colummns=['Case', '@@index', 'Event_ID', 'Event_Name', 'Timestamp', '@@case_index']
    #for column in colummns:
    #    cleaned_log.drop(column, inplace=True, axis=1)
    cleaned_log = cleaned_log[['case:concept:name','concept:name','time:timestamp','Device']]

    return cleaned_log