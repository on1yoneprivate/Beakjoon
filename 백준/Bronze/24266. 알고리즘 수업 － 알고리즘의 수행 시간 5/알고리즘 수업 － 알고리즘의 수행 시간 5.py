# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# 제시된 수도 코드 : 삼중 반복문 -> 시간 복잡도 : O(n**3)

n = int(input())

print(n**3)
print(3)        # 시간 복잡도의 최고 차항 : 3
