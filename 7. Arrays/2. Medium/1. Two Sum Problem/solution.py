def read(n: int, book: [int], target: int) -> str:
    pages_map = {}
    for pages in book:
        remaining_pages = target - pages
        pages_map[remaining_pages] = pages
    for pages in book:
        if pages in pages_map:
            return "YES"
    return "NO"
