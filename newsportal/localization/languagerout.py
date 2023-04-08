from newsportal.localization.ENG import *
from newsportal.localization.RUS import *

from django.conf import settings

class Language():
    if settings.LANGUAGE_CODE == 'en-us':
        news = ENG.News
    else:
        news = RUS.News