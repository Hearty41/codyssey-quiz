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
        print("       🎯 나만의 넌센스 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def play_quiz(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for idx, quiz in enumerate(self.quizzes, start=1):
            print("\n----------------------------------------")
            quiz.display(idx)
            user_answer = self.get_valid_number("\n정답 입력 (1~4): ", 1, 4)

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}번)")

        score = int((correct_count / total) * 100)
        print("\n========================================")
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = self.get_valid_number("선택: ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    print("\n[준비 중] 다음 단계에서 퀴즈 추가 기능을 연결합니다.")
                elif choice == 3:
                    print("\n[준비 중] 다음 단계에서 퀴즈 목록 기능을 연결합니다.")
                elif choice == 4:
                    print("\n[준비 중] 다음 단계에서 점수 확인 기능을 연결합니다.")
                elif choice == 5:
                    print("\n👋 퀴즈 게임을 종료합니다. 감사합니다!")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 중단되어 안전하게 종료합니다.")