class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용 (문자열)
        self.choices = choices    # 보기 4개 (리스트)
        self.answer = answer      # 정답 번호 1~4 (숫자)

    def display(self, number):
        print(f"\n[문제 {number}]")
        print(self.question)
        for idx, choice in enumerate(self.choices, start=1):
            print(f"  {idx}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer