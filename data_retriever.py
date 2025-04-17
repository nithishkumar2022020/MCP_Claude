from mcp.server.fastmcp import FastMCP
import os
from PyPDF2 import PdfReader
mcp = FastMCP("SmartContext")

# Hardcoded path to your PDF file
LEAVE_POLICY_PDF = "/Users/reddyvarinithishkumarreddy/Documents/Books/AI:ML/Hands-On Large Language Models (Jay Alammar) (Z-Library).pdf"

@mcp.tool()
def fetch_context(query: str) -> str:
    """Fetch content from a Hands on LLM PDF based on the query."""
    query_lower = query.lower()

    # Only process if "llm" is in the query
    if "llm" not in query_lower:
        return "This tool only answers Gen AI related questions!"

    print(f"Checking if file exists at: {LEAVE_POLICY_PDF}")
    if not os.path.exists(LEAVE_POLICY_PDF):
        return f"Error: PDF not found at {LEAVE_POLICY_PDF}!"

    try:
        print("Attempting to read the PDF...")
        with open(LEAVE_POLICY_PDF, "rb") as f:
            pdf_reader = PdfReader(f)
            print(f"Successfully opened PDF with {len(pdf_reader.pages)} pages.")

            content = ""
            for page in pdf_reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    content += extracted_text + "\n"

            if not content:
                return "Error: No text could be extracted from the PDF!"

        print("Returning content...")
        return (f"Using context from {LEAVE_POLICY_PDF}:\n\n"
                f"Content:\n{content}\n\n"
                f"Query: {query}\n\n"
                f"Please answer based on the content above.")

    except Exception as e:
        print(f"Exception occurred: {e}")
        return f"Error reading the book: {str(e)}"

if __name__ == "__main__":
    mcp.run()