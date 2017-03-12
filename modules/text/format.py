def camel(string):
    return string[0].upper() + string[1:].lower()

def printable(word):
    return ''.join(c for c in word if c in string.printable)

def chunk(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))