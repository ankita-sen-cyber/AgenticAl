from mcp.server.fastmcp import FastMCP
import mass_ts as mts
import numpy as np

mcp = FastMCP("mass")

@mcp.tool()
def similaritySearch(d: list, q: list) -> list:
    """
    Perform a similarity search using the provided query and data.
    Select the top 3 matches.

    :param q: The query string to search for.
    :param d: The data string to search within.
    :return: A list of top 3 matches.
    """
    # Perform similarity search
    result = mts.mass2(d, q)
    result = np.real(result).astype(float)

    # Sort results by similarity score (descending)
    sorted_indices = np.argsort(result)[::-1]
    top_matches = []
    query_length = len(q)

    for idx in sorted_indices:
        if len(top_matches) >= 3:
            break

        # Calculate overlap
        start_idx = idx
        end_idx = idx + query_length
        overlap = min(query_length, end_idx - start_idx) / query_length

        # Add match if overlap is at least 50% but not 100%
        if 0.5 <= overlap < 1.0:
            top_matches.append((idx, result[idx]))

    print("Top matches:", top_matches)
    return top_matches

if __name__ == "__main__":
    # Example usage
    # similaritySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3])
    mcp.run(transport="stdio")