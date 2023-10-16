def chain_sum(a):
    def sum(b=0):
        return chain_sum(a + b) if b else a

    return sum
