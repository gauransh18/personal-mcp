# personal-mcp

A remote MCP server exposing my portfolio data as tools — so any Claude instance can answer questions about me.

## Tools

| Tool | Description |
|---|---|
| `get_profile` | Name, summary, tagline, location, website |
| `get_skills` | Tech skills grouped by category |
| `get_experience` | Work history with highlights |
| `get_projects` | Projects with tech stack and links |
| `get_education` | Education background |
| `get_certifications` | Certs with verification links |
| `get_contact` | Email, GitHub, LinkedIn, Twitter |
| `is_available` | Whether I'm open to new opportunities |

## Connect

Add to Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "gauransh": {
      "url": "https://gauranshsharma.com/mcp/sse"
    }
  }
}
```

Then ask Claude: *"Who is Gauransh and what has he built?"*

## Run locally

```bash
pip install -r requirements.txt
uvicorn server:app --reload
```

## Deploy (Railway)

1. Push to GitHub
2. New project on [railway.app](https://railway.app) → Deploy from GitHub
3. Done — Railway reads `railway.toml` automatically
