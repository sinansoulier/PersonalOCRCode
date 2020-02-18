# Simple SDL mini Makefile

CC=gcc

CPPFLAGS= `pkg-config --cflags sdl2` -MMD
CFLAGS= -Wall -Wextra -Werror -std=c99 -O3
LDFLAGS=
LDLIBS= `pkg-config --libs sdl2` -lSDL2_image

all: libsdl2 grayscale

libsdl2: libsdl2.o

clean:
	${RM} *.o
	${RM} *.d
	${RM} libsdl2

# END
