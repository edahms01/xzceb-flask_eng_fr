'''
This translates stuff.
'''

#import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

#CONNECT
authenticator = IAMAuthenticator('5_Vc93y4c-6dkykFGMDvXKS5fRbfkdbFyx73T23KxOkf')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6899767b-2961-45dc-a1fa-0dbeed13fee8')


#FUNCTIONS DEF
def english_to_french(english_text):
    '''Takes in English and translates to French.'''

    try:
        translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()

        tr_x = translation.get('translations')
        tr_w = tr_x[0]
        tr_z = tr_w.get('translation')

        print(tr_z)
        return tr_z
    except:
        print('No result')


def french_to_english(french_text):
    '''Takes in French and translates to English.'''
    try:
        translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()

        tr_x = translation.get('translations')
        tr_w = tr_x[0]
        tr_z = tr_w.get('translation')

        print(tr_z)

        return tr_z
    except:
        print('No result')


#english_text = 'hello'
#english_to_french(english_text)

#french_text = 'bonjour'
#french_to_english(french_text)
