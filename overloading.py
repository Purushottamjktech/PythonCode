class Solution:

    def add(self, *other):
        output =0

        for i in other:
            output += i

        print(f'output is {output}')

p = Solution()
m = Solution()

m.add(9,1)
p.add(10,80,97)
p.add(79,5)
