//
// Created by François Soulier on 28/01/2020.
//

#ifndef OCR_BMP_PIC_H
#define OCR_BMP_PIC_H

int PLANES;

typedef struct
{
    char signature[2];
    unsigned int size;
    char reserved[4];
    char offset[4];

}HeaderFile;

typedef struct
{
    int signature:4;    // Bitmap info header structure size
    int width:4;
    int height:4;
    int planes:2;   // Always equals to 1
    int compression:2;  // Compression method (0: not compressed, 1: 8 bits RLE, 2: 4 bits RLE, 3: bitfield)
    int size:4;
    int x_ppm:4;    // Pixels per meter in the X axe
    int y_ppm:4;    // Pixels per meter in the Y axe
}HeaderImage;

#endif //OCR_BMP_PIC_H
