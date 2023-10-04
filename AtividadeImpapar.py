jogador1=0
jogador2=0
empate=0
for x in range (3):
  player1=input("Jogador 1, pedra,papel e tesoura:")
  player2=input("Jogador 2, sua vez! pedra papel e tesoura:")
  print()
  if player1 == player2:
      print(f"Ambos efetuaram o lançamento de {player1}, ou seja, empate!")
      empate+=1
  elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel"):
      print("Jogador1 venceu a rodada!")
      jogador1+=1
  else: 
     print("jogador2 venceu a rodada!")
     jogador2+=1
if (empate>=jogador1 and empate>=jogador2):
    print("partida empatada, por favor tentem novamente!")
else:
    if jogador1>=jogador2:
       print("Jogador1 venceu a partida,parabéns ＼⁠(⁠°⁠o⁠°⁠)⁠／!")
    else: 
       print("Jogador2 venceu a partida, GGWP (⁠ﾉﾟ⁠0ﾟ⁠)⁠ﾉ⁠~")