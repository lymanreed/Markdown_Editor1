def get_percentage(percentage, precision=None):
    return f'{round(percentage * 100)}%' if precision is None else f'{round(percentage * 100, precision)}%'
