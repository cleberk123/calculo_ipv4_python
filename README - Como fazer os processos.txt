1° Converter números decidmais do IP para binário

    IP que iremos converter é 10.20.12.45
    Separar o em 4 grupos pelo pontos.
    Defina esses números primeiro (128  64  32  16  8  4  2  1):
                 
                 128  64  32  16  8  4  2  1
                   0   0   0   0  1  0  1  0 

    No 1° grupo que é 10. Perguntamos: Qual número da tabela que se aproxima de 10 ou é igual a 10?
    No caso aqui será 8. Então vamos por número 1 a baixo o número 8 na tabela.
    Agora indo para direita na tabela.
    Perguntamos: Qual o número somado com 8 que dará 10 ou aproxima de 10?
    No caso do 4+8=12, irá passar e então embaixo do 4 na tabela coloca 0, pois, passou de 10.
    Já 8+2 é igual a 10, então embaixo do 2 na tabela coloca 1.
    E no último pode por 0, pois, já deu 10.
    Por fim completamos os números da esquerda com 0.
    Fim do 1º grupo que é 10. Temos então 10 em binário 00001010. 

    Agora Vamso converter o 2º grupo que é 20.
    Defina esses números novamente e faça a mesma coisa de antes:

                 128  64  32  16  8  4  2  1
                   0   0   0   1  0  1  0  0 

    Perguntamos: Qual número que aproxima ou é igual a 20?
    Aqui na tabela será 16. Então põe 1 a baixo de 16.
    Para resumirmos: Qualquer número a direita somado com 16 que seja igual a 20 ou aproxima de 20 será 1
    se passar de 20 será 0 e se der 20, então certo, atingimos o que queríamos e assim os restantes na direita e na esquerta serão 0.
    Temos então 20 em binário: 00010100

    Vamos converter o 3º grupo que é 12.
    Defina esses números novamente e faça a mesma coisa de antes:

                 128  64  32  16  8  4  2  1
                   0   0   0   0  1  1  0  0

    Perguntamos: Qual número que aproxima ou é igual a 12?
    Aqui na tabela será 8. Então põe 1 a baixo de 8.
    Para resumirmos: Qualquer número a direita somado com 8 que seja igual a 12 ou aproxima de 12 será 1
    se passar de 12 será 0 e se der 12, então certo, atingimos o que queríamos e assim os restantes na direita e na esquerta serão 0.
    Temos então 12 em binário: 00001100

    Vamos converter o 4º grupo que é 45.
    Defina esses números novamente e faça a mesma coisa de antes:

                 128  64  32  16  8  4  2  1
                   0   0   1   0  1  1  0  1 

    Perguntamos: Qual número que aproxima ou é igual a 45?
    Aqui na tabela será 32. Então põe 1 a baixo de 32.
    Para resumirmos: Qualquer número a direita somado com 32 que seja igual a 45 ou aproxima de 45 será 1
    se passar de 45 será 0 e se der 45, então certo, atingimos o que queríamos e assim os restantes na direita e na esquerta serão 0.
    Temos então 45 em binário: 00101101

    Resumo do 1º tópipo:
    10 = 00001010
    20 = 00010100
    12 = 00001100 
    45 = 00101101

2º - Definir a Mascara de Sub Rede
    Suponhamos que seja /26 a máscara de sub rede.
    Ou seja, está sendo de 26 bits então.

    Temos que colocar 26 sequência de 1 embaixo dos binário definidos e os que falta a ser preenchido ficará como 0, então,
    ficará assim:
    10          20          12          45       - IP decimal
    00001010    00010100    00001100    00101101 - IP binário
    11111111    11111111    11111111    11000000 - Bits da mascara de sub rede /26

3º Quantidade de Hosts que teremos para essa rede.
    A quantidade de zero que deu na máscara de sub rede, usaremos como B dentro da fórmula (2^b-2 = hosts):
    2^b-2 (-2 devido ao IP da Rede e Broadcast) = Hosts
    Temos então 2^6 - 2 = 62
    Podemos ter 62 IPs válido dentro dessa rede!

4º Transformar os bits da máscara em Decimal
    Utilizaremos a tabela de 128 a 1 novamente e a onde tiver 1 embaixo da tabela, iremos somar com o outro número
    que tiver 1 abaixo dele mesmo, ou seja, pegaremos o primeiro octeto ali dos 26 bits que são 11111111...
    Ficará assim então:

        128  64  32  16  8  4  2  1    128  64  32  16  8  4  2  1    128  64  32  16  8  4  2  1    128  64  32  16  8  4  2  1
         1    1   1   1  1  1  1  1     1    1   1   1  1  1  1  1     1   v1   1   1  1  1  1  1     1    1   0   0  0  0  0  0
        Significa então que iremos somar 128+64+32+16+8+4+2+1 = 255 e a onde for 0 não soma.
        Teremos então:

            10          20          12          45       - IP decimal
            00001010    00010100    00001100    00101101 - IP binário
            255         255         255         192      - Mascara de sub rede /26 em decimal

5º Saber o IP da Rede (primeiro IP) e Broadcast (último IP)
    Iremos reescrever os bits do IP de entrada que tivemos.
    Teremos nesse momento essa tabela.
        10          20          12          45
    00001010    00010100    00001100    00101101
       255         255         255         192     
    00001010    00010100    00001100    00000000 (No caso aqui nós mantemos os 0 dos hosts)

    Iremos converter esses bits do IP de entrada para decimal, teremos:
    10          20          12          45
    00001010    00010100    00001100    00101101
    255         255         255         192     
    00001010    00010100    00001100    00000000
    10          20          12          0         /26 (Devido mantermos os 0 dos hosts, o último acabou sendo 0)

    Temos então o primeiro IP da rede que é 10.20.12.0

    Para saber o Broadcast (último IP da rede) iremos pegar
    os bits do IP de entrada com os 0 dos hosts da tabela a cima e iremos substituir
    os 0 dos hosts por 1.
    Teremos agora:

    10          20          12          45
    00001010    00010100    00001100    00101101
    255         255         255         192     
    00001010    00010100    00001100    00000000
    10          20          12          0        
    00001010    00010100    00001100    00111111 <<-- aqui substituímos os 0 por 1

    Pegaremos o último octeto(00111111) e colocamos a baixo da tabela de cálculo de decimal para binário e iremos fazer o cálculo.

    128 64 32 16 8 4 2 1
      0  0  1  1 1 1 1 1

    Somamos então 32+16+8+4+2+1 = 63

    Teremos então o Broadcast
    10          20          12          45       - IP de entrada
    00001010    00010100    00001100    00101101 - IP convertido para binário
    255         255         255         192      - Mascara de Sub Rede
    00001010    00010100    00001100    00000000 - Hosts - 2^b-2 = Hosts
    10          20          12          0        - IP da Rede
    00001010    00010100    00001100    00111111 - Hosts convertido para 1 para cálculo do Broadcast
    10          20          12          63       - Broadcast 

Resumo:

IP de entrada: 10.20.12.45/26
Rede: 10.20.12.0/26
Broadcast: 10.20.12.63/26
Máscara: 255.255.255.192
Primeiro IP válido: 10.20.12.1/26
Último IP válido: 10.20.12.62/26
Nº de IPs válidos: 62