from mcp.server.fastmcp import FastMCP

#create an mcp server named greeter
mcp=FastMCP("greeter")

@mcp.tool()
def greet() -> str:
    """Return this welcome message, when greeted with "Hi", "Hey" or "Hello". """
    return "Hey nithish, welcome to MCP!"

if __name__ == "__main__":
    mcp.run()