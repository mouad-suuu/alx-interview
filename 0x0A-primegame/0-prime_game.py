#!/usr/bin/python3


def sieve_of_eratosthenes(max_n):
    """
    Sieve of Eratosthenes algorithm to find all prime numbers up to max_n.

    Parameters:
    - max_n: Maximum number up to which prime numbers are found.

    Returns:
    - List of prime numbers up to max_n.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_numbers


def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    Parameters:
    - x: Number of rounds.
    - nums: List of integers n for each round.

    Returns:
    - Name of the player that won the most rounds ('Maria' or 'Ben').
      If the winner cannot be determined, return None.
    """
    max_n = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_n)

    dp = [False] * (max_n + 1)

    for i in range(2, max_n + 1):
        dp[i] = False
        for prime in prime_numbers:
            if prime > i:
                break
            if not dp[i - prime]:
                dp[i] = True
                break

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if dp[n]:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
