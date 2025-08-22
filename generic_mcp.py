import os

from fastmcp import FastMCP
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Create a generic MCP server
mcp = FastMCP("Generic MCP Server")

# Initialize OpenAI API
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key=openai_api_key) if openai_api_key else None

@mcp.tool()
def example_tool(param: str) -> dict:
    """
    Example stub tool for MCP server.
    Args:
        param: Example parameter
    Returns:
        Dictionary with a message
    """
    print(f"Example tool called with param: {param}")
    return {"success": True, "message": f"You sent: {param}"}

if __name__ == "__main__":
    mcp.run()