# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
ALLOWED_HOSTS = ['', '']

# Production status (options: 'live' and 'dev')
production_status = 'dev'

# Tracking post portal url configure
tracking_url = "https://post.gov"

# Sms api key configure
SMS_API = ''

# Woocommerce api key configure
from woocommerce import API
WC_API = API(
    url="https://Example.com",
    consumer_key="",
    consumer_secret="",
    version="wc/v3"
)

