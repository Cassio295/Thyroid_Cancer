# 1. Crie uma variável com a string “ instituto de ciências matemáticas e de computação” e faça:
string = ' Instituto  de ciências matéticas e de computação'
# a. Concatene (adicione) uma outra string chamada “usp”
string + 'usp' 
# b. Concatene (adicione) uma outra informação: 2021
string + '2021'
# c. Verifique o tamanho da nova string (com as informações adicionadas
print(len(string))
# das questões a e b), com referência a caracteres e espaços
# d. Transforme a string inteiramente em maiúsculo
print(string.upper())
# e. Transforme a string inteiramente em minúsculo
print(string.lower())
# f. Retire o espaço que está no início da string e imprima a string
print(string.split())
# g. Substitua todas as letras ‘a’ por ‘x’
teste = string.replace('a', 'x')
print(teste)
# h. Separe a string em palavras únicas
separado = string.split()
print(separado)
# i. Verifique quantas palavras existem na string
print(len(separado))
# j. Separe a string por meio da palavra “de”
de = string.split("de")
print(de)
# k. Verifique agora quantas palavras/frases foram formadas quando houve
# a separação pela palavra “de”
print(len(de))

# l. Junte as palavras que foram separadas (pode usar a separação resultante
# da questão h ou j)
print(" ".join(de))

# m. Junte as palavras que foram separadas, mas agora separadas por uma
# barra invertida, não por espaços (pode usar a separação resultante da questão h ou j)
print("/".join(de))