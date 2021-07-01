#reverse every word in a sentence

def reversesentence(sentence):
    return " ".join(reversed(sentence.split()))


print(reversesentence("I wish I could"))


def reversesentence2(sentence):
    return " ".join(sentence.split()[::-1])

print(reversesentence2("No matter what"))


def reversesentence3(sentence):
    return " ".join(word[::-1] for word in sentence.split(" "))

print(reversesentence3("No way to forget"))


# reverse letters in text with loop
def reverseletters(sentence):
    result = ""
    for s in range(1, len(sentence) + 1):
        result += sentence[len(sentence) - s]
    return result

print(reverseletters("No way to forget")) 


# reverse letters in text with function
def reverseletters(sentence):
    return "".join(reversed(sentence))

print(reverseletters("No matter what")) 


