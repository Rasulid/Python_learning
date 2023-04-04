def do_staff(num):
    try:
        return int(num) + 10
    except Exception as erorr:
        print(erorr)