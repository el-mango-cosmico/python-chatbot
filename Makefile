# Default target
.PHONY: setup
setup:
	@echo "Checking for Poetry installation..."
	@command -v poetry >/dev/null 2>&1 || { echo >&2 "Poetry is not installed. Please install it: https://python-poetry.org/docs/#installation"; exit 1; }
	@echo "Setting up environment with Poetry..."
	poetry install
	@echo "Activating Poetry Env"
	poetry shell

.PHONY: activate
activate:
	@echo "Activating Poetry virtual environment..."
	poetry shell

# Download model(s) with user-provided repository and filename
.PHONY: download-model
download-model:
	@echo "Downloading model(s) using Hugging Face CLI..."
	@mkdir -p models
	@read -p "Enter the Hugging Face repository (e.g., TheBloke/Llama-2-7b-Chat-GGUF): " model_repo; \
	read -p "Enter the model filename (e.g., llama-2-7b-chat.Q4_K_M.gguf): " model_filename; \
	echo "Downloading $$model_filename from $$model_repo..."; \
	poetry run huggingface-cli download $$model_repo $$model_filename --local-dir ./models --local-dir-use-symlinks False || { echo >&2 "Failed to download the model."; exit 1; }
	@echo "Model downloaded to the 'models' directory."
