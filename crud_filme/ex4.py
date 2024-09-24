import banco

if __name__ == "__main__":
    filme = {"titulo": "The Immitation Game",
             'diretor': 'Morten Tyldum',
             'atores': 'Benedict Cumberbatch, Keira Knightley e Matthew Goode',
             'nota': 9.1,
             'id': 1,
             'estudio': 'Black Bear Pictures',
             'data': '28-9-2014',
             'sinopse': '''Em 1939, a recém-criada agência de inteligência britânica MI6 recruta Alan Turing, um aluno da Universidade de Cambridge, para entender códigos nazistas, incluindo o "Enigma", que criptógrafos acreditavam ser inquebrável. A equipe de Turing, incluindo Joan Clarke, analisa as mensagens de "Enigma"'''
            }
    banco.atualiza_filme(filme)
    