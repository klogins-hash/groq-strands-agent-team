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

## Railway Deployment

This project is optimized for Railway deployment using Railpack. 

### Quick Deploy to Railway

1. **Fork and push to GitHub**:
   ```bash
   git add .
   git commit -m "Add Railway deployment configuration"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your forked repository
   - Railway will automatically detect the Python project and deploy using Railpack

3. **Set Environment Variables**:
   In your Railway project settings, add:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Deployment Files

- `railway.toml` - Railway configuration with Railpack builder
- `app.py` - Flask web server entry point
- `Procfile` - Railway process definition
- `requirements.txt` - Python dependencies including Flask

### Web Interface

Once deployed, your app will have:
- **Web UI**: Interactive interface at your Railway URL
- **API Endpoint**: POST `/chat` for programmatic access
- **Health Check**: GET `/health` for monitoring

### Local Development

To test the web interface locally:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp .env.template .env
   # Edit .env with your Groq API key
   ```

3. **Run locally**:
   ```bash
   python app.py
   ```

4. **Access the web interface**:
   Open http://localhost:8080 in your browser

## Groq Models Available

- `groq/llama-3.1-405b-reasoning`
- `groq/llama-3.1-70b-versatile`
- `groq/llama-3.1-8b-instant`
- `groq/mixtral-8x7b-32768`
- `groq/gemma2-9b-it`
