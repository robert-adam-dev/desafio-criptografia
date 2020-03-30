
class Criptografia:

    import requests
    import json
    import hashlib


    # Criando uma variável com a URL do desafio
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=OMITIDO'

    # URL destino

    url_destino = \
        'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=OMITIDO'

    # Fazendo um get do arquivo json

    r = requests.get(url)

    # Salvando em um arquivo chamado answer.json
    with open('answer.json', 'wb') as f:
        f.write(r.content)
        f.close()

        arquivo_json = open('answer.json', 'r', encoding='utf-8')
        dados_json = json.load(arquivo_json)

        numero_de_casas = dados_json['numero_casas']
        texto_cifrado = dados_json['cifrado']
        list_texto_decifrado = []

        for char in texto_cifrado:

            letra_atual = ord(char)
            letra_decifrada = letra_atual - numero_de_casas
            letra_correta = chr(letra_decifrada)

            if not char.isspace():
                if char == 'a':
                    list_texto_decifrado.append('x')
                elif char == '.':
                    list_texto_decifrado.append('.')
                else:
                    list_texto_decifrado.append(letra_correta)
            else:
                list_texto_decifrado.append(chr(letra_atual))

        str_texto_decifrada = ''.join(map(str, list_texto_decifrado))

        dados_json['decifrado'] = str_texto_decifrada

        a_file = open('answer.json', "w")
        json.dump(dados_json, a_file)
        a_file.close()

        resumo = hashlib.sha1(str_texto_decifrada.encode('utf-8')).hexdigest()
        dados_json['resumo_criptografico'] = resumo

        b_file = open('answer.json', "w")
        json.dump(dados_json, b_file)
        b_file.close()

        files = {'answer': open('answer.json', 'rb')}
        s = requests.post(url_destino, files=files)
        print(s.text)

        arquivo_json.close()

