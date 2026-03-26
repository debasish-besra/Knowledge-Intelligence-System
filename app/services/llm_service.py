from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import Config


class LLMService:
    def __init__(self, vector_store):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            api_key=Config.OPENAI_API_KEY
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.vector_store.as_retriever(),
            memory=self.memory,
            verbose=True
        )

    def get_response(self, query):
        try:
            result = self.chain.invoke({"question": query})
            return result["answer"]
        except Exception as e:
            print(f"LLM ERROR: {e}")
            return "System error while processing request."