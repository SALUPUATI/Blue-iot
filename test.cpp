#include <iostream>
#include <chrono>
#include <thread>
#include <ctime>
#include <atomic>

int main(void)
{
  time_t t1, t2;
  time_t t3, t4;
 
        t1 = time(NULL);
        t3 = time(NULL);
        int n;
        while(1)        //probleme de boucle infinie
       {
            t2 = time(NULL);
            t4 = time(NULL);
 
            if(difftime(t2, t1) == 1) // exemple pour 1 secondes
            {
               t1 = t2;
               n = rand() % 100 + 1;
               printf("Profondeur:%d \n", n);   
               n = rand() % 360 + 1;
               printf("altitude:%d \n", n);
               n = rand() % 15000 + 1;
               printf("Force:%d \n", n);
               printf("///////////////\n");
               printf("%x \n", n);
              //std::cout<<"execution de la tache"<<std::endl;
            }
            else if(difftime(t4, t3) == 60) // exemple pour 60 secondes
            {
               t3 = t4;
               n = rand() % 100 + 1;
               printf("Température:%d \n", n);   
               n = rand() % 12 + 1;
               printf("Tension:%d \n", n);
               printf("::::::::::::::\n");    
               //std::cout<<"execution de la tache"<<std::endl;
            }
        }

}
