from preprocessing import get_feats
import pandas as pd

def build_df(df):
    df_full = pd.DataFrame(columns=['https', 'len_url', 'have_host_name', 'have_ip', 'special_chars',
       'digits', 'letters', 'letters_to_digits', 'netloc_length',
       'char_to_len'])
    
    for i, r in df.iterrows():

        temp = get_feats(r['url'])

        df_full = pd.concat([df_full, temp], axis=0)
    
    df_full['labels'] = df['labels']
    return df_full



def predict_url(url: str, model) -> str:
    pred = model.predict(get_feats(url)).item()
    return 'safe' if pred == 0 else 'PHISHING'