def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        return print("Impossivel dividir por zero")
    else:
        return a/b
def test_sum():
    assert sum(8,9)==17
    assert sum (10,5)==15
    assert sum(-2,2)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(10,5)==5
    assert sub(2,1)==1

def test_mult():
    assert mult(2,1)==2
    assert mult(5,5)==25
    assert mult(7.4,2)==14.8

def test_div():
    assert div(2,0)