def solution(dots):
    answer = 0
    for i in range(0, 4):
        v1 = dots[i][0]
        v2 = dots[i][1]

        for j in range(0, 4):
            if(i != j):
                v3 = dots[j][0]
                v4 = dots[j][1]

                r1 = (v4-v2)/(v3-v1)

                for k in range(0, 4):
                    if(i != k and j != k):
                        V1 = dots[k][0]
                        V2 = dots[k][1]

                        for l in range(0, 4):
                            if(i != l and j != l and k != l):
                                V3 = dots[l][0]
                                V4 = dots[l][1]

                                R1 = (V4-V2)/(V3-V1)

                                if(r1 == R1):
                                    answer = 1

    return answer

print(solution([[-1, -1], [3, -1], [3, 2], [-1, 2]]))