CMAKE_FLAGS := 

build:
	mkdir -p build && cd build && cmake $(CMAKE_FLAGS) .. && make -j$(shell nproc)
