import pyDOE import lhs




def main():
     my_LHS = lhs(10, samples=5000, criterion='maximin', iterations=10)
    
    

if __name__ == "__main__":
        main()
