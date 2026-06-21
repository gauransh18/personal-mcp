import json
import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.responses import JSONResponse
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


# Build the Starlette app manually using the low-level transport
# to avoid TrustedHostMiddleware blocking external connections
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
