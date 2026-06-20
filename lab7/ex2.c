#define OPENSSL_SUPPRESS_DEPRECATED
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <openssl/sha.h>
#include <stdatomic.h>

#define ITERS 2000000

char** files;
int num_files;
unsigned long* results;

// index global protejat de stdatomic
atomic_int current_file_idx = 0;

unsigned long stretch_hash(const char* path) {
    FILE* f = fopen(path, "r");
    if (!f) return 0;
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char* buf = malloc(sz);
    fread(buf, 1, sz, f);
    fclose(f);

    unsigned char digest[32];
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, buf, sz);
    SHA256_Final(digest, &ctx);
    free(buf);

    for (int i = 0; i < ITERS; i++) {
        SHA256_Init(&ctx);
        SHA256_Update(&ctx, digest, 32);
        SHA256_Final(digest, &ctx);
    }

    unsigned long sum = 0;
    for (int i = 0; i < 32; i++) sum += digest[i];
    return sum;
}

void* thread_routine(void* arg) {
    while (1) {
        // extragem atomic următorul index
        int idx = atomic_fetch_add(&current_file_idx, 1);
        
        // Dacă am depășit numărul de fișiere, thread-ul își termină munca
        if (idx >= num_files) {
            break;
        }
        
        results[idx] = stretch_hash(files[idx]);
    }
    return NULL;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        printf("Utilizare: %s <numar_threaduri> <fisier1> [fisier2...]\n", argv[0]);
        return 1;
    }
    
    int num_threads = atoi(argv[1]);
    num_files = argc - 2;
    files = &argv[2];
    results = malloc(num_files * sizeof(unsigned long));
    
    pthread_t* threads = malloc(num_threads * sizeof(pthread_t));
    
    for (int i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, thread_routine, NULL);
    }
    
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }
    
    for (int i = 0; i < num_files; i++) {
        printf("File %s hash: %lu\n", files[i], results[i]);
    }
    
    free(results);
    free(threads);
    return 0;
}
