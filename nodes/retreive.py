from typing import Any,Dict
from graph.state import GraphState
from  ingestion import retriever # import retriever (thành phần dùng để tìm kiếm dữ liệu)
def retrieve (state: GraphState) ->Dict[str, Any]:
    print("---RETRIEVE---")  # in log ra màn hình để biết đang chạy bước Retrieve
    question = state["question"]# lấy câu hỏi từ state (trạng thái truyền vào)
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}


tri