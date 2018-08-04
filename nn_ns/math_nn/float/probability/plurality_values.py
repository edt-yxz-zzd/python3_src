def is_plurality_values(plurality_values):
    return (has_positive_len(plurality_values)
        and all(p >= 0 for p in plurality_values)
        and sum(plurality_values) > 0
        )
