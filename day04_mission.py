#연습문제 7.1
year=int(input())
year_lists=[i for i in range(year,year+6)]
print(year_lists)

#7.2
print(f'세번째 생일 : {year_lists[3]}')

#7.3
print(f'가장 나이 많을 때 : {year_lists[-1]}')

#7.8
surprise = ["Groucho", "Chico", "Harpo"]

#7.9
surprise[2]=surprise[2].lower()
print(surprise)
surprise[2]=surprise[2][::-1].title()
print(surprise)

#7.10
even = [i for i in range(10) if i%2==0]
print(even)

#7.11
start1=["fee", "fie", "foe"]
rhymes=[
    ("float", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2="Someone better"

for i in range(7):
    print(f'{start1[0].title()}! {start1[1].title()}! {start1[2].title()}!', end=' ')
    print(f'{rhymes[i][0].title()}!')
    print(f'{start2} {rhymes[i][1]}.')
