import random
# Fonction qui calcule le PGCD de 2 nombres / Vérifier et valide
def PGCD(a, b):
    r = 1
    if(a > b):
        tmp = a
        a = b
        b = tmp
    while(True):
        if(a % b == 0):
            return r
        else:
            r = a % b
            a = b 
            b = r
# Calcul l'inverse modulaire de 'e' modulo 'phi' / Vérifier et valide
def inverse_modulaire(e, phi):
    if(e % 10 == 0):
        print("Les nombres ne sont pas premiers entre eux !")
        return None
    for i in range(0, phi - 1):
        if(e * i % phi == 1):
            return i

# Vérifie si un nombre est premier / Vérifier et valide
def isPrime(q):
    for i in range(2, q - 1):
        if(q % i == 0):
            return False
    return True

# Genère un nombre premier aléatoire dans une plage / Vérifier et valide
def generate_prime_number(min, max):
    liste_prime = []
    for i in range (min, max):
        if(isPrime(i)):
            liste_prime.append(i)
    return liste_prime[random.randint(0, len(liste_prime))]

# Génèreu ne clé public et privée en fonction de 2 nombres premiers
def generate_public_and_private_key(p, q):
    n = p * q
    # Fonction d'Euler : indique le nombre d'entiers inférieurs qui sont inférieurs et premier avec n 
    phi = (p - 1) * (q - 1)

    for i in range(2, phi-1):
        if(PGCD(i, phi) == 1):
            e = i
            break

    d = inverse_modulaire(e, phi)
    # couple (e,n) -> clé publique ; couple (d,n) -> clé privée
    return (e, n), (d, n)

def chiffrer_message(cle: tuple[int, int], message_brut):
    e, n = cle
    ASCII_message = []
    for i in range(0, len(message_brut)):
        ASCII_message.append(ord(message_brut[i]))
    message_chiffre = []
    for i in range(0, len(ASCII_message)):
        message_chiffre.append(pow(ASCII_message[i], e) % n)
    return message_chiffre

def dechiffrer_message(cle: tuple[int, int], message_chiffre):
    d, n = cle
    message_dechiffre_ASCII = []
    for i in range(0, len(message_chiffre)):
        message_dechiffre_ASCII.append(pow(message_chiffre[i], d) % n)

    message_dechiffre = []
    for i in range(0, len(message_dechiffre_ASCII)):
        message_dechiffre.append(chr(message_dechiffre_ASCII[i]))

    return message_dechiffre

p = generate_prime_number(200, 1000)
q = generate_prime_number(300, 1000)
(e,n), (d, n) = generate_public_and_private_key(p, q)
message = "ici la terre comment allez vous"
message_chiffrer = chiffrer_message((e,n), message)
print(message_chiffrer)
print(dechiffrer_message((d, n), message_chiffrer))




