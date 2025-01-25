def count_words(text):
    # Split the text into words and filter out empty strings
    words = text.split()
    return len(words)
def main():
    print("Welcome to the Word Counter Program!")
    print("Enter a sentence or paragraph below:")
    # Take user input
    user_input = input("> ").strip()
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty input. Please try again.")
        return
    # Count words using the function
    word_count = count_words(user_input)
    # Display the result
    print(f"\nThe total number of words is: {word_count}")