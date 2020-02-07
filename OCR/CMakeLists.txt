cmake_minimum_required(VERSION 3.15)
project(OCR C)

set(CMAKE_C_STANDARD 99)

add_executable(OCR main.c BMP_Pic.c BMP_Pic.h SDL_Functions.c SDL_Functions.h)