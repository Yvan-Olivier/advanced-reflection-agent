from typing import List

from pydantic import BaseModel, Field


class Reflection(BaseModel):
    """ Represents a critique of an answer, detailing what is missing and what is superfluous. """
    missing: str = Field(description="Critique of what is missing in the answer")
    superfluous: str = Field(description="Critique of what is superfluous in the answer")

class AnswerQuestion(BaseModel):
    """Represents a detailed answer to a user's question, 
    including a reflection and suggested search queries for improvement."""

    answer: str = Field(description="~250 words detailed answer to the user's question")
    reflection: Reflection = Field(description="Your reflection on the initial answer")
    search_queries: List[str] = Field(description="1-3 search queries for researching improvements to adress the critique of your current answer")

class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""

    references: List[str] = Field(
        description="Citations motivating your updated answer."
    )