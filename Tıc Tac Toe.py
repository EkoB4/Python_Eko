Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> board = [[0,0,0],[0,0,0],[0,0,0]]
>>> m1=board[0]
>>> m2=board[1]
>>> m3=board[2]
>>> def game():
	print('',m1,'\n',m2,'\n',m3)
	print('TIC TAC TOE GAME')
	print('Each position has number assigned on it (From 1 to 9)')
	print('','[1,2,3]','\n','[4,5,6]','\n','[7,8,9]')
	game()

	
>>> def turna():
	inpa=int(input('Player 1?'))
	if inpa==1:
		m1[0]=1
	if inpa==2:
		m1[1]=1
	if inpa==3:
		m1[2]=1
	if inpa==4:
		m2[0]=1
	if inpa==5:
		m2[1]=1
	if inpa==6:
		m2[2]=1
	if inpa==7:
		m3[0]=1
	if inpa==8:
		m3[1]=1
	if inpa==9:
		m3[2]=1
	game()

	
>>> def turnb():
	inpb=int(input("Player 2?"))
	if inpb==1:
		m1[0]=2
	if inpb==2:
		m1[1]=2
	if inpb==3:
		m1[2]=2
	if inpb==4:
		m2[0]=2
	if inpb==5:
		m2[1]=2
	if inpb==6:
		m2[2]=2
	if inpb==7:
		m3[0]
	if inpb==8:
		m3[1]=2
	if inpb==9:
		m3[2]=2
	game()

	
>>> while True:
	turna()
	turnb()
	w1=[1,1,1]
	if m1==w1 or m2==w1 or m3==w1:
		print('Player 1 wins!')
		break
	for i in range(0,3):
		if m1[i]==1 and m2[i]==1 and m3[i]==1:
			print('Player 1 wins!')
			break
		break
	if m2[1]==1:
		if m1[0]==1 and m3[2]==1:
			print('Player 1 wins!')
			break
	w2=[2,2,2]
	if m1==w2 or m2==w2 or m3==w2:
		print('Player 2 wins!')
		break
	for i in range(0,3):
		if m1[i]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m3[2]==2:
			print('Player 2 wins!')
			break
		if m3[0]==2 and m1[2]==2:
			print('Player 2 wins')
			break

		
Player 1?
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    turna()
  File "<pyshell#9>", line 2, in turna
    inpa=int(input('Player 1?'))
ValueError: invalid literal for int() with base 10: ''
>>> while True:
	turna()
	turnb()
	w1=[1,1,1]
	if m1==w1 or m2==w1 or m3==w1:
		print('Player 1 wins!')
		break
	for i in range(0,3):
		if m1[i]==1 and m2[i]==1 and m3[i]==1:
			print('Player 1 wins!')
			break
		break
	if m2[1]==1:
		if m1[0]==1 and m3[2]==1:
			print('Player 1 wins!')
			break
	w2=[2,2,2]
	if m1==w2 or m2==w2 or m3==w2:
		print('Player 2 wins!')
		break
	for i in range(0,3):
		if m1[i]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m3[2]==2:
			print('Player 2 wins!')
			break
		if m3[0]==2 and m1[2]==2:
			print('Player 2 wins')
			break

		
Player 1? ekin
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    turna()
  File "<pyshell#9>", line 2, in turna
    inpa=int(input('Player 1?'))
ValueError: invalid literal for int() with base 10: ' ekin'
>>> while True:
	turna()
	turnb()
	w1=[1,1,1]
	if m1==w1 or m2==w1 or m3==w1:
		print('Player 1 wins!')
		break
	for i in range(0,3):
		if m1[i]==1 and m2[i]==1 and m3[i]==1:
			print('Player 1 wins!')
			break
		break
	if m2[1]==1:
		if m1[0]==1 and m3[2]==1:
			print('Player 1 wins!')
			break
	w2=[2,2,2]
	if m1==w2 or m2==w2 or m3==w2:
		print('Player 2 wins!')
		break
	for i in range(0,3):
		if m1[i]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m2[i]==2 and m3[i]==2:
			print('Player 2 wins!')
			break
		break
	if m2[1]==2:
		if m1[0]==2 and m3[2]==2:
			print('Player 2 wins!')
			break
		if m3[0]==2 and m1[2]==2:
			print('Player 2 wins')
			break

		
Player 1?1
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
 [1, 0, 0] 
 [0, 0, 0] 
 [0, 0, 0]
TIC TAC TOE GAME
Each position has number assigned on it (From 1 to 9)
 [1,2,3] 
 [4,5,6] 
 [7,8,9]
Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    turna()
  File "<pyshell#9>", line 21, in turna
    game()
  File "<pyshell#6>", line 6, in game
    game()
  File "<pyshell#6>", line 6, in game
    game()
  File "<pyshell#6>", line 6, in game
    game()
  [Previous line repeated 975 more times]
  File "<pyshell#6>", line 2, in game
    print('',m1,'\n',m2,'\n',m3)
RecursionError: maximum recursion depth exceeded while pickling an object
>>> 
