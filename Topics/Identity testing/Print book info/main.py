def print_book_info(title, author=None, year=None):
    string = f'"{title}"'
    if author is not None or year is not None:
        string += ' was written'
    if author is not None:
        string += f' by {author}'
    if year is not None:
        string += f' in {year}'
    print(string)
