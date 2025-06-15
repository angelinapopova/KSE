import word_generator
import word_input

generated_word = word_generator.generate_word()
user_word = word_input.word_input()
def check_word(user_word, generated_word):
    result=[]
    for i, letter in enumerate(user_word):
        if letter == generated_word[i]:
            result.append(f"\033[92m{letter}\033[0m")
        elif letter in generated_word:
            result.append(f"\033[93m{letter}\033[0m")
        else:
            result.append(f"\033[90m{letter}\033[0m")
    return"".join(result)
print(check_word(user_word, generated_word))