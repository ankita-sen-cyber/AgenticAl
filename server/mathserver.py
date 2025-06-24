from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    :param a: The first integer.
    :param
    b: The second integer.
    :return: The sum of the two integers.
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers together.

    :param a: The first integer.
    :param b: The second integer.
    :return: The product of the two integers.
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")