# def head(L):
#     return L[0]
 
# def tail(L):
#     return L[1]

# def py2ll(L):
#     if not L:
#         return None
#     else :
#         return  (L[0] ,py2ll(L[1:]))

# def ll2py(L):
#     if not L :
#         return []
#     else :
#         h0 = head(L)
#         T0 = tail(L)
#     return [h0] + ll2py(T0)

# def size(L):
#     if not L :
#         return 0
#     else :
#         return (1 + size(tail(L)))

# def sorted(L):
#     if not L :
#         return True
#     elif not tail(L) :
#         return True
#     else :
#         Sort = head(L)<= head(tail(L))
#         return (Sort and sorted(tail(L)))

# def sum(L):
#     res = 0
#     if not L :
#       return 0
#     else :
#         return sum(tail(L)) + head(L)
      
# def split(L):
#     if not L :
#          return (None,None)
#     elif not tail(L) :
#         return (L,None)
#     else :
#         H0 = head(L)
#         H1 = head(tail(L))
#         (T0,T1) = split(tail(tail(L)))
#         return ((H0,T0) , (H1,T1))


# def merge(L0, L1):
#     if not L0 :
#         return L1
#     elif not L1 :
#         return L0
#     else :
#         H0 = head(L0)
#         H1 = head(L1)
#         T0 = tail(L0)
#         T1 = tail(L1)
#         if H0<H1 :
#             return (H0,merge(T0,L1))
#         else :
#             return (H1,merge(L0,T1))

# def mSort(L):
#     if not L :
#         return None
#     if not tail(L) :
#         return L
#     else :
#         (L0,L1) = split(L)
#         return merge(mSort(L0),mSort(L1))

# def max(L):
#     if not L:
#         return 0
#     elif len(L) == 1:
#         return L[0]
#     else :
#         m = max(L[1:])
#         if m > L[0] :
#             return 1


# def get(L, N):
#     if not L :
#         return None
#     elif len(L) == 1 and N == L[0] :
#         return L[0]
#     elif N> len(L):
#         return None
#     else :
#         return L[N]







def head(L):
    return L[0]
    
def tail(L):
    return L[1]

def py2ll(L):
    if not L :
        return None
    else :
        return (L[0] , py2ll(L[1:]))

def ll2py(L):
    if not L :
        return []
    else :
        H = head(L)
        T = tail(L)
        return [H] + ll2py(T)

def size(L):
    if not L :
        return 0
    else :
        return (1 + size(tail(L)))

def sorted(L):
    if not L :
        return True
    elif not tail(L) :
        return True
    else :
        Sort = head(L)<= head(tail(L))
        return (Sort and sorted(tail(L)))

def sum(L):
    res = 0
    if not L :
       return 0
    else :
        return sum(tail(L)) + head(L)
      

def split(L):
    if not L :
         return (None,None)
    elif not tail(L) :
        return (L,None)
    else :
        H0 = head(L)
        H1 = head(tail(L))
        (T0,T1) = split(tail(tail(L)))
        return ((H0,T0) , (H1,T1))



def split2(L):
    if not L :
         return (None,None)
    elif not tail(L) :
        return (L,None)
    else :
        H0 = head(L)
        H1 = head(tail(L))
        (T0,T1) = split(tail(tail(L)))
        return ((H1,T1) , (H0,T0))


def merge(L0, L1):
    if not L0 :
        return L1
    elif not L1 :
        return L0
    else :
        H0 = head(L0)
        H1 = head(L1)
        T0 = tail(L0)
        T1 = tail(L1)
        if H0<H1 :
            return (H0,merge(T0,L1))
        else :
            return (H1,merge(L0,T1))





def merge2(L0, L1):
    if not L0 :
        return L1
    elif not L1 :
        return L0
    else :
        H0 = head(L0)
        H1 = head(L1)
        T0 = tail(L0)
        T1 = tail(L1)
        if H0>H1 :
            return (H0,merge(T0,L1))
        else :
            return (H1,merge(L0,T1))

def mSort(L):
    if not L :
        return None
    if not tail(L) :
        return L
    else :
        (L0,L1) = split(L)
        return merge(mSort(L0),mSort(L1))

def mSort2(L):
    if not L :
        return None
    if not tail(L) :
        return L
    else :
        (L1,L0) = split2(L)
        return merge2(mSort2(L1),mSort2(L0))


def max(L):
    L1 = mSort2(L)
    H = head(L1)
    T = head(tail(L1))
   
    if not L:
        return None
    elif T>H :
        return T
    else :
        return H


def get(L, N):
    count = 0
    p = 0
    if not L :
        return None
    elif N==0 :
        return  head(L)
    elif N>=0 :
        count += 1
        p = get(tail(L),N-1)
        return p
   