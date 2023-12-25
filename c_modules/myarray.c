#include <stdlib.h>

typedef struct{
    int *array;
    unsigned long long size;
} Array;

Array* NewArray(unsigned long long size){
    Array *array = malloc(sizeof(Array));
    array->array = malloc(sizeof(int) * size);
    array->size = size;
    return array;
}

unsigned long long SumArray(Array *array){
    long long sum = 0;
    for(int i = 0; i < array->size; i++){
        sum += array->array[i];
    }
    return sum;
}

void SetArray(Array *array, unsigned long long index, int value){
    array->array[index] = value;
}

void FillArray(Array *array){
    for(unsigned long long i = 0; i < array->size; i++){
        array->array[i] = i;
    }
}

void FreeArray(Array *array){
    free(array->array);
    free(array);
}