import random

# 1) 단어 리스트: 여기에 원하는 단어들을 추가하세요.
WORDS = ['python', 'apple', 'banana', 'cherry', 'dragon']

# ANSI 컬러 코드 (윈도우의 경우 터미널 호환 모듈(colorama) 설치 후 초기화 필요)
GREEN  = '\033[42m\033[30m'  # 초록 배경, 검정 글씨
YELLOW = '\033[43m\033[30m'  # 노랑 배경, 검정 글씨
RED    = '\033[41m\033[30m'  # 빨강 배경, 검정 글씨
RESET  = '\033[0m'          # 색상 초기화

def choose_word():
    """단어 리스트에서 랜덤으로 한 개 선택"""
    return random.choice(WORDS)

def print_blanks(word):
    """단어 길이만큼 밑줄(언더스코어) 출력"""
    print(' '.join('_' for _ in word))

def color_feedback(guess, answer):
    """
    추측(guess)과 정답(answer)을 비교해
    위치·문자 일치 → GREEN
    문자만 일치 → YELLOW
    일치 없음 → RED
    """
    feedback = [''] * len(guess)
    # 정답 문자를 추후 비교용으로 복제
    answer_chars = list(answer)

    # 1차: 정확히 같은 위치(GREEN) 검사
    for i, ch in enumerate(guess):
        if i < len(answer) and ch == answer[i]:
            feedback[i] = GREEN + ch + RESET
            answer_chars[i] = None  # 이미 매칭된 글자는 제거

    # 2차: 위치는 다르지만 단어 안에 있는 문자(YELLOW) / 나머지(RED)
    for i, ch in enumerate(guess):
        if feedback[i]:
            continue
        if ch in answer_chars:
            feedback[i] = YELLOW + ch + RESET
            answer_chars[answer_chars.index(ch)] = None
        else:
            feedback[i] = RED + ch + RESET

    return ''.join(feedback)

def play():
    answer = choose_word()
    print("\n🔍 단어 맞추기 게임을 시작합니다! (5회 시도)\n")
    print_blanks(answer)

    for turn in range(1, 6):
        guess = input(f"{turn}/5회차) 추측 단어 입력 → ").strip().lower()
        if len(guess) != len(answer):
            print(f"⚠️  단어는 반드시 {len(answer)}글자여야 합니다.\n")
            continue

        # 힌트 출력
        print(color_feedback(guess, answer), "\n")

        if guess == answer:
            print("🎉 축하합니다! 정답을 맞추셨습니다! 🎉")
            break
    else:
        print(f"😢 실패했습니다. 정답은 “{answer}”였습니다.")
    print("게임 종료.\n")

if __name__ == "__main__":
    play()
