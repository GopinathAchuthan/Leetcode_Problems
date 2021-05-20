class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pointer_1 = 0
        pointer_2 = 1
        
        while(pointer_2<len(asteroids)):
            if asteroids[pointer_1]>0 and asteroids[pointer_2]<0:
                if asteroids[pointer_1] > -(asteroids[pointer_2]):
                    asteroids.pop(pointer_2)
                elif asteroids[pointer_1] < -(asteroids[pointer_2]):
                    asteroids.pop(pointer_1)
                    if pointer_1 != 0:
                        pointer_1 -= 1
                        pointer_2 = pointer_1+1
                else:
                    asteroids.pop(pointer_2)
                    asteroids.pop(pointer_1)
                    if pointer_1 != 0:
                        pointer_1 -= 1
                        pointer_2 = pointer_1+1 
                        
            else:
                pointer_1 += 1
                pointer_2 += 1
        
        return asteroids