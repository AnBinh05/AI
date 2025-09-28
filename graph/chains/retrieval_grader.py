from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama

# Dùng model Ollama local (gemma3:270m)
llm = ChatOllama(
    model="gemma3:270m",  #
    temperature=0
)

class GradeDocuments(BaseModel):
    """Class GradeDocuments được dùng để định nghĩa kết quả nhị phân (yes/no) cho việc đánh giá tài liệu có liên quan đến câu hỏi hay không."""

    binary_score: str = Field(
        description="Tài liệu có liên quan đến câu hỏi hay không, trả lời 'yes' hoặc 'no'."
    )

# ép LLM trả về kết quả theo schema GradeDocuments
structured_llm_grader = llm.with_structured_output(GradeDocuments)

# Prompt cho LLM đóng vai "giám khảo"
system = """Bạn là một giám khảo đánh giá mức độ liên quan của tài liệu được truy xuất với câu hỏi của người dùng.\n
Nếu tài liệu chứa từ khóa hoặc ý nghĩa ngữ nghĩa liên quan đến câu hỏi, hãy đánh giá là có liên quan.\n
Hãy đưa ra điểm nhị phân "yes" hoặc "no" để chỉ ra liệu tài liệu có liên quan đến câu hỏi hay không."""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

# Kết hợp prompt và structured output
retrieval_grader = grade_prompt | structured_llm_grader
