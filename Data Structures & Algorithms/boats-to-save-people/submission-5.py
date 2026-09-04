class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L, R = 0, len(people)-1
        num_boats = 0

        while L <= R:
            num_boats += 1
            if (limit - people[R]) >= people[L]:
                L += 1
            R -= 1
        return num_boats