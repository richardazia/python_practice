from translate import Translator
translator= Translator(to_lang="fr")
translation = translator.translate("This is a pen.")

print(translation)