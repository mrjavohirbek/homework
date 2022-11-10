songs = []

choose = " "


def music():
    print("1 - Create a new song")
    print("2 - Read the playlist")
    print("3 - Update a song")
    print("4 - Delete the playlist")


while True:
    music()
    choose = int(input("Choose the action: "))
    if choose == 1:
        a = input("Create a new song: ")
        songs.append(a)
        print("Added: " + a)
    elif choose == 2:
        songs2 = {}
        n = 0
        for i in songs:
            n += 1
            songs2[n] = i
        print(songs2)
    elif choose == 3:
        songs2 = {}
        n = 0
        for i in songs:
            n += 1
            songs2[n] = i
        print(songs2)
        a = int(input("Update the song: "))
        if a in songs2:
            b = input("New song name: ")
            songs[a] = b
            print("Updated: " + a + " to " + b)
        else:
            print("Song doesn't exist")
    elif choose == 4:
        songs2 = {}
        n = 0
        for i in songs:
            n += 1
            songs2[n] = i
        songs2.clear()
        print("Deleted: " + songs2)
