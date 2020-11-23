## LIST
## LIBRARY INI BERISI DATABASE CODE UNTUK SET 
## LIBRARY INI DIBUAT DAN DIKUMPULKAN OLEH :
## MUHAMAD NUR BAIHAQI (INFORMATIKA UNDIP 2020)
## INI ADALAH LIBRARY FUNGSI PRIMITIF
## Konstruktor:
def mklist():
    return []

## Basic Predikat
## Mengecek List Kosong atau Bukan:
def IsEmpty(L):
    if L == []:
        return True
    else:
        return False

## Utility
## Inverse List:
def Inverse(L):
	Ls = list(L)
	Ls.reverse()
	return Ls


## Selector
## Mengambil Tail:
def Tail(L):
    if not(IsEmpty(L)):
        return L[1:]

## Mengambil Head:
def Head(L):
    Ls = list(L)
    Ls.reverse()
    del Ls[0]
    Ls.reverse()
    return Ls

## Mengambil Element Pertama:
def FirstElmt(L):
    return L[0]

## Mengambil Element Terakhir:
def LastElmt(L):
    return FirstElmt(Inverse(L))

## Mengambil Element ke N dari List L:
def ElmtKeN(N, L):
    if IsEmpty(L):
        return "List kosong"
    if Nb_Elmt(L) == 1:
        return L
    else:
        if N > Nb_Elmt(L):
            return "N tidak boleh melebihi jumlah element list"
        elif N == 1:
            return FirstElmt(L)
        else:
            return ElmtKeN(N-1, Tail(L))


## Add Element ke List :
## Add ke Awal List
def Konso(e, L):
    Ls = list(L)
    Ls.insert(0,e)
    return Ls

## Add ke Akhir List
def Konsi(e, L):
    Ls = list(L)
    Ls.append(e)
    return Ls


## Counter
## Menghitung Jumlah element list:
def Nb_Elmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + Nb_Elmt(Tail(L))

## Menghitung Jumlah element dari List L
def Nb_ElmtX(X,L):
    if IsEmpty(L):
        return 0
    else:
        if FirstElmt(L) == X:
            return 1 + Nb_ElmtX(X,Tail(L))
        else:
            return 0 + Nb_ElmtX(X,Tail(L))

## Advanced Predicate
## Apakah inverse
def IsInverse(La, Lb):
    if Inverse(La) == Lb:
        return True
    else:
        return False

# Apakah member
def IsMember(n, L):
    if IsEmpty(L):
        return False
    else :
        if n == FirstElmt(L):
            return True
        else :
            return IsMember(n,Tail(L))

# Apakah X elemen ke N dari list L
def IsXElmtKeN(X,N,L):
    if IsMember(X,L):
        if N == 1 :
            if X == FirstElmt(L):
                return True
            else:
                return False
        else:
            return IsXElmtKeN(X,N-1,Tail(L))    
    else:
        return False


## Operasi
def KaliList(k,L):
    if L == []:
        return []
    else:
        if k == 0 :
            return SetAllZero(L)
        elif k == 1:
            return L
        else:
            return Konso(k*FirstElmt(L),KaliList(k,Tail(L)))


# Menjumlahakan semua element dari List:
def SumList(L):
    if L == []:
        return 0
    else:
        return FirstElmt(L) + SumList(Tail(L))

# Menjumlahkan semua elemen L tanpa X
def SumListExceptX(x, L):
    if L == []:
        return 0
    else:
        if x == FirstElmt(L):
            return 0 + SumListExceptX(x, Tail(L))
        else:
            return FirstElmt(L) + SumListExceptX(x, Tail(L))

# Menghapus satu elemen dari L
def Rember(e,L):
    if IsEmpty(L):
        return L
    else:
        if e == FirstElmt(L):
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember(e,Tail(L)))

# Menghapus semua elemen e dari L
def MultiRember(e,L):
    if IsEmpty(L):
        return L
    else:
        if e == FirstElmt(L):
            return MultiRember(e,MultiRember(e,Tail(L)))
        else:
            return Konso(FirstElmt(L),MultiRember(e,Tail(L)))

# Mengubah semua elemen e menjadi x dalam list L
def SetElmtEtoX(e,X,L):
    if IsMember(e, L):
        if FirstElmt(L) == e:
            return Konso(X,SetElmtEtoX(e,X,Tail(L)))
        else: 
            return Konso(FirstElmt(L),SetElmtEtoX(e,X,Tail(L)))
    else:
        return L

# Mengubah elemen e ke 0
def SetElmtZero(e,L):
    if IsMember(e, L):
        if e == FirstElmt(L):
            return Konso(0,SetElmtZero(e,Tail(L)))
        else:
            return Konso(FirstElmt(L),SetElmtZero(e,Tail(L)))
    else:
        return L

def SetAllZero(L):
    if L == []:
        return []
    else:
        return Konso(0,SetAllZero(Tail(L)))

# Insert
def Insert(x,L):
    if IsEmpty(L):
        return Konso(x,L)
    else:
        if x <= FirstElmt(L):
            return Konso(x, L)
        else:
            return Konso(FirstElmt(L),Insert(x,Tail(L)))

## SET
## LIBRARY INI BERISI DATABASE CODE UNTUK SET 
## LIBRARY INI DIBUAT DAN DIKUMPULKAN OLEH :
## MUHAMAD NUR BAIHAQI (INFORMATIKA UNDIP 2020)
## INI ADALAH LIBRARY FUNGSI PRIMITIF

## Predikat Dasar
## Apakah Set:
def IsSet(L):
    if L == []:
        return True
    else:
        if Nb_ElmtX(FirstElmt(L),L) > 1:
            return False
        else:
            return IsSet(Tail(L))

## Konstruktor:
def MakeSet(L):
        if L == []:
            return []
        else:
            if IsMember(FirstElmt(L),Tail(L)):
                return MakeSet(Tail(L))
            else:
                return Konso(FirstElmt(L),MakeSet(Tail(L)))

## Advanced Predicate:
def IsIntersect(H1,H2):
    if IsSet(H1) and IsSet(H2):
        if (IsEmpty(H1) and not IsEmpty(H2)) or (IsEmpty(H2) and not IsEmpty(H1)):
            return False
        elif IsEmpty(H1) and IsEmpty(H2):
            return False
        else : 
            if IsMember(FirstElmt(H1),H2):
                return True
            else:
                return IsMember(FirstElmt(Tail(H1)),H2)
    else:
        return "Bukan merupakan set"

## Apakah H1 subset dari H2
def IsSubset(H1,H2):
    if H1 == []:
        return True
    else:
        if not (IsMember(FirstElmt(H1),H2)):
            return False
        else:
            return IsSubset(Tail(H1),H2)

## Selector:
# Mencari elemen yang berinterseksi
def MakeIntersect(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    elif IsEmpty(H2) and not IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeIntersect(Tail(H1),H2))
        else:
            return MakeIntersect(Tail(H1),H2)

# Menggabungkan semua elemen set
def MakeUnion(H1,H2):
    if IsEmpty(H1):
        return H2
    elif IsEmpty(H2):
        return H1
    else:
        if not IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeUnion(Tail(H1),H2))
        else:
            return MakeUnion(Tail(H1),H2)

# Mengurangi set H1 dengan H2
def MakeMinus(H1,H2):
    if H1 == []:
        return []
    elif H2 == []:
        return H1
    else:
        if IsMember(FirstElmt(H1),H2):
            return MakeMinus(Tail(H1),H2)
        else:
            return Konso(FirstElmt(H1),MakeMinus(Tail(H1),H2))

# Apakah kedua Set sama
def IsEQSet(H1,H2):
    if IsSubset(H1,H2) and IsSubset(H2,H1):
        return True
    else:
        return False

## LOL
# Apakah list of list
def IsLoL(S):
    if S == []:
        return True
    else:
        if type(FirstElmt(S)) == list:
            return True
        else:
            return IsLoL(Tail(S))

# Apakah List of List kosong
def IsEmptyLoL(S):
    return S == []

# Apakah atom
def IsAtom(S):
    if type(S) != list:
        return True
    else:
        return False

# Apakah List
def IsList(S):
    return not (IsAtom(S))

# SELEKTOR
# Elemen pertama list of list
def FirstList(S):
    if not(IsEmptyLoL(S)):
        return S[0]

# Elemen terakhir list of list
def LastList(S):
    if not(IsEmptyLoL(S)):
        return FirstList(Inverse(S))

# Tail dari List of List
def TailList(S):
    if not(IsEmptyLoL(S)):
        return S[1:]

# Head dari list of list
def HeadList(S):
    Ss = list(S)
    Ss.reverse()
    del Ss[0]
    Ss.reverse()
    return Ss

def HeadList2(S):
    if not(IsEmptyLoL(S)):
        return S[:-1]

# Apakah kedua List of List sama 
def IsEqS(S1,S2):
    if IsEmptyLoL(S1) and IsEmptyLoL(S2):
        return True
    elif IsEmptyLoL(S1) and not IsEmptyLoL(S2):
        return False
    elif not IsEmptyLoL(S1) and IsEmptyLoL(S2):
        return False
    else:
        if IsAtom(FirstList(S1))and IsAtom(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1),TailList(S2))
        if IsList(FirstList(S1))and IsList(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1),TailList(S2))
        else:
            return False

# Insert list of list ke list of list lain
def Konslo(S1,S2):
    Ls = list(list(S2))
    Ls.insert(0,S1)
    return Ls

## MATRIX
# Menghitung Banyak Elemen dari suatu Matrix
def NbEleX(X, L):
    if L == []:
        return 0
    else:
        if IsAtom(FirstList(L)):
            if FirstList(L) == X:
                return 1 + NbEleX(X, Tail(L))
            else:
                return 0 + NbEleX(X, Tail(L))
        elif IsList(FirstList(L)):
            return Nb_ElmtX(X, FirstList(L)) + Nb_ElmtX(X, Tail(L))

# Mengalikan Matrix dengan suatu konstanta
def KaliMatrix(k ,L):
    if IsEmpty(L):
        return []
    else:
        if k == 0:
            return Konso(SetAllZero(FirstList(L)),KaliMatrix(k,TailList(L)))
        elif k == 1:
            return L
        else:
            return Konso(KaliList(k,FirstList(L)),KaliMatrix(k,Tail(L)))

# Menghitung jumlah list of list / row dari suatu matrix
def NbList(L):
    if L ==  []:
        return 0
    else:
        if IsAtom(FirstList(L)):
            return 0 + NbList(Tail(L))
        else:
            return 1 + NbList(Tail(L))