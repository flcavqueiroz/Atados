
'''O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.

Determine o maior lucro dado esse array K de preços.

Exemplo 1:


    Input: [7,1,5,3,6,4]

    Output: 5

    Explicação: Este valor acontece quando compramos a ação no 2o dia e a vendemos no 5o dia (6 - 1)

Exemplo 2:


    Input: [7,6,4,3,1]

    Output: 0

    Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.
'''
from random import randint

array = []
count = 0

while True:
    num = randint(1, 10)
    if num not in array:
        array.append(num)
        count += 1
    if count >= 6:
        break

value = max(array) - min(array)
posmin = array.index(min(array))
posmax = array.index(max(array))
print(f'The difference between high and low prices was {value}')
print('='*75)
print(f'The day with the highets price was: Day {posmax + 1}')
print('='*75)
print(f'The day with the minimum value was: Day {posmax + 1}')
print('='*75) 
if posmax > posmin:
    print(f'There was a good opportunity to buy the stocks at day {posmin + 1} and sell on day {posmax + 1} \nWith a profit of {value} per stock')
else:
    print(f'There was no opportunity this week, the highest value this week was on day {posmax + 1}')
print('='*75)
print(f'The stocks values for the week per day are: {array}')

