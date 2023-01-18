#연습문제 8.11
odd = {i for i in range(10) if i%2==1}
print(odd)

#8.12 제너레이터 안배움

#8.13
key = ('optimist', 'pessimist', 'troll')
value = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
dic = dict(zip(key, value))
print(dic)

#8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
