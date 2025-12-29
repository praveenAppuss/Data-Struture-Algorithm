# Anagram

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True
    m1 = min(s1)
    m2 = min(s2)
    if m1 != m2:
        return False
    s1 = s1.replace(m1, '')
    s2 = s2.replace(m2, '')
    return anagram(s1, s2)