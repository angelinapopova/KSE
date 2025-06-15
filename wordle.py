import word_generator
import word_input
import results

while True:
    generated_word = word_generator.generate_word()
    max_attempts = 7
    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1}/{max_attempts}")
    
        user_word = word_input.word_input()
        result = results.check_word(user_word, generated_word)
        print(result)
        if user_word == generated_word:
            print("Congradulations!")
            break
    else:
        print("Soory, you're a loser:(")
    play_again = input("Do you want to play again? ")
    if play_again != "yes":
        break