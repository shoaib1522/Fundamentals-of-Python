def next_vowel(c):
    if ord(c)<ord('E'):
        return 'E'
    elif ord(c) < ord('I'):
        return 'I'
    elif ord(c) < ord('O'):
        return 'O'
    elif ord(c) < ord('U'):
        return 'U'
    else:
        return 'A'
    
def main():
    c=input('Enter the character after which you want to know the vowel: ')
    print(f'the vowel after {c} is {next_vowel(c)}')
main()