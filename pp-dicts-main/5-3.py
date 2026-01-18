translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input("Enter English word: ")

if word in translations:
    print("Polish translation:", translations[word])
else:
    print("Translation unavailable.")
