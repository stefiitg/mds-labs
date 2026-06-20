#include <stdio.h>
#include <pthread.h>

int counter = 0;

void* thread_routine(void* arg) {
    for (int i = 0; i < 100000; i++) {
        counter++; // Acest ++ nu este operație atomică, ceea ce duce la data races
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    
    pthread_create(&t1, NULL, thread_routine, NULL);
    pthread_create(&t2, NULL, thread_routine, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Rezultat Final: %d (Asteptat: 200000)\n", counter);
    return 0;
}
