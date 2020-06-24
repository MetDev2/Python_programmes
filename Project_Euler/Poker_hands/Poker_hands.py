def poker_hands(filename):
    list_of_value_lists = []
    list_of_suit_sets = []
    first_player_wins = 0
    with open(filename) as poker:
        for line in poker:
            line.strip()
            a = {i for i in line[1:15:3]}
            b = {i for i in line[16:29:3]}
            list_of_suit_sets.append([a, b])
            c = []
            for i in line[0:15:3]:
                if i == 'A':
                    c.append(14)
                elif i == 'K':
                    c.append(13)
                elif i == 'Q':
                    c.append(12)
                elif i == 'J':
                    c.append(11)
                elif i == 'T':
                    c.append(10)
                else:
                    c.append(int(i))
            d = []
            for i in line[15:29:3]:
                if i == 'A':
                    d.append(14)
                elif i == 'K':
                    d.append(13)
                elif i == 'Q':
                    d.append(12)
                elif i == 'J':
                    d.append(11)
                elif i == 'T':
                    d.append(10)
                else:
                    d.append(int(i))
            list_of_value_lists.append([sorted(c), sorted(d)])

    for i, hands in enumerate(list_of_value_lists):
        highest_card_1 = 0
        highest_card_1_pair = []
        highest_card_1_three = 0
        highest_card_2 = 0
        highest_card_2_pair = []
        highest_card_2_three = 0
        combination_1 = 0
        combination_2 = 0
        if len(list_of_suit_sets[i][0]) == 1:
            combination_1 += 5
        street = [j for j in range(hands[0][0], hands[0][0] + 5, 1)]
        if hands[0] == street:
            combination_1 += 4
            highest_card_1 = hands[0][4]
        if combination_1 == 0:
            for k in hands[0]:
                if combination_1 == 4:
                    combination_1 = 6
                    break
                if hands[0].count(k) == 4:
                    combination_1 += 7
                    highest_card_1 = k
                    break
                if hands[0].count(k) == 3 and combination_1 != 3:
                    combination_1 += 3
                    highest_card_1_three = k
                if hands[0].count(k) == 2:
                    if k not in highest_card_1_pair:
                        combination_1 += 1
                        highest_card_1_pair.append(k)

        if len(list_of_suit_sets[i][1]) == 1:
            combination_2 += 5
        street = [j for j in range(hands[1][0], hands[1][0] + 5, 1)]
        if hands[1] == street:
            combination_2 += 4
            highest_card_2 = hands[1][4]
        if combination_2 == 0:
            for k in hands[1]:
                if combination_2 == 4:
                    combination_2 = 6
                    break
                elif hands[1].count(k) == 4:
                    combination_2 += 7
                    highest_card_2 = k
                    break
                elif hands[1].count(k) == 3 and combination_2 != 3:
                    combination_2 += 3
                    highest_card_2_three = k
                elif hands[1].count(k) == 2:
                    if k not in highest_card_2_pair:
                        combination_2 += 1
                        highest_card_2_pair.append(k)
                

        if combination_1 > combination_2: first_player_wins += 1
        elif combination_1 == combination_2:
            if combination_1 == 4 or combination_1 == 9 or combination_1 == 7:
                if highest_card_1 > highest_card_2: first_player_wins += 1
            
            elif combination_1 == 3:
                if highest_card_1_three > highest_card_2_three:
                    first_player_wins += 1
                
            elif combination_1 == 6:
                if highest_card_1_three > highest_card_2_three:
                    first_player_wins += 1
                elif highest_card_1_pair[0] > highest_card_2_pair[0]:
                    first_player_wins += 1
                
            elif combination_1 == 2:
                if max(highest_card_1_pair) > max(highest_card_2_pair):
                    first_player_wins += 1
                elif min(highest_card_1_pair) > min(highest_card_2_pair):
                    first_player_wins += 1
                elif sum(hands[0]) > sum(hands[1]):
                    first_player_wins += 1
                
            elif combination_1 == 1:
                if highest_card_1_pair[0] > highest_card_2_pair[0]:
                    first_player_wins += 1
                elif highest_card_1_pair[0] == highest_card_2_pair[0]:
                    hands[0].remove(highest_card_1_pair[0])
                    hands[0].remove(highest_card_1_pair[0])
                    hands[1].remove(highest_card_1_pair[0])
                    hands[1].remove(highest_card_1_pair[0])
                    while max(hands[0]) == max(hands[1]):
                        hands[0].remove(max(hand[0]))
                        hands[1].remove(max(hand[1]))
                    if max(hands[0]) > max(hands[1]):
                        first_player_wins += 1

            elif combination_1 == 0 or combination_1 == 5:
                while max(hands[0]) == max(hands[1]):
                    hands[0].remove(max(hands[0]))
                    hands[1].remove(max(hands[1]))
                if max(hands[0]) > max(hands[1]):
                    first_player_wins += 1

    return first_player_wins



if __name__ == '__main__':
    print(poker_hands('poker.txt'))



        
