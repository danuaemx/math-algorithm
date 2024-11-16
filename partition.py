from numba import jit

@jit(nopython=True)
def partition_p(m,n,p=1,k=2):
    while k<=m and k<=n:
        if m==k:
            p += 1
        else:
            p += partition_p(m-k,k)
        k += 1
    return p

def partition(n):
  return partition_p(n,n)
    
@jit(nopython=True)
def partition_iterative(n):
    P = [0] * (n + 1)
    P[0] = 1
    
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            P[m] += P[m - k]
    
    return P[n]
