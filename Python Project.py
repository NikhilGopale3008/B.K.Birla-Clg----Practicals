import random
color  = ['red', 'yellow', 'orange', 'green', 'blue']
name = input('enter name: ')
win = 0
lose = 0
while True:
  try:
    rounds = int(input('enter no of rounds: \n'))
    comp = random.randint(1,5)   
    i=1   
    while i<=rounds:
      user = int(input('enter no between 1 to 5: \n'))
      if user > 5 or user < 0:
        print('enter no. in given range')
      if rounds < 0:
        print('enter correct no of rounds')
      if user < 1 or user >5:
        print('enter nos in range 1 to 5:')
        user = int(input('enter no between 1 to 5'))
      print(name, ':',user,' ', color[user-1])
      print('PC:',comp,' ', color[comp-1])
      print('\n')
      print('-------------score------------: ')
      if user == comp:
        win+=1      
        print(name, ':' , win, '\n PC:', lose)
      else:
        lose+=1
        print(name, ':' , win, '\n PC:', lose)
        i+=1
        print('-----------------------------')
    if win>lose:
      print('winner:', name)
    elif lose>win:
      print('winner: PC')
      print("\n")
    else:
      print('tie')
    play_again = input('Do you want to play again:')
    if play_again == 'no':
      print("Thank you")
      break
    else:
      i = 1
      win = 0
      lose = 0
  except Exception as e:
    print(e)
