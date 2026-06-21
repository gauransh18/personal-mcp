import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mcp.server.fastmcp import FastMCP
from data import PROFILE, AVAILABILITY, SKILLS, EXPERIENCE, PROJECTS, EDUCATION, CERTIFICATIONS

mcp = FastMCP(
    "Gauransh Sharma",
    instructions=(
        "This MCP server provides live information about Gauransh Sharma — "
        "a full-stack engineer specializing in LLM systems, RAG pipelines, and mobile. "
        "Use it to answer any questions about his background, skills, projects, availability, or contact details."
    ),
)


@mcp.tool()
def get_profile() -> str:
    """Get Gauransh's name, summary, tagline, location, and website."""
    return json.dumps(PROFILE, indent=2)


@mcp.tool()
def get_skills() -> str:
    """Get Gauransh's technical skills grouped by category: Languages, Mobile, AI & Data, Backend, DevOps."""
    return json.dumps(SKILLS, indent=2)


@mcp.tool()
def get_experience() -> str:
    """Get Gauransh's full work history — companies, roles, dates, and what he built."""
    return json.dumps(EXPERIENCE, indent=2)


@mcp.tool()
def get_projects() -> str:
    """Get Gauransh's notable projects with descriptions, tech stack, and links."""
    return json.dumps(PROJECTS, indent=2)


@mcp.tool()
def get_education() -> str:
    """Get Gauransh's educational background."""
    return json.dumps(EDUCATION, indent=2)


@mcp.tool()
def get_certifications() -> str:
    """Get Gauransh's certifications with verification links."""
    return json.dumps(CERTIFICATIONS, indent=2)


@mcp.tool()
def get_contact() -> str:
    """Get Gauransh's contact information: email, GitHub, LinkedIn, Twitter."""
    return json.dumps({
        "email": PROFILE["email"],
        "github": PROFILE["github"],
        "linkedin": PROFILE["linkedin"],
        "twitter": PROFILE["twitter"],
        "website": PROFILE["website"],
    }, indent=2)


@mcp.tool()
def is_available() -> str:
    """Check if Gauransh is currently open to new work opportunities."""
    return json.dumps(AVAILABILITY, indent=2)


app = FastAPI()


@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})


app.mount("/mcp", mcp.sse_app())
