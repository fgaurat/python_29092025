import traceback

def div(a,b):
    return a/b

def call_div(a,b):
    result = 0
    try:
        print("OPEN FILE")
        result = div(a,b)
        print("WRITE LOG")
    # except Exception as e:
    #     print("erreur",e)
    finally:    
        print("CLOSE FILE")

    return result

def main():
    a = 2
    b = 0
    c = call_div(a,b)
    print(c)

def main_1():
    try:
        a = 2
        b = int(input("valeur de b:"))
        c = a/b
        print(c)
    except ZeroDivisionError as e:
        print(e)
        print("erreur")
        traceback.print_exc()
    except TypeError as e:
        print(e)        
    except ValueError as e:
        print(e)        
    except Exception as e:
        print(e)        
    else:
        print("pas d'erreur")
    finally:
        print("finally")        
    
    print("la suite du code")

if __name__=='__main__':
    main()
