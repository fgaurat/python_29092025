def main():
    a  = 2
    b = 3
    c = a/b
    print(c)

    #f-string => formated string
    s = f"a={a} / b={b} => c={c}"
    s = f"{a} / {b} = {c*100:.2}%"
    s = f"{a} / {b} = {c:.2%}"
    s = f"{a=} / {b=} = {c=:.2%}"
    print(s)




if __name__=='__main__':
    main()
