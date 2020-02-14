#include <stdio.h>
#include <stdlib.h>
#include "thresholding.h"
#include <math.h>

unsigned char max_pixel_intensity(Uint32 pixel[][], int width, int height)
{
    unsigned char maximum_intensity = 0;
    for (unsigned int i = 0; i < width; i++)
    {
        for (unsigned int j = 0; j < height; j++)

    }
}

unsigned int number_pixel_occurences()
{
    //TODO
}

float global_variance()
{
    //TODO
}

float global_mean()
{
    //TODO
}

float probability_first_class(unsigned char t)
{
    //TODO
}

float probability_second_class(unsigned char t) // omega_1 = 1 - omega_0
{
    //TODO
}

float first_class_mean(unsigned char t /* WITH PROBABILITY FIRST CLASS */)
{
    //TODO
}

float second_class_mean(unsigned char t /* WITH PROBABILITY SECOND CLASS */)
{
    //TODO
}

float total_mean()
{
    //TODO
}

unsigned char otsu_criteria(unsigned char t) //sigma_b^2
{
    //TODO
}

unsigned char threshold()
{
    //TODO
}
