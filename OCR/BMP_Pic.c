// Created by François Soulier on 28/01/2020.

/// INFORMATION:
/// The variable 'char_representation' that appears in some of the structures below
/// represents each structures' parameter, transformed into character(s)
/// and concatenated to one another

#include <stdio.h>

char *filename;

// Structure representing file header of a bitmap file
typedef struct
{
    char *char_representation;
    char signature[2];                  // signature = {'B', 'M'} in most cases
    unsigned int file_size:4;
    unsigned int reserved_1:2;          // Should be initialized the 0 (unsigned integer value)
    unsigned int reserved_2:2;          // Same as above
    unsigned int pixel_data_offset:4;   // Distance between the first byte of the file
}HeaderFile;                            // and the first byte of the pixels data set


/*

bbp = bits per pixel
1 bbp -> 2 colors
4 bbp -> 16 colors
8 bbp (or 1 byte per pixel) -> 256 colors

 */

// Structure representing image header of a bitmap file
typedef struct
{
    char *char_representation;
    unsigned int header_size:4;
    int width:4;                        // In pixels
    int height:4;                       // In pixels
    const unsigned int planes:2;        // Number of color planes (1 in decimal)
    unsigned int bbp:2;                 // bits per pixel
    unsigned int compression:4;         // Value of compression to use (0 -> no compression)
    unsigned int size:4;                // Final size of the compressed image (0 -> no compression has been used)
    int x_ppm:4;                        // Horizontal resolution of the target device (0 -> no preference)
    int y_ppm:4;                        // Vertical resolution of the target device (0 -> no preference)
    unsigned int total_colors:4;        // Number of colors in the color pallet
    unsigned int important_colors:4;    // Number of important colors (generally ignored, thus set to 0)
}HeaderImage;


// Structure representing the color pallet of the bitmap image
typedef struct
{
    int R:1;
    int G:1;
    int B:1;
    int reserved:1; // Should be set to 0
}ColorPallet;


// Structure representing a pixel of a bitmap image (with the RGB format)
typedef struct
{
    char *char_representation;
    int x;
    int y;
    int RGB[3];
}PixelBMP;


// Structure representing the image "format"/"file" itself
// (which includes objects created out of the previous structures above)
typedef struct
{
    char *char_representation;
    HeaderFile headerFile;
    HeaderImage headerImage;
    ColorPallet pallet;
    PixelBMP *pixels;
}BMPImage;

HeaderFile read_header_file(char* filename)
{
    FILE* imageFile = fopen(filename, "rb");
    //FIXME...
    //TODO...
}






















