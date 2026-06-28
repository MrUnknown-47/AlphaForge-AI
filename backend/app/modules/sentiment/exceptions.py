from app.shared.exceptions import AlphaForgeException

class SentimentException(AlphaForgeException):
    status_code: int = 400
    detail: str = "Sentiment module operations error"

class ArticleNotFoundException(SentimentException):
    status_code: int = 404
    detail: str = "Requested news article was not found"

class ModelInferenceException(SentimentException):
    status_code: int = 500
    detail: str = "Transformer model sentiment classification failed"