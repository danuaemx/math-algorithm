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
