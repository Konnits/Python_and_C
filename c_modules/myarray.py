import ctypes
from typing import Any

__all__ = ['Array']

class array(ctypes.Structure):
    _fields_ = [
        ('array', ctypes.POINTER(ctypes.c_int)),
        ('size', ctypes.c_int)
    ]


class Array:
    
    lib = ctypes.CDLL('./c_modules/libmyarray.so')

    lib.NewArray.argtypes = [ctypes.c_uint64]
    lib.NewArray.restype = ctypes.POINTER(array)

    lib.SumArray.argtypes = [ctypes.POINTER(array)]
    lib.SumArray.restype = ctypes.c_uint64

    lib.SetArray.argtypes = [ctypes.POINTER(array), ctypes.c_uint64, ctypes.c_int]
    lib.SetArray.restype = None
    
    lib.FillArray.argtypes = [ctypes.POINTER(array)]
    lib.FillArray.restype = None

    lib.free.argtypes = [ctypes.POINTER(array)]
    lib.free.restype = None
    
    def __init__(self, size):
        self.size = size
        self.obj = self.lib.NewArray(size)
    
    def __del__(self):
        self.lib.free(self.obj)
    
    def sum(self):
        return self.lib.SumArray(self.obj)
    
    def __setitem__(self, index, value):
        self.lib.SetArray(self.obj, index, value)
    
    def __del__(self):
        self.lib.FreeArray(self.obj)
    
    def __getitem__(self, index):
        return self.obj.contents.array[index]
    
    def __str__(self):
        return str([self[i] for i in range(self.size)])

class Range(Array):
    
    def __init__(self, size):
        super().__init__(size)
        self.fill()

    def fill(self):
        self.lib.FillArray(self.obj)