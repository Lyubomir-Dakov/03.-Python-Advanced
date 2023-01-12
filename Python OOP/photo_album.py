from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) == PhotoAlbum.PHOTOS_PER_PAGE:
                continue
            self.photos[page].append(label)
            return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        dash_line = '-' * 11 + '\n'
        result = dash_line
        for page in self.photos:
            result += ('[] ' * len(page)).strip() + '\n' + dash_line
        return result.strip()

    def __init_photos(self, pages):
        return [[] for _ in range(pages)]


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
