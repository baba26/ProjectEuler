from random import randint

ans = 0.0000000	
	
def fx( current_day , state , probability ):
		global ans
		#print state
		if current_day == 16:
			return
			
		else:
			current_day = current_day + 1
			summation = sum(state)
			#print summation
			if summation == 1:
				ans = ans + probability
				#print state
				
			for i in range(1,len(state)):
				if state[i] == 0:
					continue
				new_state = state[:]
				new_state[i] = new_state[i] - 1
				for j in range(i+1,len(new_state)):
					new_state[j] = new_state[j] + 1
				fx( current_day, new_state, ((probability*state[i])/summation))

				
#          a1 a2 a3 a4 a5
state = [0,0, 1, 1, 1, 1]

p = 1.000000000
current_day = 2
fx( current_day , state[:], p )
print ans
	
