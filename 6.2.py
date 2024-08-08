def compute_series(n):
    """Computes the series m(i) up to n terms."""
    result = 0.0
    for i in range(1, n + 1):
        result += i / (i + 1)
    return result

def display_table(n):
    """Displays a table of the series m(i) up to n terms."""
    print("i    m(i)")
    print("----------")
    for i in range(1, n + 1):
        print("{:2d}   {:.4f}".format(i, compute_series(i)))

# Example usage:
display_table(20
