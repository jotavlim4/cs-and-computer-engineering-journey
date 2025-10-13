an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for c in word:
    if c in an_letters:
        print(f"give me an {c}: {c}!")
    else:
        print(f"give me a {c}: {c}!")

print("what's that spell?")
for i in range(times):
    print(f"{word}!!!")