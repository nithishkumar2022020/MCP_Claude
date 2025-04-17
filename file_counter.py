from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server named "FileCounter"
mcp = FastMCP("FileCounter")

@mcp.tool()
def count_desktop_files() -> str:
    """
    Count the number of files on the desktop.
    """
    # Get the desktop path (e.g., /Users/apoorv/Desktop or C:\Users\apoorv\Desktop)
    desktop_path = os.path.expanduser("~/Desktop")

    try:
        # List all items in the desktop directory, filter to include only files
        files = [
            f for f in os.listdir(desktop_path)
            if os.path.isfile(os.path.join(desktop_path, f))
        ]
        file_count = len(files)  # Count the number of files
        return f"There are {file_count} files on your desktop."

    except Exception as e:
        # Handle any errors gracefully
        return f"Error counting files: {str(e)}"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()