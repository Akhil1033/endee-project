from app.rag.search import search
from app.rag.generator import generate_answer

if __name__ == "__main__":
    query = input("Enter your question: ")

    results = search(query)

    answer = generate_answer(query, results)

    print("\nGenerated Answer:\n")
    print(answer)