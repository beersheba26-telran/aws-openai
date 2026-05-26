from abc  import ABC, abstractmethod
from fastembed import TextEmbedding
class TextProcessor(ABC):
    
   
    @abstractmethod   
    def setDocuments(self, documents: list[str]):
        pass
    @abstractmethod
    def process(self, query: str, threshold: float = 0.7) -> str|None:
        """Process the documents and return a tuple containing the document and a score.
        If no document meets the threshold, return None."""
        
        
             