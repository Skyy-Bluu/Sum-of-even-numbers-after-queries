def sumEvenAfterQueries(A, queries):
    out = []
    for query in queries:
        adder, nth = query[0], query[1]
        A[nth] += adder
        even_sum = 0
        for a in A:
            if a%2 == 0:
                even_sum += a
        out.append(even_sum)
    print[out]


A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

sumEvenAfterQueries(A, queries)
