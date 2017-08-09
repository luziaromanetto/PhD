import numpy as np

def expectation_maximization(Dl, Du, F, Y, MAX_STEPS):
    FDl = Y
    FT = estimate_prob_terms(Dl, W, FDl)
    
    for t in range(MAX_STEPS):
        FDu = estimate_prob_doc(T, W, FT)
        FT = estimate_prob_terms(Dl, Du, W, FD)
        
    return FDu

def co_training(Dl1, Dl2, Du1, Du2, W1, W2, Y, X):
    
    Dr1 = Du1
    Dr2 = Du2
    
    classes1 = [ -1 ]*(len(Dl1)+len(Du1))
    classes2 = [ -1 ]*(len(Dl2)+len(Du2))
    
    while ( Dr1 is not None ) and ( Dr2 is not None ):
        classification_model_view1 = inductive_learning(Dl1, W1, Y)
        classification_model_view2 = inductive_learning(Dl2, W2, Y)
        
        FDr1 = classification_model_view1( Dr1, W1 )
        FDr2 = classification_model_view1( Dr2, W2 )
        
        S1 = most_confident( FDr1, X )
        for di in S1:
            classes1[di] = np.argmax( FDr1[di] )
            
        S2 = most_confident( FDr2, X )
        for di in S2:
            classes2[di] = np.argmax( FDr2[di] )
        
        Dr1 = [ di for di in Dr1 if di not in S1 ]
        Dr2 = [ di for di in Dr2 if di not in S2 ]
        Dl1 = Dl1 + S1
        Dl2 = Dl2 + S2
        
    return classes1 + classes2

def self_training( Dl, Du, W, Y, X):
    # TODO: pensar sobre a modelagem do Y e do classes
    Dr = Du
    classes = [ -1 ]*(len(Dl)+len(Du))
    
    while Dr is not None:
        classification_model = inductive_learning(Dl, W, Y)
        FDr = classification_model(Dr, W)
        S = most_confident( FDr, X )
        
        for di in S:
            classes[di] = np.argmax( FDr[di] )
            
        Dr = [di for di in Dr if di not in S]
        Dl = Dl + S

    return classes

if __name__ == "__main__":
