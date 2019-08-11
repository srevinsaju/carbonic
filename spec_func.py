# spec function

# pyinstaller exe file size reduced with the help of https://github.com/pyinstaller/pyinstaller/issues/2270
# Thanks to solution by @choice17


Key = ['Qt5Qml','Qt5Quick', 'Qt5Network']

def remove_from_list(input, keys):
    outlist = []
    for item in input:
        name, _, _ = item
        flag = 0
        for key_word in keys:
            if name.find(key_word) > -1:
                flag = 1
        if flag != 1:
            outlist.append(item)
    return outlist

a.binaries = remove_from_list(a.binaries, Key)