def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text)
    letter_list = count_letters(text)
    report = generate_report(letter_list)
    
    return report
    
def count_words(text):
    word_counter = 0
    words = text.split()
    for word in words:
        word_counter += 1
    return word_counter

def count_letters(text):
    letter_list = []
    text = text.lower()
    for i in text:
        found = False
        if i.isalpha(): 
            for item in letter_list:
                if item['letter'] == i:
                    item['count'] += 1
                    found = True
                    break
            if not found:
                letter_list.append({'letter': i, 'count': 1})
    return letter_list
    

def generate_report(letter_list):
    letter_list.sort(reverse=True, key=lambda x: x['count'])
    for item in letter_list:
        print(f"The {item['letter']} was written {item['count']} times")

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()



