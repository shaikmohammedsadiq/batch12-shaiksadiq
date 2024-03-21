import random

# Questions database - Tuple of (question, answer) pairs
questions = [
    ("What is the holy book of Islam called?", "Quran"),
    ("Who is the final prophet in Islam?", "Muhammad"),
    ("What is the name of the Islamic declaration of faith?", "Shahada"),
    ("In which city is the Kaaba located?", "Mecca"),
    ("What is the name of the month of fasting in Islam?", "Ramadan"),
    ("What is the Islamic greeting meaning 'peace be upon you'?", "Salam"),
    ("How many pillars of Islam are there?", "Five"),
    ("What is the name of the pilgrimage to Mecca that Muslims are required to make at least once in their lifetime?", "Hajj"),
    ("What is the name of the holy month in which fasting takes place?", "Ramadan"),
    ("What is the name of the Islamic prayer performed five times a day?", "Salah"),
    ("What is the name of the direction that Muslims face during prayer?", "Qibla"),
    ("What is the name of the Islamic charity given to the poor?", "Zakat"),
    ("What is the name of the night journey made by Prophet Muhammad from Mecca to Jerusalem and then to heaven?", "Isra and Mi'raj"),
    ("What is the name of the place of worship in Islam?", "Mosque"),
    ("What is the name of the Islamic month following Ramadan?", "Shawwal"),
]

def get_random_question():
    return random.choice(questions)

def ask_question(question):
    user_answer = input(f"\nQuestion: {question}\nYour answer: ").strip().lower()
    return user_answer

def main():
    print("Welcome to the Islamic Quiz Game!")
    print("You will be asked questions related to Islam. Let's test your knowledge!")

    # Competitors
    competitors = ["Arshad", "Sadiq"]
    scores = {competitor: 0 for competitor in competitors}

    num_questions = 15  # Number of questions to ask
    
    for _ in range(num_questions):
        question, answer = get_random_question()
        print("\nNew Question:")
        for competitor in competitors:
            print(f"{competitor}, it's your turn:")
            user_answer = ask_question(question)
            if user_answer == answer.lower():
                print("Correct!")
                scores[competitor] += 1
            else:
                print(f"Wrong! The correct answer is: {answer}")

    print("\nQuiz completed!\n")
    for competitor, score in scores.items():
        print(f"{competitor}'s score: {score}/{num_questions}")

    winner = max(scores, key=scores.get)
    print(f"\nThe winner is: {winner}!")

if __name__ == "__main__":
    main()
