import ctypes

libc = ctypes.CDLL("libc.so.6")
# <CDLL 'libc.so.6', handle 7ef2ff8f8160 at 0x7ef2ff2912b0>

libc.__ctype_b_loc.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_ushort))
# <class 'ctypes.LP_LP_c_ushort'>

table_ptr = libc.__ctype_b_loc().contents
# <ctypes.LP_c_ushort object at 0x7cee750e68f0>

a1 = (
    4065673187844438380 .to_bytes(8, "little") +
    3474583431018204217 .to_bytes(8, "little") +
    3833460713302314036 .to_bytes(8, "little") +
    (-865323092).to_bytes(4, "little", signed=True)
)

a2 = (
    1959690601885274933 .to_bytes(8,"little") +
    807027392368026419 .to_bytes(8,"little") +
    2538089600001706771 .to_bytes(8, "little") +
    b"3539458369+8"
)

def get_flag(a1, seconds):
    is_digit = (table_ptr[a1] & 2048) != 0

    if is_digit:
        v4 = (8 * a1) % 10

        if v4 <= 7 or v4 > 9:
            return v4 + 50
        else:
            return v4 + 40

    else:
        v3 = (a1 << (8 - seconds)) | (a1 >> seconds)

        v3 &= 0xff

        if v3 >= 0:
            return v3
        else:
            return v3 + 104

for seconds in range(9):
    result = bytes(get_flag(ch, seconds) for ch in a1)
    print(seconds, result.decode("latin1"))
# c8b48ac08bbe00068ffb6606e2cf

def get_flag2(a2, seconds):
    is_digit = (table_ptr[a2] & 2048) != 0

    if is_digit:
        v4 = (8*a2) % 10

        if v4 <=7 or v4 > 9:
            return v4+50
        else:
            return v4+40
    else:
        v3 = (a2 << (8 - seconds)) | (a2 >> seconds)
        v3 &= 0xff

        if v3 >= 0:
            return v3
        else:
            return v3+104

# for seconds in range(9):
#     result = bytes(get_flag2(ch, seconds) for ch in a2)
#     print(seconds, result.decode("latin1"))
# 6ba0002c0dc4dd0aba20ac8d0608860048e0


