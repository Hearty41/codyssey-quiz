import json
import os
from quiz import Quiz


class QuizGame:
    def __init__(self, default_quizzes, state_file="state.json"):
        self.default_quizzes = default_quizzes
        self.state_file = state_file
        self.quizzes = []
        self.best_score = 0
        self.has_played = False
        self.load_state()

    def load_state(self):
        if not os.path.exists(self.state_file):
            self.quizzes = list(self.default_quizzes)
            self.best_score = 0
            self.has_played = False
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            raw_quizzes = data["quizzes"]
            best_score = data["best_score"]

            if (
                not isinstance(raw_quizzes, list)
                or not isinstance(best_score, int)
                or isinstance(best_score, bool)
            ):
                raise ValueError("필드 타입이 올바르지 않습니다.")

            loaded_quizzes = []
            for item in raw_quizzes:
                if (
                    not isinstance(item, dict)
                    or not isinstance(item.get("question"), str)
                    or not isinstance(item.get("choices"), list)
                    or len(item["choices"]) != 4
                    or not isinstance(item.get("answer"), int)
                    or isinstance(item["answer"], bool)
                    or not (1 <= item["answer"] <= 4)
                ):
                    raise ValueError("퀴즈 항목 형식이 올바르지 않습니다.")
                loaded_quizzes.append(
                    Quiz(item["question"], item["choices"], item["answer"])
                )

            self.quizzes = loaded_quizzes
            self.best_score = best_score
            if self.best_score > 0:
                self.has_played = True

            print(
                f"\n📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)"
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError):
            print("\n⚠️ 데이터 파일이 손상되어 기본 퀴즈 데이터로 복구합니다.")
            self.quizzes = list(self.default_quizzes)
            self.best_score = 0
            self.has_played = False
            self.save_state()

    def save_state(self):
        data = {
            "quizzes": [
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer,
                }
                for q in self.quizzes
            ],
            "best_score": self.best_score,
        }
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"\n⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

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
        self.save_state()

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
        self.save_state()
        print("✅ 새로운 퀴즈가 추가되고 저장되었습니다!")

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
        if not self.has_played and self.best_score == 0:
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
                    self.save_state()
                    print("\n👋 퀴즈 게임을 종료합니다. 감사합니다!")
                    break
        except (KeyboardInterrupt, EOFError):
            self.save_state()
            print("\n\n⚠️ 프로그램이 중단되어 현재 상태를 저장하고 안전하게 종료합니다.")