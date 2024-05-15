from urllib.parse import urlparse
def get_protocol(url: str) -> str:
  from urllib.parse import urlparse
  parsed_url = urlparse(url)
  return parsed_url.scheme == 'https'


def have_host_name(url: str) -> int:
    from urllib.parse import urlparse 
    hostname = urlparse(url).hostname
    # print(f'hostname:{hostname} ')
    if hostname:
        return 1
    else:
        return 0
    
def has_ip_address(url):
    import re
    # Regular expression pattern to match IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    # Check if the URL contains an IP address
    if re.search(ip_pattern, url):
        return 1
    else:
        return 0
  

def spec_car_count(url: str) -> int:
    sp_c = ['@','?','-','=','.','#','%','+','$','!','*',',','//']
    num_chars = sum([url.count(char)  for char in sp_c ])
    return num_chars

def digit_count(URL: str) -> int:
    digits = 0
    for i in URL:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letters_count(URL: str) -> int:
    alphas = 0
    for i in URL:
        if i.isalpha():
            alphas = alphas + 1
    return alphas



def netloc_length(url):
    parsed_url = urlparse(url)
    netloc_length = len(parsed_url.netloc)
    return netloc_length

def letters_to_digits(df):
    df['letters_to_digits'] = (df['letters'] + 1) / (df['digits'] + 1)
    return df

def spec_to_len(df):
  df['spec_to_len'] = df['special_chars'] / df['len_url']
  return df