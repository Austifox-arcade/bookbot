def main():
    lowered_string = ""

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    def word_count(contents):
        words = contents.split()
        print (len(words))
    word_count(file_contents)

    def character_counter(char):
        count = {}
        lowered_string = char.lower()
        for c in lowered_string:
            if c.isalpha():
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1

        return count

    def print_report(file_contents):
        # Count words
        words = file_contents.split()
        word_count = len(words)
        
        # Count characters
        character_counts = character_counter(file_contents)
        
        # Convert dictionary to list of dictionaries for sorting
        results = [{"character": char, "num": num} for char, num in character_counts.items()]
        
        # Define sorting function
        def sort_on(dict):
            return dict["num"]
        
        # Sort the list by character count in descending order
        results.sort(reverse=True, key=sort_on)
        
        # Print report
        print("--- Begin report ---")
        print(f"{word_count} words found in the document")
        for result in results:
            print(f"The '{result['character']}' character was found {result['num']} times")
        print("--- End report ---")
    
    print_report(file_contents)

main()
    


