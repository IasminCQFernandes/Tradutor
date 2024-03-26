from googletrans import Translator

# detectar idioma
translator = Translator()

text = 'bom dia'


def deteccao(txt):
    idioma = translator.detect(txt)
    print(idioma)
    return idioma
    
deteccao(text)

idioma_desejado = 'en'

def traduzir(txt):
    try:
        traducao = translator.translate(txt, dest=idioma_desejado).text
        print(traducao)
        return traducao
    
    except:
        print('Erro na tradução')
        
    
traduzir(text)