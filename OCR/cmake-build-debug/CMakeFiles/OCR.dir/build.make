# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/francoissoulier/Desktop/OCR_Project/OCR

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/OCR.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/OCR.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/OCR.dir/flags.make

CMakeFiles/OCR.dir/main.c.o: CMakeFiles/OCR.dir/flags.make
CMakeFiles/OCR.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/OCR.dir/main.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/OCR.dir/main.c.o   -c /Users/francoissoulier/Desktop/OCR_Project/OCR/main.c

CMakeFiles/OCR.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/OCR.dir/main.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/francoissoulier/Desktop/OCR_Project/OCR/main.c > CMakeFiles/OCR.dir/main.c.i

CMakeFiles/OCR.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/OCR.dir/main.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/francoissoulier/Desktop/OCR_Project/OCR/main.c -o CMakeFiles/OCR.dir/main.c.s

CMakeFiles/OCR.dir/BMP_Pic.c.o: CMakeFiles/OCR.dir/flags.make
CMakeFiles/OCR.dir/BMP_Pic.c.o: ../BMP_Pic.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/OCR.dir/BMP_Pic.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/OCR.dir/BMP_Pic.c.o   -c /Users/francoissoulier/Desktop/OCR_Project/OCR/BMP_Pic.c

CMakeFiles/OCR.dir/BMP_Pic.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/OCR.dir/BMP_Pic.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/francoissoulier/Desktop/OCR_Project/OCR/BMP_Pic.c > CMakeFiles/OCR.dir/BMP_Pic.c.i

CMakeFiles/OCR.dir/BMP_Pic.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/OCR.dir/BMP_Pic.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/francoissoulier/Desktop/OCR_Project/OCR/BMP_Pic.c -o CMakeFiles/OCR.dir/BMP_Pic.c.s

CMakeFiles/OCR.dir/SDL_Functions.c.o: CMakeFiles/OCR.dir/flags.make
CMakeFiles/OCR.dir/SDL_Functions.c.o: ../SDL_Functions.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/OCR.dir/SDL_Functions.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/OCR.dir/SDL_Functions.c.o   -c /Users/francoissoulier/Desktop/OCR_Project/OCR/SDL_Functions.c

CMakeFiles/OCR.dir/SDL_Functions.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/OCR.dir/SDL_Functions.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/francoissoulier/Desktop/OCR_Project/OCR/SDL_Functions.c > CMakeFiles/OCR.dir/SDL_Functions.c.i

CMakeFiles/OCR.dir/SDL_Functions.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/OCR.dir/SDL_Functions.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/francoissoulier/Desktop/OCR_Project/OCR/SDL_Functions.c -o CMakeFiles/OCR.dir/SDL_Functions.c.s

# Object files for target OCR
OCR_OBJECTS = \
"CMakeFiles/OCR.dir/main.c.o" \
"CMakeFiles/OCR.dir/BMP_Pic.c.o" \
"CMakeFiles/OCR.dir/SDL_Functions.c.o"

# External object files for target OCR
OCR_EXTERNAL_OBJECTS =

OCR: CMakeFiles/OCR.dir/main.c.o
OCR: CMakeFiles/OCR.dir/BMP_Pic.c.o
OCR: CMakeFiles/OCR.dir/SDL_Functions.c.o
OCR: CMakeFiles/OCR.dir/build.make
OCR: CMakeFiles/OCR.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C executable OCR"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/OCR.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/OCR.dir/build: OCR

.PHONY : CMakeFiles/OCR.dir/build

CMakeFiles/OCR.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/OCR.dir/cmake_clean.cmake
.PHONY : CMakeFiles/OCR.dir/clean

CMakeFiles/OCR.dir/depend:
	cd /Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/francoissoulier/Desktop/OCR_Project/OCR /Users/francoissoulier/Desktop/OCR_Project/OCR /Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug /Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug /Users/francoissoulier/Desktop/OCR_Project/OCR/cmake-build-debug/CMakeFiles/OCR.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/OCR.dir/depend

