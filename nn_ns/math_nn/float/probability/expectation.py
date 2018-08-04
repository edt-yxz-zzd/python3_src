
__all__ = '''
    expectation_of
    '''.split()


from .plurality_values import is_plurality_values
#def expectation_of(numbers, probability_distribution):
def expectation_of(numbers, plurality_values):
    '''#probability theory and statistics
    expected value
    expectation
    mathematical expectation
    EV
    average
    mean value
    mean
    first moment
    '''
    assert has_positive_len(numbers)
    assert is_plurality_values(plurality_values)
    assert len(numbers) == len(plurality_values)
    TOTAL = sum(plurality_values)
    return sum(x*p for x, p in zip(numbers, plurality_values))/TOTAL

