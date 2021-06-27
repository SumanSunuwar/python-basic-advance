HELLO = "This is vairable HELLO"

PI = 3.14

def print_hello(name):
	print(f"Hello ! {name}")

def search_index(name, anylist):
	for index, value in enumerate(anylist):
		if name == value:
			return index
	return -1

print(__name__)


if __name__ == "__main__":
	print(HELLO)

