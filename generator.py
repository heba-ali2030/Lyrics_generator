# check validation of user input
def check_selection (user_selection):
    selections = [ 'A' , 'a' , 'S' , 's']
    while user_selection not in selections:
        print('please type a or s no other letters to complete!')
        user_selection = input(' please type A to select songs by Artists or S to choose by song! \n ').casefold()
    else:
        pass
    return user_selection

# check validation o song numbers
def check_number(song_choice):
    while song_choice.isdigit()== False:
        print('please enter valid number ^_^')
        song_choice = input( 'please type the number of the song you want to play from the previous list :\n')
    return int (song_choice)

#put songs in a list
songs = ['Baby by Bieber', 'Hotline Bling by Drake' , 'Flawless by Beyonce', 'Fall by Eminem', 'Started From the Bottom by Drake']

# ask the user to choose by song or artist
user_selection = check_selection(input ('please type A to select songs by Artists or S to choose by song! \n ')).casefold()

# 1 - if he choose by song:
if user_selection == 's'.casefold():
    
    # print the songs list 
    print(f'Welcome, please select a song from this top 5 songs: ')
    for (index,song) in enumerate (songs, start= 1):
        print(index, song)
    
# tell the user to put the index of the song 
song_choice = check_number(input( 'please type the number of the song you want to play from the previous list :\n'))

# print the song name according to user choice
for (index,song) in enumerate (songs, start= 1):

    if song_choice == 1:
        print(f'You chose {songs[0]}. Here you go: ')

        # print the lyrics of the song he choose
        print (f'----- {songs[0]} -----')
        print(f' Ooh, ooh \n Across the ocean, across the sea \n Startin to forget the way you look at me now\n Over the mountains, across the sky\n Need to see your face \n I need to look in your eyes \n Through the storm and through the clouds\n Bumps in the road and upside down now \n I know it\'s hard babe, to sleep at night\n Don\'t you worry\n Cause everything\'s gonna be alright, ai-ai-ai-a\'ight\n Be alright, ai-ai-ai-a\'ight.')
        break
    elif song_choice  == 2:
        print(f'You chose {songs[1]}. Here you go: ')

        # print the lyrics of the song he choose
        print (f'----- {songs[1]} -----')
        print (f'You used to call me on my cell phone \n Late night when you need my love \n Call me on my cell phone \n Late night when you need my love \n And I know when that hotline bling \n That can only mean one thing \n I know when that hotline bling \n That can only mean one thing')
        break

    elif song_choice  == 3:
        print(f'You chose {songs[2]}. Here you go: ')

        # print the lyrics of the song he choose
        print (f'----- {songs[2]} -----')
        print (f'I\'m out that H, town coming coming down\n I\'m coming down, drippin\' candy on the ground\n H, Town, Town, I\'m coming down, coming down\n Drippin\' candy on the ground...')
        break
    elif song_choice == 4:
        print(f'You chose {songs[3]}. Here you go: ')

        # print the lyrics of the song he choose
        print (f'----- {songs[3]} -----')
        print (f'Don\'t fall on my face \n Don\'t fall on my faith, oh \n Don\'t fall on my fate \n Don\'t fall on my faith, oh \n Don\'t fall on my fate \n Don\'t fall on my')
        break
    else:
        print(f'You chose {songs[4]}. Here you go: ')

        # print the lyrics of the song he choose
        print (f'----- {songs[4]} -----')
        print (f'I done kept it real from the jump \n Living at my mama house we\'d argue every month \n Nigga, I was tryna get it on my own \n Workin\' all night, traffic on the way home \n And my uncle calling me like, "Where ya at? \n I gave you the keys told you bring it right back" \n Nigga, I just think it\'s funny how it goes \n Now I\'m on the road, half a million for a show')
        break

        

# 2- if he choose artist:
# ask the user to type name of artists available 


# tell him the songs of the artist to choose from 

# print user choice 

# print song lyrics


# ask the user to type * to choose again


