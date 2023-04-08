"""
You will complete the PaginationHelper class, which is a utility
class helpful for querying paging information related to an array.
The class is designed to take in an array of values and an integer
indicating how many items will be allowed per each page.
The types of values contained within the collection/array are not relevant.
"""


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection: list, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        result = len(self.collection) / self.items_per_page
        if result % self.items_per_page != 0:
            return len(self.collection) // self.items_per_page + 1
        return int(result)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        check_page = self.page_count() - 1  # 2
        if page_index <= check_page:
            return len(
                self.collection[
                    self.items_per_page * page_index:self.items_per_page * (
                        page_index + 1)
                    ]
                )
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        items = self.item_count()
        if 0 <= item_index < items:
            return item_index // self.items_per_page
        return -1


arr = ['a', 'b', 'c', 'd', 'e', 'f']
pages = 4
helper = PaginationHelper(arr, pages)
print(helper.page_count())  # 2
print(helper.item_count())  # 6
print(helper.page_item_count(0))  # 4
print(helper.page_item_count(1))  # 2
print(helper.page_item_count(2))  # -1
print(helper.page_index(5))  # 1 (zero based index)
print(helper.page_index(2))  # 0
print(helper.page_index(20))  # -1
print(helper.page_index(-10))  # -1 because negative indexes are invalid
