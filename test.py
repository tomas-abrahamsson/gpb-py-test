import test_pb2 as test_pb

def valid():
    t0 = test_pb.Test()
    t0.id = 18446744073709551615

    print(f't0: {t0}')

    with open("./valid_ser_test", "wb") as fd:
        fd.write(t0.SerializeToString())

    t1 = test_pb.Test()

    with open("./valid_ser_test", "rb") as fd:
        t1.ParseFromString(fd.read())

    print(f't1: {t1}')
    assert(t0.id == t1.id)

def invalid2():
    t1 = test_pb.Test()

    with open("./uint70_ser_test", "rb") as fd:
        t1.ParseFromString(fd.read())

    print(f'invalid2: t1: {t1}')

if __name__ == '__main__':
    valid()
    invalid2()
