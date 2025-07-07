import random

WORD_LIST = [
    # 과일·채소·동물·추상어 혼합, 최대 8글자 단어 100개
    "APPLE",   "BANANA",  "ORANGE",  "MANGO",   "PAPAYA",
    "GRAPES",  "CHERRY",  "PEACH",   "LEMON",   "LIME",
    "MELON",   "OLIVE",   "PLUM",    "KIWI",    "APRICOT",
    "PEPPER",  "CABBAGE", "CARROT",  "RADISH",  "SPINACH",

    "POTATO",  "TOMATO",  "GARLIC",  "ONION",   "GIRAFFE",
    "ELEPHANT","CHEETAH", "PANTHER", "OCTOPUS", "DOLPHIN",
    "SHARK",   "WHALE",   "RABBIT",  "TURKEY",  "PENGUIN",
    "KANGAROO","CAMERA",  "MONITOR", "KEYBOARD","LAPTOP",

    "PHONE",   "TABLE",   "CHAIR",   "DESKTOP", "PILLOW",
    "BLANKET", "BACKPACK","NOTEBOOK","PAINTING","SCISSOR",
    "UMBRELLA","SUNGLASS","MIRROR",  "WINDOWS", "QUANTUM",
    "ECLIPSE", "AURORA",  "GALAXY",  "NEUTRON", "PROTON",

    "GRAVITY", "PHYSICS", "CHEMIST", "ATOM",    "MOLECULE",
    "CRYSTAL", "PLASMA",  "ACOUSTIC","HARMONY", "SYMMETRY",
    "RHYTHM",  "EUPHONY", "ENIGMA",  "RIDDLE",  "PUZZLE",
    "MYSTERY","PARADOX", "CRYPTIC", "OXYGEN",  "ZEPHYR",

    "EPOCH",   "ZIGZAG",  "VIVID",   "SYNTAX",  "TENSOR",
    "VECTOR",  "EULER",   "GAUSSIAN","RIEMANN", "LAPLACE",
    "LEGEND",  "FABLE",   "HEROISM", "EPIC",    "ODYSSEY",
    "PHANTOM", "HARVEST", "SONIC",   "RELAX",   "TRIBUTE",
]

re = 0

word = random.choice(WORD_LIST)
print(word) #지울거

question = list(word)
count = len(question) #문제 단어 글자 개수 + 배열화

for j in range(count):
    print("_", end=" ")  # 밑줄 출력

for i in range(5): #반복 횟수

    print("\n")

    answer = input(f"Your Answer {i+1} (in capital) : ")#답변

    answer_count = len(answer)
    answer_letter = list(answer)

    if answer_count != count:
        print("Try Again : ")

    result = [x if x == y else '_' for x, y in zip(question, answer_letter)]
    check = ' '.join(result)
    print(check)

    if answer_letter == question:
        re = 1
        break

if re == 0:
    print("실패!!")

if re == 1:
    print("정답!!")