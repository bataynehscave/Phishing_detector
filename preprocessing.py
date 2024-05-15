from feature_engineering import * 
import pandas as pd


def get_feats(url: str, url_len = True) -> pd.DataFrame:
    protocol = (get_protocol(url) == 'https')
    url_len = len(url)
    host_name = have_host_name(url)
    ip = has_ip_address(url)
    special_chars = spec_car_count(url)
    digits = digit_count(url)
    letters = letters_count(url)
    let_to_digs = (letters + 1) / (digits + 1)
    netloc_len = netloc_length(url)
    specials_to_len = (special_chars + 1) / (url_len + 1)
    

    return pd.DataFrame({
        'https': [protocol],
        'len_url': [url_len],
        'have_host_name': [host_name],
        'have_ip': [ip],
        'special_chars': [special_chars],
        'digits': [digits],
        'letters': [letters],
        'letters_to_digits': [let_to_digs],
        'netloc_length' : [netloc_len],
        'char_to_len': [specials_to_len]
        
    })