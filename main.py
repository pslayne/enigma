from modules import crypto, steg
import cv2 as cv
import numpy as np

lena = cv.imread('./images/lena_cor.jpg')
lena_pgm = cv.imread('./images/lena.pgm', -1)
images = [lena_pgm, lena]

hello = 'hello, world!'
pridenprejudice = 'É uma verdade universalmente reconhecida que um homem solteiro e muito rico deve precisar de uma esposa'
dune = 'É no início que se deve tomar, com máxima delicadeza, o cuidado de dar às coisas sua devida proporção. Disso toda irmã Bene Gesserit sabe. Portanto, para começar a estudar a vida de Muad\'Dib, tome o cuidado de primeiro situá-lo em sua época: nascido no 57° ano do imperador padixá Shaddam IV. E tome o cuidado mais que especial de colocar Muad\'Dib em seu devido lugar: o planeta Arrakis. Não se deixe enganar pelo fato de que ele nasceu em Caladan e ali viveu seus primeiros 15 anos. Arrakis, o planeta conhecido como Duna, será sempre o lugar dele.'
lightningthief = 'Eu não queria ser um meio-sangue.\nSe você está lendo isto porque acha que pode ser um, meu conselho é o seguinte: feche este livro agora mesmo. Acredite em qualquer mentira que sua mãe ou seu pai lhe contou sobre seu nascimento, e tente levar uma vida normal.\nSer meio-sangue é perigoso. É assustador. Na maioria das vezes, acaba com a gente de um jeito penoso e detestável.\nSe você é uma criança normal, que está lendo isto porque acha que é ficção, ótimo. Continue lendo. Eu o invejo por ser capaz de acreditar que nada disso aconteceu. Mas, se você se reconhecer nestas páginas - se sentir alguma coisa emocionante lá dentro -, pare de ler imediatamente. Você pode ser um de nós. E, uma vez que fica sabendo disso, é apenas uma questão de tempo antes que eles também sintam isso, e venham atrás de você.\nNão diga que eu não avisei.\nMeu nome é Percy Jackson.\nTenho doze anos de idade. Até alguns meses atrás, era aluno de um internato, na Academia Yancy, uma escola particular para crianças problemáticas no norte do estado de Nova York.\nSe eu sou uma criança problemática? Sim. Pode-se dizer isso.\nEu poderia partir de qualquer ponto da minha vida curta e infeliz para prová-lo, mas as coisas começaram a ir realmente mal no último mês de maio, quando nossa turma do sexto ano fez uma excursão a Manhattan - vinte e oito crianças alucinadas e dois professores em um ônibus escolar amarelo indo para o Metropolitan Museum of Art, a fim de observar velharias gregas e romanas.\nEu sei, parece tortura. A maior parte das excursões da Yancy era mesmo. Mas o Sr. Brunner, nosso professor de latim, estava guiando essa excursão, assim eu tinha esperanças.\nO Sr. Brunner era um sujeito de meia-idade em uma cadeira de rodas motorizada. Tinha o cabelo ralo, uma barba desalinhada e usava um casaco surrado de tweed que sempre cheirava a café. Talvez você não o achasse legal, mas ele contava histórias e piadas e nos deixava fazer brincadeiras em sala. Também tinha uma impressionante coleção de armaduras e armas romanas, portanto era o único professor cuja aula não me fazia dormir.\nEu esperava que desse tudo certo na excursão. Pelo menos tinha esperança de não me meter em encrenca dessa vez.\nCara, como eu estava errado.\nEntenda: coisas ruins me acontecem em excursões escolares. Como na minha escola da quinta série, quando fomos para o campo de batalha de Saratoga, e eu tive aquele acidente com um canhão da Revolução Americana. Eu não estava apontando para o ônibus da escola, mas é claro que fui expulso do mesmo jeito.\nE antes disso, na escola da quarta série, quando fizemos um passeio pelos bastidores do tanque dos tubarões do Mundo Marinho, e eu de, alguma forma, acionei a alavanca errada no passadiço e nossa turma tomou um banho inesperado. E antes disso... Bem, já dá para você ter uma ideia.\nNessa viagem, eu estava determinado a ser bonzinho.\nAo longo de todo o caminho para a cidade aguentei Nancy Bobofit, aquela cleptomaníaca ruiva e sardenta, acertando a nuca do meu melhor amigo, Grover, com pedaços de sanduíche de manteiga de amendoim com ketchup.\nGrover era um alvo fácil. Ele era magrelo. Chorava quando ficava frustrado. Devia ter repetido de ano muitas vezes, porque era o único na sexta série que tinha espinhas e uma barba rala começando a nascer no queixo. E, ainda por cima, era aleijado. Tinha um atestado que o dispensava da Educação Física pelo resto da vida, porque tinha algum tipo de doença muscular nas pernas. Andava de um jeito engraçado, como se cada passo doesse, mas não se deixe enganar por isso. Você precisa vê-lo correr quando era dia de enchilada na cantina.\nDe qualquer modo, Nancy Bobofit estava jogando bolinhas de sanduíche que grudavam no cabelo castanho cacheado dele, e ela sabia que eu não podia revidar, porque já estava sendo observado, sob o risco de ser expulso. O diretor me ameaçara de morte com uma suspensão "na escola" (ou seja, sem poder assistir às aulas, mas tendo de comparecer à escola e ficar trancado numa sala fazendo tarefas de casa) caso alguma coisa ruim, embaraçosa ou até moderadamente divertida acontecesse durante a excursão.'
messages = [hello, pridenprejudice, dune, lightningthief]

for img in images:
    cv.imshow('original', img)
    print(f'\nmax size for this image = {steg.get_max_size(img.shape)}')
    cv.waitKey()
    i = 1 
    for msg in messages:
        enc = crypto.encrypt(msg)
        steg_img = steg.hide(img, enc)
        cv.imshow(f'message - {i}', steg_img)
        cipher_msg = steg.reveal(steg_img)
        plain_msg = crypto.decrypt(cipher_msg)
        print(f'message - {i}')
        print('-----------------------------')
        print(f'cipher_msg -> {cipher_msg}')
        print(f'plain_msg -> {plain_msg}')
        i += 1
        cv.waitKey()
    cv.destroyAllWindows()

