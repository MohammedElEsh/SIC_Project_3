def destroy_page(page):
    """Destroys a Tkinter page safely."""
    try:
        page.destroy()
    except:
        pass

def quick_sort_price(items):
    """
    Sorts a list of products by price in ascending order using QuickSort.
    Args:
        items: List of dictionaries, each containing a 'price' key.
    Returns:
        Sorted list of products.
    """
    def partition(low, high):
        pivot = items[high]['price']
        i = low - 1
        for j in range(low, high):
            if items[j]['price'] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    def quick_sort(low, high):
        stack = [(low, high)]
        while stack:
            low, high = stack.pop()
            if low < high:
                pivot_index = partition(low, high)
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))

    if items:
        quick_sort(0, len(items) - 1)
    return items