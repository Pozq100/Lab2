import bmi


def test_overweight():
    result = 1
    height = 1.60
    weight = 100
    bmi_calculated = bmi.calculate_bmi(height,weight)
    assert(result == bmi_calculated)

def test_underweight():
    result = -1
    height = 1.90
    weight = 45
    bmi_calculated = bmi.calculate_bmi(height,weight)
    assert(result == bmi_calculated)

def test_normal():
    result = 0
    height = 1.84
    weight = 70
    bmi_calculated = bmi.calculate_bmi(height,weight)
    assert(result == bmi_calculated)

