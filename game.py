class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = 0

    def get_valid_number(self, prompt, min_val, max_val):
        while True:
            raw = input(prompt).strip()
            if not raw:
                print(f"⚠️ 입력이 비어 있습니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")
                continue
            try:
                num = int(raw)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")
                continue
            if not (min_val <= num <= max_val):
                print(f"⚠️ 범위를 벗어났습니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")
                continue
            return num

    def display_menu(self):
        print("\n========================================")
        print("        🎯 나만의 마블 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = self.get_valid_number("선택: ", 1, 5)
                if choice == 1:
                    print("\n[준비 중] 4단계에서 퀴즈 풀기 기능을 연결합니다.")
                elif choice == 2:
                    print("\n[준비 중] 5단계에서 퀴즈 추가 기능을 연결합니다.")
                elif choice == 3:
                    print("\n[준비 중] 5단계에서 퀴즈 목록 기능을 연결합니다.")
                elif choice == 4:
                    print("\n[준비 중] 6단계에서 점수 확인 기능을 연결합니다.")
                elif choice == 5:
                    print("\n👋 퀴즈 게임을 종료합니다. 감사합니다!")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 중단되어 안전하게 종료합니다.")