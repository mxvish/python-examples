import random as rd

def demo(player_hp, player_attack1, player_attack2):
	win=0
	turn=0

	for x in range(10000):
		hp_1=player_hp
		hp_2=player_hp
		king_hp=6500

		while hp_1>0 or hp_2>0 and king_hp>0:
			turn+=1
			if hp_1>0:
				king_hp-=rd.randint(1,6)*player_attack1
			if hp_2>0:
				king_hp-=rd.randint(1,6)*player_attack2

			if king_hp<=0:
				win+=1
				break

			damage=rd.randint(0,4)*70
			randnum=rd.randint(1,12)

			for x in range(2):
				if 1<=randnum and randnum<=4:
					if hp_1>0:
						hp_1-=damage
					else:
						hp_2-=damage
					if hp_2>0:
						hp_2-=damage
					else:
						hp_1-=damage
				elif 5<=randnum and randnum<=7:
					if hp_1>0:
						hp_1-=damage
					else:
						hp_2-=damage
				elif 8<=randnum and randnum<=10:
					if hp_2>0:
						hp_2-=damage
					else:
						hp_1-=damage
				else:
					king_hp+=1000

			if hp_1<=0 and hp_2<=0:
						break

	print("--------------------------------------------------------")
	print("player_hp	",player_hp)
	print("player_attack1",player_attack1)
	print("player_attack2",player_attack2)
	print(win/10000)
	print(turn/10000)

demo(1000, 300, 300)
demo(700, 200, 200)
demo(640, 430, 430)
demo(640, 430, 180)
