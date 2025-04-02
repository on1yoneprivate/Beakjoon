# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 제시된 수도 코드 : 이중 반복문 -> 시간 복잡도 : O(n**2)

n = int(input())

print(n**2)
print(2)        # 시간 복잡도의 최고 차항 : 2