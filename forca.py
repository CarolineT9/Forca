import random

def sorteio():
  return random.choice(["amarelo", "amiga", "amor", "ave", "bala", "bela", "bolo", "branco",
     "cama", "caneca", "celular", "clube", "copo", "doce", "elefante", "escola",
     "estojo", "faca", "foto", "garfo", "geleia", "girafa", "janela", "limonada",
     "meia", "noite", "ovo", "pai", "parque", "passarinho", "peixe",
     "pijama", "rato", "umbigo"])

def forca(vidas):
  if vidas == 0:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')
  elif vidas == 1:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
  elif vidas == 2:
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
  elif vidas == 3:
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
  elif vidas == 4:
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
  elif vidas == 5:
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''')
  else:
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========
''')

# 1. Sorteia a palavra
palavra = sorteio()
print(palavra)

# 2. Gera uma palavra com _
tam = len(palavra)
adivinhada = "_" * tam # letras já adivinhadas
vidas = 6
letras = ""  # letras já escolhidas
#print(adivinhada)

jogoAtivo = True
# 3. Enquanto o jogo estiver ativo:
while jogoAtivo:

  # 4. Exibe estado do jogo
  print()
  forca(vidas)
  print(adivinhada)
  print()
  print(f"Letras já escolhidas: {letras}")

  # 5. Aguarda a digitação de uma letra válida (ainda não escolhida)
  valida = False
  while not valida:
    letra = input("Escolha uma letra: ")
    if letra not in letras:
      valida = True
    else:
      print("Esta letra já foi escolhida!")
  
  # Registra a letra digitada
  letras += letra

  # 6. Verifica se a letra está na palavra:
  if letra in palavra:
    # - Se estiver, troca os _
    for pos in range(tam):
      if letra == palavra[pos]:
        adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]
  else:
    # - Se não estiver, perde uma vida e verifica se o jogador perdeu
    print("Esta letra não está na palavra...")
    vidas -= 1
    if vidas == 0:
      forca(vidas)
      print("Infelizmente você perdeu...")
      jogoAtivo = False
  
  # 7. Verifica se o jogador ganhou
  if "_" not in adivinhada:
    print("Parabéns, você acertou!")
    jogoAtivo = False

# 8. Mostra a palavra sorteada
print(f"A palavra sorteada era {palavra}")