#include <stdio.h>
#include <stdlib.h>
#include "thresholding.h"
#include <math.h>
#include "sdl/pixel_operations.h"

Uint8 get_gray_value(SDL_Surface *image_surface, Uint32 pixel)
{
    Uint8 gray_value;
    SDL_GetRGB(pixel, image_surface->format, &gray_value, &gray_value, &gray_value);
    return gray_value;
}

// Function that gets the maximum pixel intensity of the surface, along with the number of occurences of a pixel
void set_initital_parameters(SDL_Surface *image_surface, Uint8 *max_pixel_intensity, unsigned int *occurences, unsigned int width, unsigned int height)
{
    for (unsigned int i = 0; i < width; i++)
    {
        for (unsigned int j = 0; j < height; j++)
        {
            Uint32 pixel = get_pixel(image_surface, i, j);
            Uint8 gray_value = get_gray_value(image_surface, pixel);
            *max_pixel_intensity = gray_value > *max_pixel_intensity? gray_value:*max_pixel_intensity;
            occurences[gray_value]++;
        }
    }
}

float probability_finding_pixel(SDL_Surface *image_surface, Uint32 pixel, unsigned int *occurences, unsigned int width, unsigned int height)
{
    Uint8 gray_value = get_gray_value(image_surface, pixel);
    return ((float)(occurences[gray_value])*(float)(gray_value))/((float)width*height);
}

float probability_first_class(unsigned int t, SDL_Surface *image_surface, unsigned int *number_pixel_occurences, unsigned int width, unsigned int height)
{
    float prob1 = 0.0f;
    for (unsigned int i = 0; i <= t; i++)
    {
        Uint8 gray_value;
    }
    return prob1;
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

float total_mean(SDL_Surface *image_surface, unsigned int width, unsigned int height, unsigned int *occurences)
{
    float t_mean = 0.0f;
    for (unsigned int i = 0; i < width; i++)
    {
        for (unsigned int j = 0; j < height; j++)
        {
            Uint32 pixel = get_pixel(image_surface, i, j);
            t_mean += ((float)get_gray_value(image_surface, pixel))*(probability_finding_pixel(image_surface, pixel, occurences, width, height));
        }
    }
}

unsigned char otsu_criteria(unsigned char t) //sigma_b^2
{
    //TODO
}

unsigned char threshold()
{
    //TODO
}
