from quiz import Quiz
from game import QuizGame


def get_default_quizzes():
    return [
        Quiz(
            "논리 있는 사람이 총을 쏘면?",
            ["빵빵빵", "타당타당", "탕탕탕", "퓩퓩퓩"],
            2
        ),
        Quiz(
            "네 마리의 고양이가 괴물이 되면?",
            ["디지몬", "유희왕", "파워레인저", "포켓몬"],
            4
        ),
        Quiz(
            "닭이 좁은 틈에 갇히면 내는 소리는?",
            ["꽥꽥", "삐약삐약", "짹짹", "꽉끼오"],
            4
        ),
        Quiz(
            "석유가 도착하는데 걸리는 시간은?",
            ["오일", "반나절", "하루", "일주일"],
            1
        ),
        Quiz(
            "침대를 밀고 돌리면?",
            ["배드민턴", "탁구", "테니스", "볼링"],
            1
        )
    ]


if __name__ == "__main__":
    default_quizzes = get_default_quizzes()
    game = QuizGame(default_quizzes)
    game.run()