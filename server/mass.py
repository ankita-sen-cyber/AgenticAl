from mcp.server.fastmcp import FastMCP
import mass_ts as mts
mcp = FastMCP("mass")
@mcp.tool()
def similaritySearch(q:list,d:list) -> list:
    """
    Perform a similarity search using the provided query and data.

    :param q: The query string to search for.
    :param d: The data string to search within.
    :return: A list of results from the similarity search.
    """
    result= mts.mass2(d, q)
    print(result)
    return result

if __name__ == "__main__":
    # similaritySearch([1,2,3],[1,2,3,4,4,5,6,7,8,9])
    mcp.run(transport="stdio")