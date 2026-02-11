from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_text_splitter():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter


def chunk_text(text):
    splitter = get_text_splitter()
    return splitter.split_text(text)