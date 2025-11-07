# Strands Agent Team - Railway Deployment

A multi-agent AI system deployed on Railway using Groq LLM for fast inference.

## 🚀 Quick Deploy on Railway

### One-Click Deployment
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/klogins-hash/groq-strands-agent-team)

### Manual Deployment

1. **Fork this repository** to your GitHub account
2. **Create new Railway project** from your forked repository
3. **Set environment variables** in Railway dashboard:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=groq/llama-3.1-8b-instant
TEMPERATURE=0.7
MAX_TOKENS=500
SECRET_KEY=your-secret-key-here
PORT=8080
```

4. **Deploy** - Railway will automatically build and deploy

## 📋 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GROQ_API_KEY` | ✅ | - | Your Groq API key from <https://console.groq.com/> |
| `GROQ_MODEL` | ❌ | `groq/llama-3.1-8b-instant` | Groq model to use |
| `TEMPERATURE` | ❌ | `0.7` | LLM temperature (0.0-1.0) |
| `MAX_TOKENS` | ❌ | `500` | Maximum response tokens |
| `SECRET_KEY` | ❌ | Auto-generated | Flask session secret |
| `PORT` | ❌ | `8080` | Application port |

## 🏗️ Architecture

### Multi-Agent System

- **Research Analyst** - Technology and business research
- **Project Planner** - Strategic project planning and task breakdown
- **Senior Developer** - Code analysis and technical guidance
- **Team Coordinator** - Intelligent task delegation and coordination

### Technical Stack

- **Backend**: Flask + Strands Agents SDK
- **LLM**: Groq via LiteLLM
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Deployment**: Railway with Nixpacks
- **Web Server**: Gunicorn

## 🎯 Features

- **Web Interface**: Clean, responsive chat interface
- **Real-time Communication**: Instant agent responses
- **Multi-Agent Coordination**: Intelligent task routing
- **Health Monitoring**: Built-in health checks
- **Error Handling**: Graceful error management
- **Mobile Responsive**: Works on all devices

## 📱 Usage Examples

Once deployed, you can ask the Team Coordinator:

### Research Tasks

- "Research the latest trends in artificial intelligence"
- "Analyze the blockchain technology market"
- "Investigate renewable energy developments"

### Planning Tasks

- "Plan a mobile app development project"
- "Create a roadmap for a website redesign"
- "Break down a data migration project"

### Code Analysis

- "Analyze this Python code: `def calculate_sum(numbers): return sum(numbers)`"
- "Review this JavaScript function for best practices"
- "Suggest improvements for this SQL query"

### Complex Requests

- "Research AI trends and then plan an AI assistant project"
- "I need to understand cloud computing and plan a migration strategy"

## 🔧 Local Development

1. **Clone and setup**:

```bash
git clone https://github.com/klogins-hash/groq-strands-agent-team.git
cd groq-strands-agent-team
cp .env.template .env
# Add your GROQ_API_KEY to .env
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run locally**:

```bash
python app.py
```

4. **Open browser**: Navigate to <http://localhost:8080>

## 🐛 Troubleshooting

### Common Issues

#### API Key Errors

- Ensure your Groq API key is valid and active
- Check if you have sufficient credits in your Groq account
- Verify the key is set correctly in Railway environment variables

#### Deployment Issues

- Check Railway build logs for errors
- Ensure all environment variables are set
- Verify the repository is properly forked

#### Performance Issues

- Adjust `MAX_TOKENS` for faster responses
- Use `groq/llama-3.1-8b-instant` for speed
- Monitor Railway resource usage

### Health Check

Your deployed app includes a health endpoint:

```http
GET /health
```

Returns:

```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "version": "1.0.0"
}
```

## 🔒 Security

- ✅ API keys stored in environment variables
- ✅ No hardcoded secrets in code
- ✅ HTTPS enforced on Railway
- ✅ Session management enabled
- ✅ Input sanitization implemented

## 📊 Monitoring

Railway provides built-in monitoring for:

- Resource usage (CPU, Memory)
- Request logs
- Error tracking
- Deployment metrics

## 🚀 Scaling

Your Railway deployment automatically scales based on:

- Traffic load
- Resource utilization
- Geographic distribution

## 💰 Cost Optimization

- **Groq API**: Pay-per-use, very cost-effective
- **Railway**: Free tier available, then usage-based
- **Optimizations**: Adjust token limits and model choice

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- **Live Demo**: `[Your Railway App URL]`
- **Repository**: `[https://github.com/klogins-hash/groq-strands-agent-team](https://github.com/klogins-hash/groq-strands-agent-team)`
- **Groq Console**: `[https://console.groq.com/](https://console.groq.com/)`
- **Strands Agents**: `[https://strandsagents.com/](https://strandsagents.com/)`
- **Railway**: `[https://railway.app/](https://railway.app/)`

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Documentation**: Check the README and inline comments
- **Community**: Join our Discord/Slack community
