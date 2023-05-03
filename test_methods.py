import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 3
    b = 7

    output = methods.soma(a,b)

    assert output == 10

def test_subtrai():
    a = 7
    b = 3

    output = methods.subtrai(a,b)

    assert output == 4

def test_multiplicacao():
    a = 3
    b = 7

    output = methods.multiplicacao(a,b)

    assert output == 21

def test_divisao():
    a = 8
    b = 4

    output = methods.divisao(a,b)

    assert output == 2

def test_elevaQuadrado():
    a = 9

    output = methods.elevaQuadrado(a)

    assert output == 81