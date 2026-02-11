from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_answer(query, retrieved_docs):
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
Answer the question clearly using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer