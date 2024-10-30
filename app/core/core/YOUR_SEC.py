# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'PASTE_YOUR_DJANGO_SECRET_KEY_HERE'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Production status (options: 'live' and 'dev')
production_status = 'dev' if DEBUG == True else 'live'

# Tracking post portal url configure
tracking_url = "https://post.gov"

# Media forlder path configure
media_dir = "/home/public/media/post_tracker"

# Sms api key configure
SMS_API = 'YOUR_SEC_KEY'

# Woocommerce api key configure
WC_API = API(
    url="YOUR_SEC_KEY",
    consumer_key="YOUR_SEC_KEY",
    consumer_secret="YOUR_SEC_KEY",
    version="wc/v3"
)
