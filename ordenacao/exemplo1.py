def esta_ordenada(conj: list) -> bool:
    i = 0
    while i < len(conj) - 1:
        if conj[i] > conj[i + 1]:
            return False
        i = i + 1

    return True    


