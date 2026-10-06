class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_decreasing = [(val, i) for i, val in sorted(enumerate(position), key=lambda x: x[1], reverse=True)]
        times = []
        
        for pos, i in pos_decreasing:
            t = (target-pos)/speed[i]
            times.append(t)

        fleets = 0

        while times:
            #main idea is that a car can only
            #form a fleet with a car that:
            # (1) is in front of it in position
            # (2) it is faster than -> quicker time to target
            currTime = times.pop()
            while times and currTime <= times[-1]:
                currTime = times.pop()
            fleets += 1
        return fleets    
            




        