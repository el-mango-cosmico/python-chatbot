from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Define the prompt template with a placeholder for the question
prompt_template = "You are a helpful chatbot that responds in spanish when asking a question: {question_input}" 
prompt = PromptTemplate(
    input_variables=["question_input"], template=prompt_template
    )

# Load the LlamaCpp language model, adjust GPU usage based on your hardware
llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.Q4_K_M.gguf",
    n_gpu_layers=40,
    n_batch=512,  # Batch size for model processing
    verbose=False,  # Enable detailed logging for debugging
)

# Create an LLMChain to manage interactions with the prompt and model
chain = prompt | llm | StrOutputParser()

print("Chatbot initialized, ready to chat...")
while True:
    question = input("> ")
    answer = chain.invoke(question)    
    print(answer, '\n') 