from dotenv import load_dotenv




from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from pprint import pprint  #Dùng để in ra dữ liệu phức tạp (dictionary, list lồng nhau, JSON…) theo cách dễ đọc hơn so với print thông thường.
from ingestion import retriever
from graph.chains.generation import generation_chain
load_dotenv()

"""
def test_retrival_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"


def test_retrival_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "hôm nay ngày mấy ", "document": doc_txt}
    )

    assert res.binary_score == "no"
"""
def test_generation_chain() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    generation = generation_chain.invoke({"context": docs, "question": question})
    pprint(generation)