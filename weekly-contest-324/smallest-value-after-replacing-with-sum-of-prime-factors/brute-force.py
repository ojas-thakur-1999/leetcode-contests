class Solution:
    def smallestValue(self, n: int) -> int:
        prime_factors = self.getPrimeFactors(n)
        if len(prime_factors) == 1 or len(prime_factors) == 0:
            return n
        
        sum_of_prime_factors = 0
        for factor in prime_factors:
            sum_of_prime_factors += factor
        
        if sum_of_prime_factors == n:
            return n
        
        return self.smallestValue(sum_of_prime_factors)

    def getPrimeFactors(self, n):
        prime_factors = []
        for i in range(1, n+1):
            if n%i == 0:
                factors = 0
                for j in range(1, i+1):
                    if i%j == 0:
                        factors += 1
                if factors == 2:
                    prime_factors.append(i)

        all_prime_factors = []
        for prime_factor in prime_factors:
            while n%prime_factor == 0:
                all_prime_factors.append(prime_factor)
                n = n // prime_factor
        
        return all_prime_factors

# ans = Solution().smallestValue(15)
# ans = Solution().smallestValue(5)
# ans = Solution().smallestValue(1)
ans = Solution().smallestValue(4)

print(ans)
