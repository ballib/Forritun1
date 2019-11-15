#definition for music_func goes here


def music_func(music = "Classic Rock",group = "The Beatles",singer = "Freddie Mercury"):
    print("The best lead vocalist is " + singer)
    print("The best type of music is " + music)
    print("The best music group is " + group)


def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()