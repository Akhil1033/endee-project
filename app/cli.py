# app/cli.py

from rag import answer_query

def main():
    print("\n🔍 Endee RAG System (type 'exit' to quit)\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = answer_query(query)
        print("\n🧠 Answer:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()