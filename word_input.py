def word_input():
    while True:
        try:
            user_word = input("Enter a 5 letter word (a noun): ").lower()

            if len(user_word) != 5 or not user_word.isalpha():
                raise ValueError("The word must be exactly 5 letters long and contain only letters.")

            return user_word

        except ValueError as e:
            print("Error:", e)
            print("Please try again")
    


