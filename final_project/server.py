from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask('Web Translator')

@app.route('/')
def renderIndexPage():
    return render_template('index.html')


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    e
    english_to_french()

    return "Translated text to French"
    


'''
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    
    #frenchtext = textToTranslate
    #french_to_english(textToTranslate)

    return "Translated text to English"
    print(tr_z)
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
