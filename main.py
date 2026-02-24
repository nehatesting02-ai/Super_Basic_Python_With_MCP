from mcp.server.fastmcp import FastMCP
import time
import logging

mcp = FastMCP("add integers") #create an instance of the FastMCP class with the name "add integers"

class MCPError(Exception):
    """Custom exception for MCP errors."""
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"MCPError {code}: {message}")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename= "mcp.log", # This line tell the logging module to write logs to a file named "mcp_server.log"
    filemode="a", #Append to the log file instead of overwriting it each time the server starts
    force=True
) 

logger = logging.getLogger(__name__) # Create a logger object named "MCPServer" to log messages related to the MCP server

@mcp.tool()
def add_integers(a: int, b: int) -> int:
    """Add two integers and return the result.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The sum of the two integers.
    """
    logger.info(f"Adding {a} and {b}")
    result = a + b
    logger.info(f"Result of addition: {result}")
    return result

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two integers and return the result.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        float: The result of dividing the first integer by the second.
    """
    if b == 0:
        raise MCPError(code=400, message="Cannot divide by zero.")
    return a / b

@mcp.tool()
def longprocess(steps: int):
    """Simulate a long process by sleeping for a specified number of steps.
    Args:
        steps (int): The number of steps to simulate. """
    for i in range(steps):
        print(f"Processing Step {i + 1} of {steps}")
        time.sleep(0.1)  # Simulate work by sleeping for 1 second per step
    return "Process complete"


if __name__ == "__main__":
    mcp.run(transport="stdio")