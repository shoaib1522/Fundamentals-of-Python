char1=ord(input('enter the character 1'))
char2=ord(input('enter the character 2'))
if (char1-char2==0):
    print(f"'{chr(char1)}'and '{chr(char2)}' are same")
else:
    print(f"'{chr(char1)}'and '{chr(char2)}' are different")