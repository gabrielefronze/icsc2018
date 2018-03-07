main_original: main_original.cxx
	g++ -g -O0 -std=c++11 -I. -o main_original main_original.cxx

main_solution: main_solution.cxx
	g++ -g -O0 -std=c++11 -I. -o main_solution main_solution.cxx

main: main.cxx
	g++ -g -O0 -std=c++11 -I. -o main main.cxx

main_double: main_double.cxx
	g++ -g -O0 -std=c++11 -I. -o main_double main_double.cxx

all: main main_original main_solution main_double

.PHONY: clean
clean:
	rm -rf main main.dSYM
	rm -rf main_original main_originalmain.dSYM
