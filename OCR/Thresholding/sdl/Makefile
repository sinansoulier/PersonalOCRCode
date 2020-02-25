#Simple SDL mini Makefile

CC=gcc

CPPFLAGS= `pkg-config --cflags sdl2` -MMD
CFLAGS= -Wall -Wextra -Werror -std=c99 -O3
LDFLAGS=
LDLIBS= `pkg-config --libs sdl2` -lSDL2_image

all: display2

display2: display2.o

clean:
	${RM} *.o
	${RM} *.d
	${RM} display2

# END
