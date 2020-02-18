#include <stdio.h>
#include <stdbool.h>
#include <err.h>
#include "SDL2/SDL.h"
#include "SDL2/SDL_image.h"

#include <SDL2/SDL.h>        

void init_sdl()
{
    if(SDL_Init(SDL_INIT_VIDEO) == -1)
        errx(1,"Could not initialize SDL: %s.\n", SDL_GetError());
}

void display(SDL_Surface *img)        
{        
    char quit = 0;        
    SDL_Event event;      
            
    SDL_Window *screen = SDL_CreateWindow("Displaying",
                        SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, img->w, img->h, 0);
    
    SDL_Renderer * renderer = SDL_CreateRenderer(screen, -1, 0);        
    
    SDL_Texture * texture = SDL_CreateTextureFromSurface(renderer, img);

    while (!quit)        
    {        
        SDL_WaitEvent(&event);
            
        switch(event.type)        
        {        
           case SDL_QUIT:        
               quit = 1;        
               break;        
        }
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        SDL_RenderPresent(renderer);
    }        

    SDL_DestroyTexture(texture);  
    SDL_FreeSurface(img);  
    SDL_DestroyRenderer(renderer);  
    SDL_DestroyWindow(screen);

    SDL_Quit();        
}

int main()
{
    SDL_Surface *image_surface;

    init_sdl();
    image_surface = IMG_Load("Try.jpg");
    display(image_surface);
    return 0;
}