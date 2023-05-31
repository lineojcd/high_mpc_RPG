import ctypes
from casadi import *

# Load the shared object file
lib = ctypes.CDLL("high_mpc/mpc/saved/mpc_v1.so")

# # Define the function prototype for the desired function
# lib.your_function_name.argtypes = [ctypes.c_double]
# lib.your_function_name.restype = ctypes.c_double

# # Create a CasADi function
# x = MX.sym("x")
# casadi_function = Function("your_function_name", [x], [x])

# # Example usage
# input_value = 2.0
# output_value = lib.your_function_name(ctypes.c_double(input_value))
# result = casadi_function(output_value)
# print(result)
