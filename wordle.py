import random
from collections import Counter
from colorama import Back,Style,init
init()

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
tries = 0
Max_tries = 5

word = random.choice(WORD_LIST)
print(word)
print('Guess The Word', '\n')

question = list(word)
count = len(question) #문제 단어 글자 개수 + 배열화

for j in range(count):
    print("_", end=" ")  # 밑줄 출력
print('\n', count,'글자', '\n')

while tries < Max_tries: #반복 횟수(기회 5번)

    answer = input(f"Your Answer {tries+1} (in capital) : ")#답변
    print('\n')

    answer_count = len(answer)
    answer_letter = list(answer)

    if answer_count != count:
        print("Try Again")
        continue #글자수 맞지 않으면 다시

    tries += 1

    def color_compare(question, answer_letter):
      remaining = Counter(question)
      result = [None] * len(question)

      # 1) 초록 처리 (위치+글자 일치)
      for i, (q, a) in enumerate(zip(question, answer_letter)):
        if a == q:
          result[i] = Back.GREEN + a + Style.RESET_ALL
          remaining[a] -= 1

      # 2) 노랑·빨강 처리 (나머지)
      for i, a in enumerate(answer_letter):
        if result[i] is not None:
          continue
        if remaining[a] > 0:
          result[i] = Back.YELLOW + a + Style.RESET_ALL
          remaining[a] -= 1
        else:
          result[i] = Back.RED + '_' + Style.RESET_ALL

      return result #글자위치, 종류 맞으면 초록색 하나라도 틀리면 빨간색

    result = color_compare(question, answer_letter)
    check = ''.join(result)

    print(check)
    print("\n")

    if answer_letter == question:
        re = 1
        break #루프 종료

if re == 0:
    print("실패!!")
    print('정답은', word)

if re == 1:
    print("정답!!")

