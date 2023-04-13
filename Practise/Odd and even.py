# for q100
Q= range(2,101)
Odd= []
Even = []
for i in Q:
    if i%2 == 0 :
        Even.append(i)
    else:
        Odd.append(i)
print(f'The odd list= {Odd}')
print(f'The even list = {Even}')

