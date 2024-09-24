import banco
import datetime

lista = [
    ['ET O Extraterrestre', 'Steven Spielberg', 
     'Drew Barrimore e Peter Coyote', datetime.datetime(1982, 12, 25),
     'Universal Studios', 7.9, '''O garoto Elliott faz amizade com 
     um pequeno alienígena inofensivo que está bem longe do seu 
     planeta. Ele decide manter a adorável criatura em segredo e em 
     casa após apresentá-la aos irmãos.'''],

     ['Uma mente brilhante', 'Ron Howard', 
      'Russel Crowe e Jennifer Connely', datetime.datetime(2002, 2, 15),
      'Dreamworks', 8.4, '''John Forbes Nash Jr. é reconhecido como 
      gênio da matemática aos 21 anos. Cedo, casa-se com uma bela 
      mulher, mas logo começa a dar sinais de esquizofrenia. Após 
      anos de luta contra a doença, ele acaba ganhando o prêmio 
      Nobel'''],

      ['Estrelas Além do Tempo', 'Theodore Melfi', 
       'Octavia Spencer e Kevin Costner', datetime.datetime(2017, 2, 2),
       'Fox', 8.8, '''No auge da corrida espacial travada entre 
       Estados Unidos e Rússia durante a Guerra Fria, uma equipe de 
       cientistas da NASA, formada exclusivamente por mulheres 
       afro-americanas, provou ser o elemento crucial que faltava na 
       equação para a vitória dos Estados Unidos, liderando uma das 
       maiores operações''']
]

for linha in lista:
    movie = {'titulo': linha[0],
             'diretor': linha[1],
             'atores': linha[2],
             'data_lancamento': linha[3],
             'estudio': linha[4],
             'nota': linha[5],
             'sinopse': linha[6]}
    banco.insere_filme(movie)
    