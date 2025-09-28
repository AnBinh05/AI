from typing import Any, Dict

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Xác định xem các tài liệu đã được truy xuất có liên quan đến câu hỏi hay không.
Nếu có bất kỳ tài liệu nào không liên quan, chúng ta sẽ bật cờ để thực hiện tìm kiếm web.

Tham số:
    state (dict): Trạng thái hiện tại của đồ thị (Graph State)

Trả về:
    state (dict): Trạng thái mới, trong đó đã lọc bỏ các tài liệu không liên quan và cập nhật cờ web_search
    """

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = False
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score.binary_score
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            web_search = True
            continue
    return {"documents": filtered_docs, "question": question, "web_search": web_search}