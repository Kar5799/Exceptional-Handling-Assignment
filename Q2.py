subjects = ["Americans ", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]
final = [f"{sub} {verb} {obj}" for sub in subjects for verb in verbs for obj in objects]
for sentence in final:
    print(sentence)
