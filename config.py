from authomatic.providers import oauth2

CONFIG = {
  'fb': {
      'class_': oauth2.Facebook,
      'consumer_key': '293720280981026',
      'consumer_secret': '8ca2c045bfef4952870eb902a20d4862',
      'scope': ['user_about_me', 'email', 'read_stream']
  }
}