def funA(desA):
    print("It's funA")
    print('---')
    print(desA())
    print('---')
		
def funB(desB):
    print("It's funB")
	
def funC(desC):
    print("It's funC") 
	
@funC	
@funB
@funA
def funD():
    def desD():
        return "It's desD"
    print("It's funD")
    return desD

funD()
