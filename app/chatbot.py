# Imports at the top for clarity and performance
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Function to initialize the chatbot model and chain
def initialize_chatbot():
    # Define the prompt template
    prompt_template = "You are a helpful chatbot that responds in Spanish when asked a question: {question_input}"
    prompt = PromptTemplate(
        input_variables=["question_input"], template=prompt_template
    )

    # Load the LlamaCpp language model
    llm = LlamaCpp(
        model_path="models/llama-2-7b-chat.Q4_K_M.gguf",
        n_gpu_layers=40,
        n_batch=512,
        verbose=False
    )

    # Create an LLMChain for interaction
    return prompt | llm | StrOutputParser()


# Main function to handle the chatbot loop
def main():
    chain = initialize_chatbot()
    print("Chatbot initialized. Type 'exit' to quit.")
    while True:
        try:
            question = input("> ")
            if question.lower() == "exit":
                print("Goodbye!")
                break
            answer = chain.invoke({"question_input": question})
            print(answer, '\n')
        except Exception as e:
            print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
