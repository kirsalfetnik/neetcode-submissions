class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()   
        boat_count = 0

        l, r = 0, len(people)-1

        while (l <= r):
            total_sum = people[l] + people[r]
            
            if total_sum <= limit:
                l += 1

            r -= 1
            boat_count += 1

        return boat_count
