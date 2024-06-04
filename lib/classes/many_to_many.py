class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Names must be of type str and longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Names must be of type str and between 2 and 16 characters, inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Categories must be of type str and longer than 0 characters")
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        result = [author for author, count in authors_count.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag._articles))
class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Titles must be of type str and between 5 and 50 characters, inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
