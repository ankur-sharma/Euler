def sum(number , end):
    end //= number
    result = end*(end+1)/2
    return result*number
    
A= 3
B = 5
End = 1000 -1
result = sum(A, End) +  sum(B, End) - sum(A*B, End)
print(int(result))
