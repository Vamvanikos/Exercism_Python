def rotate(text, key):
    cypher = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            cypher.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            cypher.append(ch)
    
    return "".join(cypher)