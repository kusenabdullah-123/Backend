list_Game = ['Game PC', 'Game Android', 'Game Playstation']
list_Game_Pc = ['Assassin Cread', 'Call Of Duty', 'Battlefield', 'Valorant']
list_Game_Android = ['PUBG', 'Call Of Duty Mobile',
                     'Genshin Impact', 'Pokemon Unite']
list_Game_PS = ['God Of War', 'Ghost Of Tsushima',
                'Mortal Kombat', 'Resident Evil']
cart = []
while True:
    print('==================')
    for item in range(0, len(list_Game)):
        print(f'{item + 1}. {list_Game[item]} ')
    game = input('Silahkan Pilih Platfom 1-3 ')
    if game == '1':
        for item_game in range(0, len(list_Game_Pc)):
            print(f'{item_game + 1}. {list_Game_Pc[item_game]} ')
        ulang = True
        while ulang:
            select_game = int(
                input(f'Silahkan Pilih Game 1-{len(list_Game_Pc)} '))
            if select_game <= 0 or select_game > len(list_Game_Pc):
                print('silahkan masukan menu dengan benar')
                for item_game in range(0, len(list_Game_Pc)):
                    print(f'{item_game + 1}. {list_Game_Pc[item_game]} ')
                continue
            else:
                cart.append(list_Game_Pc[select_game - 1])
                print('==== list game ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                ulang = False
            continue
    elif game == '2':
        for item_game2 in range(0, len(list_Game_Android)):
            print(f'{item_game2 + 1}. {list_Game_Android[item_game2]} ')
        ulang = True
        while ulang:
            select_game = int(
                input(f'Silahkan Pilih Game 1-{len(list_Game_Android)} '))
            if select_game <= 0 or select_game > len(list_Game_Android):
                print('silahkan masukan menu dengan benar')
                for item_game2 in range(0, len(list_Game_Android)):
                    print(
                        f'{item_game2 + 1}. {list_Game_Android[item_game2]} ')
            else:
                cart.append(list_Game_Android[select_game - 1])
                print('==== list game ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
                continue
    elif game == '3':
        for item_game3 in range(0, len(list_Game_PS)):
            print(f'{item_game3 + 1}. {list_Game_PS[item_game3]} ')
        ulang = True
        while ulang:
            select_game = int(
                input(f'Silahkan Pilih Game 1-{len(list_Game_PS)} '))
            if select_game <= 0 or select_game > len(list_Game_PS):
                print('silahkan masukan menu dengan benar')
                for item_game3 in range(0, len(list_Game_PS)):
                    print(f'{item_game3 + 1}. {list_Game_PS[item_game3]} ')
            else:
                cart.append(list_Game_PS[select_game - 1])
                print('==== list game ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
            continue
    else:
        print('game tidak ditemukan')
        continue
    pilih = input('Apakah Pilih Lagi ?')
    if pilih == 'y':
        continue
    else:
        print('==== list game ====')
        for list_cart in range(0, len(cart)):
            print(f'{list_cart +1} . {cart[list_cart]}')
        break
