class IGDBCover():
    def __init__(self, id, url) -> None:
        self.id = id
        self.url = url

    def __repr__(self) -> str:
        return f'<IGDBCover url={self.url}>'

class IGDBGame():
    def __init__(self, id: int, name: str, cover: IGDBCover=None) -> None:
        self.id = id
        self.name = name
        self.cover = cover

    def __repr__(self) -> str:
        return f'<IGDBGame name={self.name}>'