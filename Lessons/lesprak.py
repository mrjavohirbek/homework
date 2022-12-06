nums = [1, 4, 45, 67, 433, 9]
m = 0
for i in nums:
    m += i

print(m)

b = 0
a = 0

while a < len(nums):
    b += nums[a]
    a += 1

print(b)


def is_prime(n):

    if n < 2:

        return False

    if n == 2:

        return True

    limit = n**(1/2)

    i = 2

    while i <= limit:

        if n % i == 0:

            return False

        i += 1

    return True


print(is_prime(int(input("Enter: "))))
