def tokenize(raw_string: str) -> list[str]:
    tokens = []
    skip = False
    for i in range(len(raw_string) - 1):
        if ord(raw_string[i]) == 803:
            continue
        if ord(raw_string[i]) == 772:
            continue
        if skip:
            skip = False
            continue
        c = raw_string[i]
        if c in u'pbtdṭdkg' and raw_string[i+1] == u'h':
            c += raw_string[i+1]
            skip = True
        elif c == u'a' and raw_string[i+1] in u'iu':
            c += raw_string[i+1]
            skip = True
        elif c in u'r' and ord(raw_string[i+1]) == 803:
            c = u'ṝ'
        elif c in u'l' and ord(raw_string[i+1]) == 803:
            c = u'ḹ'
        tokens.append(c)
    if not skip:
        tokens.append(raw_string[-1])
    return tokens


def syllabify(raw_string: str) -> list[list[str]]:
    vowels = [u'ṛ', u'ṝ', u'ḷ', u'ḹ',
              u'a', u'ā', u'i', u'ī', u'u', u'ū',
              u'au', u'ai', u'o', u'e']
    tokens = tokenize(raw_string)
    syllables = []
    current = []
    for i in range(len(tokens)):
        if tokens[i] in vowels:
            current.append(tokens[i])
        else:
            if len(current) == 0:
                current.append(tokens[i])
            elif len(current) == 1:
                if current[0] in vowels:
                    if (i + 1) < len(tokens):
                        if tokens[i + 1] in vowels:
                            syllables.append(current)
                            current = [tokens[i]]
                        elif i == (len(tokens) - 2):
                            current.append(tokens[i])
                        else:
                            current.append(tokens[i])
                    else:
                        current.append(tokens[i])
                else:
                    current.append(tokens[i])
            else:
                if (i + 1) < len(tokens):
                    if tokens[i + 1] in vowels:
                        syllables.append(current)
                        current = [tokens[i]]
                    else:
                        current.append(tokens[i])
                else:
                    current.append(tokens[i])
    syllables.append(current)
    return syllables

