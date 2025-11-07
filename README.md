# Strands Agent Team with Groq LLM

A basic multi-agent system built with Strands Agents using Groq as the LLM provider via LiteLLM.

## Features

- **Multi-Agent Architecture**: Specialized agents for different tasks
- **Groq LLM Integration**: Fast inference using Groq's models
- **Team Coordination**: Coordinator agent orchestrates task delegation
- **Tool Integration**: Custom tools for each agent specialization

## Agent Team

1. **Research Analyst** - Handles research and analysis tasks
2. **Project Planner** - Creates project plans and task breakdowns
3. **Senior Developer** - Handles code review and development tasks
4. **Team Coordinator** - Orchestrates the team and delegates tasks

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   - Copy your Groq API key to the `.env` file (already included)
   - Or set it as an environment variable:
   ```bash
   export GROQ_API_KEY=your_api_key_here
   ```

3. **Test the setup**:
   ```bash
   python test_agents.py
   ```

4. **Run the agent team**:
   ```bash
   python agent_team.py
   ```

## Usage Examples

Once running, try these commands:

- `"Research the latest trends in AI"`
- `"Plan a mobile app development project"`
- `"Review this Python code: def add(a, b): return a + b"`
- `"I need to research AI trends and then plan a project for an AI assistant"`

## Architecture

The system uses:
- **Strands Agents SDK** for agent framework
- **LiteLLM** as the model provider interface
- **Groq** for fast LLM inference
- **Custom tools** for agent specializations

## Customization

You can:
- Modify agent system prompts in `agent_team.py`
- Add new tools using the `@tool` decorator
- Change the Groq model (e.g., `groq/llama-3.1-405b-reasoning`)
- Add more specialized agents to the team

## Groq Models Available

- `groq/llama-3.1-405b-reasoning`
- `groq/llama-3.1-70b-versatile`
- `groq/llama-3.1-8b-instant`
- `groq/mixtral-8x7b-32768`
- `groq/gemma2-9b-it`
