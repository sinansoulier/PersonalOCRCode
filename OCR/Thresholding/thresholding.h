#ifndef THRESHOLDING_H
#define THRESHOLDING_H
#include <SDL/SDL.h>
#include <SDL/SDL_image.h>

// MISSING ARGUMENTS IN PROTOTYPES
// TO BE MODIFIED WHEN ALL DECLARED

unsigned char max_pixel_intensity();

unsigned int number_pixel_occurences();

float global_variance();

float global_mean();

float probability_first_class(unsigned char t);

float probability_second_class(unsigned char t); // omega_1 = 1 - omega_0

float first_class_mean(unsigned char t /* WITH PROBABILITY FIRST CLASS */);

float second_class_mean(unsigned char t /* WITH PROBABILITY SECOND CLASS */);

float total_mean();

unsigned char otsu_criteria(unsigned char t); //sigma_b^2

unsigned char threshold();

#endif