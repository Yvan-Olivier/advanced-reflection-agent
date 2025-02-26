# Advanced Reflection Agent 🤖
An intelligent research agent that uses self-reflection and external information to iteratively improve its answers to complex questions.

![Graph Architecture](graph.png)

## 🌟 Features
- **Self-Reflection**: The agent analyzes and critiques its own responses to identify gaps and superfluous information
- **Targeted Research**: Automatically generates relevant search queries based on its self-critique
- **Iterative Refinement**: Improves responses through successive refinement cycles
- **Evidence-Based Responses**: Incorporates numerical citations to back up claims
- **Concise Delivery**: Maintains focused, approximately 250-word responses

## 🏗️ Architecture
The project uses a LangGraph-based architecture with three primary components:
1. **First Responder**: Generates an initial detailed answer and performs self-critique
2. **Tool Executor**: Performs web searches via Tavily API based on identified knowledge gaps
3. **Revisor**: Refines the response by incorporating research findings and addressing critiques

## 🛠️ Technology Stack
- **LangGraph**: For creating the agent workflow and decision framework
- **LangChain**: For prompt engineering and tool integration
- **OpenAI GPT**: Powers the language understanding and generation capabilities
- **Tavily Search API**: Provides real-time information for answer improvement
- **Poetry**: Manages Python dependencies and environment

## 📋 Prerequisites
- Python 3.12 or higher
- Poetry for dependency management
- API keys for:
  - OpenAI
  - Tavily Search
  - LangSmith (optional, for tracing)

## 🚀 Installation
1. Clone the repository
   ```bash
   git clone https://github.com/Yvan-Olivier/advanced-reflection-agent.git
   cd advanced-reflection-agent
   ```

2. Install dependencies with Poetry
   ```bash
   poetry install
   ```

3. Set up your environment variables
   ```bash
   cp .env.example .env
   # Edit the .env file with your API keys
   ```

## 💻 Usage
1. Activate the virtual environment
   ```bash
   poetry shell
   ```

2. Run the agent with a question
   ```python
   python main.py
   ```
   By default, the agent answers a question about AI reflection agents and the LATS algorithm.

3. To use with your own questions, modify the input in `main.py` or use the example script:
   ```python
   python example.py
   ```

## 📊 Agent Workflow
The agent follows this process:
1. **Initial Answer**: Generates a detailed ~250 word response to the question
2. **Self-Critique**: Identifies missing and superfluous elements in the answer
3. **Research**: Generates and executes targeted search queries based on the critique
4. **Refinement**: Produces an improved answer that incorporates new information
5. **Citations**: Adds numerical references to external sources to support claims
