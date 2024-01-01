from collections import Counter
from functools import cmp_to_key
from os import path
from time import perf_counter

from icecream import ic

example = path.join(path.dirname(path.abspath(__file__)), "./example.txt")
puzzle = path.join(path.dirname(path.abspath(__file__)), "./puzzle.txt")

timer = perf_counter()

hands = []
bids = []

with open(puzzle) as f:
    for line in f.readlines():
        l_split = line.split()

        hands.append(l_split[0])
        bids.append(int(l_split[1]))

hands_type = {
    "five_of_a_kind": [],
    "four_of_a_kind": [],
    "full_house": [],
    "three_of_a_kind": [],
    "two_pair": [],
    "one_pair": [],
    "high_card": [],
}

for hand in hands:
    hand_counter = Counter(hand)

    J_count = hand_counter.get("J", 0)

    if len(hand_counter) > 1:
        del hand_counter["J"]

    hand_highest_count = hand_counter.most_common()[0][1] + J_count

    match len(hand_counter):
        case 1:
            hands_type["five_of_a_kind"].append(hand)
        case 2:
            t = "four_of_a_kind" if hand_highest_count == 4 else "full_house"
            hands_type[t].append(hand)
        case 3:
            t = "three_of_a_kind" if hand_highest_count == 3 else "two_pair"
            hands_type[t].append(hand)
        case 4:
            hands_type["one_pair"].append(hand)
        case 5:
            hands_type["high_card"].append(hand)


def hand_cmp(hand_1, hand_2):
    card_ranks = "AKQT98765432J"
    card_1, card_2 = hand_1[0], hand_2[0]

    rank_card_1 = card_ranks.index(card_1)
    rank_card_2 = card_ranks.index(card_2)

    result_cmp = 1 if rank_card_1 > rank_card_2 else -1

    if len(hand_1) == 1:
        return result_cmp

    if rank_card_1 == rank_card_2:
        return hand_cmp(hand_1[1:], hand_2[1:])

    return result_cmp


hands_count = len(hands)
total_winnings = 0

for hand_type_values in hands_type.values():
    for hand in sorted(hand_type_values, key=cmp_to_key(hand_cmp)):
        total_winnings += hands_count * bids[hands.index(hand)]
        hands_count -= 1

ic(total_winnings)

exec_time = perf_counter() - timer
ic(exec_time)
