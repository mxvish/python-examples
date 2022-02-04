import random as rd

win, times = 0, 25
#a_nazo=0
#b_nazo=0

#ゲームを10000回繰り返す
for y in range(10000):
	dice_a = 0
	dice_b = 0

	#コマがいる地点はそれまでのサイコロの出た数の総和
	for z in range(times):
		dice_a += rd.randint(1,6)
		dice_b += rd.randint(1,6)
		
		#スタート地点は相手の逆側で全26マスだから13以上差がついたら勝敗がつく
#		if dice_a % 26 < 3:
#			a_nazo += 1

#		if dice_b % 26 < 3:
#			b_nazo += 1

		if abs(dice_a - dice_b) > 13:
			win += 1
			break

print("勝敗がつく割合")
print(win/10000)
"""
print("aが25回サイコロを振る場合謎を解く回数")
print(a_nazo/10000)
print("bが25回サイコロを振る場合謎を解く回数")
print(b_nazo/10000)
"""
