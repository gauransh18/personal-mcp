import json
import os
import time
import uvicorn
import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.responses import JSONResponse

PROFILE_URL = "https://gauranshsharma.com/profile.json"
CACHE_TTL = 300  # 5 minutes

_cache: dict = {"data": None, "at": 0}


def get_profile_data() -> dict:
    now = time.time()
    if _cache["data"] is None or now - _cache["at"] > CACHE_TTL:
        response = httpx.get(PROFILE_URL, timeout=10)
        response.raise_for_status()
        _cache["data"] = response.json()
        _cache["at"] = now
    return _cache["data"]


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
    d = get_profile_data()
    return json.dumps({k: d[k] for k in ("name", "tagline", "summary", "location", "website", "email", "github", "linkedin", "twitter")}, indent=2)


@mcp.tool()
def get_skills() -> str:
    """Get Gauransh's technical skills grouped by category: Languages, Mobile, AI & Data, Backend, DevOps."""
    return json.dumps(get_profile_data()["skillCategories"], indent=2)


@mcp.tool()
def get_experience() -> str:
    """Get Gauransh's full work history — companies, roles, dates, and what he built."""
    return json.dumps(get_profile_data()["work"], indent=2)


@mcp.tool()
def get_projects() -> str:
    """Get Gauransh's notable projects with descriptions, tech stack, and links."""
    return json.dumps(get_profile_data()["projects"], indent=2)


@mcp.tool()
def get_education() -> str:
    """Get Gauransh's educational background."""
    return json.dumps(get_profile_data()["education"], indent=2)


@mcp.tool()
def get_certifications() -> str:
    """Get Gauransh's certifications with verification links."""
    return json.dumps(get_profile_data()["certifications"], indent=2)


@mcp.tool()
def get_contact() -> str:
    """Get Gauransh's contact information: email, GitHub, LinkedIn, Twitter."""
    d = get_profile_data()
    return json.dumps({k: d[k] for k in ("email", "github", "linkedin", "twitter", "website")}, indent=2)


@mcp.tool()
def is_available() -> str:
    """Check if Gauransh is currently open to new work opportunities."""
    return json.dumps(get_profile_data()["availability"], indent=2)


sse = SseServerTransport("/messages/")


async def handle_sse(request: Request):
    async with sse.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await mcp._mcp_server.run(
            streams[0], streams[1],
            mcp._mcp_server.create_initialization_options(),
        )


async def health(request: Request):
    return JSONResponse({"status": "ok"})


app = Starlette(routes=[
    Route("/health", health),
    Route("/sse", handle_sse),
    Mount("/messages/", app=sse.handle_post_message),
])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
