import timeit
import time

names = ["Irene", "Fredrick", "ire", "Jason"]
tst = "Irene"

# def wrapper(func):
#     start = time.time()
#     print(func("Jackson"))
#     end = time.time()
#     print(f"\nIt took {end-start} seconds to finish")
    
# def matchingLetter(word1, word2):
#     for letters1 in word1:
#         for letters2 in word2:
#             if letters1 == letters2:
#                 return True
#     return False

# def closetNameV1(word, wordlist = names):
    
#     simi = 0
#     commonLetters = {}
#     largestValue = {}
#     for name in names:
#         tempName = name.lower()
#         Tempword = word.lower()
        
#         if tempName == Tempword:
#             return name
        
#         if matchingLetter(Tempword, tempName) == False:
#             pass
#         else:
#             difference = (len(word) - len(name))

#             if len(name) < len(word):
#                 tempName += " " * difference
                
#             for i in range(len(word)):
#                 if word[i] == tempName[i]:
#                     simi += 1
#             commonLetters[f"{name}"] = simi
#             largestValue[simi] = name       
#             simi = 0
    
#     # print(commonLetters)
#     # print(largestValue)
#     if len(largestValue) == 0:
#         if max(largestValue) == 0:
#             return "No matching letters"
#     else:
#         return max(commonLetters, key=commonLetters.get)
        
# def closestNameV2(word, wordList = names):
#     differences = 0
#     allDiff = {}
#     letterWord = []
#     letterName = []
#     for letter in word:
#         letterWord.append(letter)
#     for name in names:
#         for letter in name:
#             letterName.append(letter)
            
#     print(letterWord)
#     print(letterName)
    
#     # for name in names:
#     #     for letters1 in word:
#     #         for letters2 in name:
#     #             if letters1 != letters2:
#     #                 print(f"wordLetter: {letters1}, nameLetter: {letters2}")
#     #                 differences += 1
        
#     #     allDiff[f"{differences}"] = name
#     #     print(allDiff)
#     #     print(differences)
#     #     differences = 0
        
x = 0
def recursive():
    global x
    x += 1
    time.sleep(1)
    print(x)
    recursive()

recursive()
