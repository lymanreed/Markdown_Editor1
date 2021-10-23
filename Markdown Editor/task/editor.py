def plain():
    return input('Text: ')


def bold():
    return f'**{input("Text:")}**'


def italic():
    return f'*{input("Text:")}*'


def header():
    while True:
        level = int(input('Level: '))
        if level not in range(1, 7):
            print('The level should be within the range of 1 to 6')
        else:
            break
    return f'{"#" * level} {input("Text:")}\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def code():
    return f'`{input("Text:")}`'


def new_line():
    return '\n'


def oulist(list_type):
    while True:
        num_rows = int(input('Number of rows:'))
        if num_rows > 0:
            break
        else:
            print('The number of rows should be greater than zero')
    return_value = ''
    for i in range(1, num_rows + 1):
        starter = '* ' if list_type == 'unordered-list' else f'{i}. '
        row_value = input(f'Row #{i}')
        return_value += starter + row_value + '\n'
    return return_value


def main():
    formatters = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header,
                  'link': link, 'inline-code': code, 'new-line': new_line,
                  'ordered-list': oulist, 'unordered-list': oulist}
    commands = ['!help', '!done']
    output = ''

    while True:
        formatter_choice = input('Choose a formatter: ')
        if formatter_choice == '!done':
            with open('output.md', 'w') as file:
                file.write(output)
            break
        elif formatter_choice == '!help':
            print('Available formatters:', ' '.join(formatters))
            print('Special commands:', ' '.join(commands))
        elif formatter_choice in formatters.keys():
            if formatter_choice == 'ordered-list' or formatter_choice == 'unordered-list':
                output += formatters[formatter_choice](formatter_choice)
            else:
                output += formatters[formatter_choice]()
            print(output)
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
