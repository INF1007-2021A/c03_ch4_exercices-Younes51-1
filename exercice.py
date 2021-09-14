#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    nb_de_caractere=len(string)
    if nb_de_caractere % 2==0 :
         parity=True
    else :
         parity=False
    return parity


def remove_third_char(string: str) -> str:
    nouveau =""
    for i in range(len(string)):
        if i!=2 :
         nouveau += string[i]
    return nouveau


def replace_char(string: str, old_char: str, new_char: str) -> str:
   nouveau =""
   for i in range(len(string)) :
       if old_char==string[i] :
        nouveau += new_char
       else:
        nouveau += string[i]
   return nouveau

def get_nb_char(string: str, char: str) -> int:
    nb_d_occurence=0
    for i in range(len(string)) :
        if char== string [i] :
            nb_d_occurence +=1
    return nb_d_occurence


def get_nb_words(sentence: str) -> int:
    nb_de_mots=1
    for i in range(len(sentence)) :
        if sentence[i]==" " :
            nb_de_mots +=1
    return nb_de_mots


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
