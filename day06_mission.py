#연습문제 9.2
def get_odds():
    for i in range(10):
        if i%2:
            yield i

cnt=0
for odds in get_odds():
    if cnt==2:
        print(odds)
    cnt+=1

#9.3  ???

def sdf(fcn):
    def nn(*args, **kwargs):
        result = fcn(*args, **kwargs)
        print(result)
    return nn

def test(fcn):
    def new_fcn(*args, **kwargs):
        print('start')
        result = fcn(*args, **kwargs) #
        print('end')


    return new_fcn
@sdf
@test
def lala():
    print('ss')
    return 1

lala()

