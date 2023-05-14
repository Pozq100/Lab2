import calculation


def test_average():
    num_list = [0, 98, 123, 23, 56]
    average = calculation.calculate_average(num_list)
    answer = 60
    assert(average == answer)

def test_minmax():
    num_list = [0, 98, 123, 23, 56]
    min_max = calculation.calculate_min_max(num_list)
    answer = [0,123]
    assert(min_max == answer)

def test_median_odd():
    num_list = [0, 98, 123, 23, 56]
    median = calculation.calculate_median(num_list)
    answer = 56
    assert(answer == median)

def test_median_even():
    num_list = [0, 98, 123, 23, 56, 68]
    median = calculation.calculate_median(num_list)
    answer = 62
    assert(answer == median)

