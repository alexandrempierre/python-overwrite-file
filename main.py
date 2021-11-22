#!/usr/bin/env python3

'''main module
'''


__all__ = []
__author__ = 'Alexandre Pierre'

if __name__ == '__main__':
    with open('file.txt', 'w') as file_ptr:
        for i in range(1000):
            file_ptr.write(f'Line {i + 1}\n')

    with open('file.txt', 'r') as file_ptr:
        content = file_ptr.read()

    with open('file.txt', 'w') as file_ptr:
        file_ptr.write('New contents')

    with open('file.txt', 'r') as file_ptr:
        new_content = file_ptr.read()
        print(f'''Differences between second and first files

Old:
{content}

Current:
{new_content}

Is in new but not in old:
{new_content.replace(content, "")}''')
