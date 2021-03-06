# -*- coding: UTF-8 -*- 
from os.path import dirname

# --------- #
#   API     #
# --------- #
access_key = '626b1fe5c1df4a878c91949aafba7f59'
access_sercet = '4127670dfbfa4fa791b4a5c4bb6bad69'
base_url = 'http://webapi.cninfo.com.cn'

# --------- #
#   Cache   #
# --------- #
# Cache file root path.
cache_root_path = dirname(dirname(__file__)) + '\\cache\\'
# Cache switch 
enable_cache = True
# Access token cache file name
token = 'token'
# Industry classification cache file name
cache_industry = 'industry_class'
# Region classification cache file name
cache_region = 'region_class'

# --------- #
#   Log     #
# --------- #
# Log file path
log_path = dirname(dirname(__file__))+'\\log\\log'
log_out = True

