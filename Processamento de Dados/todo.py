def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """
   
    if not L :
        return None
    else :
        LastN = []
        for c in L :
             (LastN.append(c[-1]))
        return LastN

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """
    if not L :
        return None
    else :
        citationN = []
        for c in L :
            citationN.append(c[0][0])
            citationN.append(c[-1])
        return  citationN
 
 
def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """
    if not L :
        return None
    else :
        fullCitation1 = []
        for c in L :
            for i in range(0,len(c)-1) :
                fullCitation1.append(c[i][0])
            fullCitation1.append(c[-1])
           
    return fullCitation1

