// Created by François Soulier on 28/01/2020.

/// INFORMATION:
/// The variable 'char_representation' that appears in some of the structures below
/// represents each structures' parameter, transformed into character(s)
/// and concatenated to one another

#include <stdio.h>
#include "BMP_Pic.h"


/*HeaderFile read_header_file(char* filename)
{
    FILE* imageFile = fopen(filename, "rb");
    //FIXME...
    //TODO...
}*/

void cat_num_str(char* chain_char1, int number, unsigned int start_index, unsigned int size_number)
{
    char file_size_char[size_number];
    sprintf(file_size_char, "%ui", number);
    for (unsigned int i = 0; i < size_number; i++)
        chain_char1[start_index + i] = file_size_char[i];
}

// Functions to get the character representation of each structure
char* get_File_Header_char(HeaderFile headerFile)
{
    char representation[14];
    unsigned int index = 0;
    for (unsigned int i = 0; i < 2; i++)
    {
        representation[i] = headerFile.signature[i];
        index++;
    }


    cat_num_str(representation, (int)headerFile.file_size, index, 4);


    return "";
}


/*char* get_Image_Header_char(HeaderImage headerImage)
{
    return "";
}


char* get_Pallet_char(ColorPallet pallet)
{
    return "";
}


char* get_Pixels_char(PixelBMP* pixels)
{
    return "";
}
*/


















