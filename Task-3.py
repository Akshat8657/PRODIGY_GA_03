import random

# Your input text
text = "I like cats. I like dogs. Dogs are fun."

# Step 1: Split the text into words
words = text.split()

# Step 2: Build the Markov chain
chain = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if word not in chain:
        chain[word] = []
    chain[word].append(next_word)

# Step 3: Generate text
def generate_text(chain, start_word, length=10):
    word = start_word
    output = [word]

    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        output.append(word)

    return ' '.join(output)

# Example run
print(generate_text(chain, start_word="I", length=10))
