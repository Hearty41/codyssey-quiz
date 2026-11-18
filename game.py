from quiz import Quiz


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = 0
        self.has_played = False

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

    def get_non_empty_text(self, prompt):
        while True:
            text = input(prompt).strip()
            if not text:
                print("⚠️ 내용을 비워둘 수 없습니다. 다시 입력해주세요.")
                continue
            return text

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
        self.has_played = True
        print("\n========================================")
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = self.get_non_empty_text("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choice = self.get_non_empty_text(f"선택지 {i}: ")
            choices.append(choice)
        answer = self.get_valid_number("정답 번호 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print("✅ 새로운 퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"[{idx}] {quiz.question}")
        print("----------------------------------------")

    def show_score(self):
        if not self.has_played:
            print("\n⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 1번을 눌러 퀴즈를 풀어보세요!")
            return

        print(f"\n🏆 현재 최고 점수: {self.best_score}점")

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = self.get_valid_number("선택: ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quizzes()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    print("\n👋 퀴즈 게임을 종료합니다. 감사합니다!")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 중단되어 안전하게 종료합니다.")