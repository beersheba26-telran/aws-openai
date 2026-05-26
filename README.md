# Creating RAG agent with tool-augmented reasoning
## Integration of Fastembed model for embeddings with cosine similarity
- Consider  introducing abstract class TextProcessor (no method factory is needed ) in module text_processor.py
- Consider introducing TextProcessor implementation (Fastembed) in module text_processor_impl.py (pattern SingleTone)
## Agent workload flow
- Trying to get document from RAG using TextProcessor Fastembed based implementation
- If there is a document with cosine similarity greater than threshold (configured value) it should be returnde as the response
- If there is no a document with cosine similarity greater than threshold (configured value) the flow goes through existing from previous task code
