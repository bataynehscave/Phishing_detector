def get_protocol(url: str) -> str:
  from urllib.parse import urlparse
  parsed_url = urlparse(url)
  return parsed_url.scheme == 'https'