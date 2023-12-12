from collections import Counter
from enum import Enum

CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

CARD_VALUES_JOKER = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


def evaluate_hand(hand: str) -> HandType:
    assert len(hand) == 5
    counter = Counter(hand)
    value_counts = sorted(list(counter.values()), reverse=True)
    if value_counts == [1, 1, 1, 1, 1]:
        return HandType.HIGH_CARD
    elif value_counts == [2, 1, 1, 1]:
        return HandType.ONE_PAIR
    elif value_counts == [2, 2, 1]:
        return HandType.TWO_PAIR
    elif value_counts == [3, 1, 1]:
        return HandType.THREE_KIND
    elif value_counts == [3, 2]:
        return HandType.FULL_HOUSE
    elif value_counts == [4, 1]:
        return HandType.FOUR_KIND
    elif value_counts == [5]:
        return HandType.FIVE_KIND
    else:
        raise ValueError(f"Bad hand {hand} with {value_counts}")


def evaluate_hand_joker(hand: str) -> HandType:
    assert len(hand) == 5
    counter = Counter(hand)
    value_counts = sorted(list(counter.values()), reverse=True)
    joker_count = counter.get("J", 0)
    if value_counts == [1, 1, 1, 1, 1]:
        if joker_count == 0:
            return HandType.HIGH_CARD
        else:
            return HandType.ONE_PAIR
    elif value_counts == [2, 1, 1, 1]:
        if joker_count == 0:
            return HandType.ONE_PAIR
        else:
            return HandType.THREE_KIND
    elif value_counts == [2, 2, 1]:
        if joker_count == 0:
            return HandType.TWO_PAIR
        elif joker_count == 1:
            return HandType.FULL_HOUSE
        else:
            return HandType.FOUR_KIND
    elif value_counts == [3, 1, 1]:
        if joker_count == 0:
            return HandType.THREE_KIND
        elif joker_count == 1:
            return HandType.FOUR_KIND
        else:
            return HandType.FOUR_KIND
    elif value_counts == [3, 2]:
        if joker_count == 0:
            return HandType.FULL_HOUSE
        else:
            return HandType.FIVE_KIND
    elif value_counts == [4, 1]:
        if joker_count == 0:
            return HandType.FOUR_KIND
        else:
            return HandType.FIVE_KIND
    elif value_counts == [5]:
        return HandType.FIVE_KIND
    else:
        raise ValueError(f"Bad hand {hand} with {value_counts}")


def sort_key(hand_and_bid: tuple[str, int]):
    hand = hand_and_bid[0]
    return (evaluate_hand(hand).value,) + tuple(CARD_VALUES[c] for c in hand)


def sort_key_joker(hand_and_bid: tuple[str, int]):
    hand = hand_and_bid[0]
    return (evaluate_hand_joker(hand).value,) + tuple(
        CARD_VALUES_JOKER[c] for c in hand
    )


def part1(input: str):
    hands_and_bids = [line.strip().split() for line in input.splitlines()]
    hands_and_bids = [(h, int(b)) for h, b in hands_and_bids]
    sorted_hands_and_bids = sorted(hands_and_bids, key=sort_key)

    total_score = 0
    for i, (h, b) in enumerate(sorted_hands_and_bids, 1):
        total_score += i * b
    return total_score


def part2(input: str):
    hands_and_bids = [line.strip().split() for line in input.splitlines()]
    hands_and_bids = [(h, int(b)) for h, b in hands_and_bids]
    sorted_hands_and_bids = sorted(hands_and_bids, key=sort_key_joker)

    total_score = 0
    for i, (h, b) in enumerate(sorted_hands_and_bids, 1):
        total_score += i * b
    return total_score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input1 = f.read()
    print(part1(input1))
    with open("input.txt", "r") as f:
        input2 = f.read()
    print(part2(input2))
