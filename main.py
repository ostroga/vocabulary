def ShowTop5WordsByLength(text):
    forbidennedSymbols = [".", ",", "-", "'", "\""]
    for symbol in forbidennedSymbols:
        text = text.replace(symbol, '') # Removing symbols we don't need

    allWords = text.split()
    wordsWithCount = [] # Array with each word and length

    for word in allWords:
        # Making dictionary of each word
        word = {
            "Word": word,
            "Length": len(word)
        }
        wordsWithCount.append(word) # Adding word to the array

    wordsSortedByLength = []

    # Sorting the array by length with "bubble" sort
    for i in range( len(wordsWithCount) ):
        for j in range( len(wordsWithCount) - i - 1):
            if wordsWithCount[j]["Length"] > wordsWithCount[j + 1]["Length"]:
                temp = wordsWithCount[j]
                wordsWithCount[j] = wordsWithCount[j + 1]
                wordsWithCount[j + 1] = temp

    # Reversing the array
    wordsWithCount.reverse()

    if len(wordsWithCount) > 5:
        for i in range(0, 5):
            print(f'Top {i + 1} - {wordsWithCount[i]["Word"]} - {wordsWithCount[i]["Length"]} symbols')
    else:
        for i in range(0, len(wordsWithCount)):
            print(f'Top {i + 1} - {wordsWithCount[i]["Word"]} - {wordsWithCount[i]["Length"]} symbols')

def ShowTop5WordsByCount(text):
    forbidennedSymbols = [".", ",", "-", "'", "\""]
    for symbol in forbidennedSymbols:
        text = text.replace(symbol, '') # Removing symbols we don't need

    allWords = text.split()
    wordsWithCount = [] # Array with each word and length

    for word in allWords:
        # Making dictionary of each word
        word = {
            "Word": word,
            "Count": text.count(word)
        }
        wordsWithCount.append(word) # Adding word to the array

    wordsSortedByLength = []

    # Sorting the array by length with "bubble" sort
    for i in range( len(wordsWithCount) ):
        for j in range( len(wordsWithCount) - i - 1):
            if wordsWithCount[j]["Count"] > wordsWithCount[j + 1]["Count"]:
                temp = wordsWithCount[j]
                wordsWithCount[j] = wordsWithCount[j + 1]
                wordsWithCount[j + 1] = temp

    # Reversing the array
    wordsWithCount.reverse()

    if len(wordsWithCount) > 5:
        for i in range(0, 5):
            print(f'Top {i + 1} - {wordsWithCount[i]["Word"]} - {wordsWithCount[i]["Count"]} times')
    else:
        for i in range(0, len(wordsWithCount)):
            print(f'Top {i + 1} - {wordsWithCount[i]["Word"]} - {wordsWithCount[i]["Count"]} times')

def ShowWordsCount(text):
    allWords = text.split()
    print(f"\n{len(allWords)} слів")

text = input("Введіть текст: ")

choice = input("Виберіть варіант:"
      "\n1 - Топ 5 по довжині"
      "\n2 - Топ 5 по кількості повторювань"
      "\n3 - Показати кількість слів у тексті\n")
if choice == "1":
    ShowTop5WordsByLength(text)
elif choice == "2":
    ShowTop5WordsByCount(text)
elif choice == "3":
    ShowWordsCount(text)