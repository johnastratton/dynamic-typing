//
//  ISCodeSamples1.cpp
//  
//
//  Created by Lillie on 3/23/15.
//
//

#include "ISCodeSamples1.h"
#include <cmath>
#include <iostream>

//Implementation with member function

void function_plus(double* d){
    *d = *d + 1;
}

//Virtual Function Implementation

class sample_base {
public:
    virtual void vfunction_plus(double *d) = 0;
};

class sample_inherit1 : public sample_base{
public:
    void vfunction_plus(double *d){
        *d = *d + 1;
    }
};

//run both
int main(int argc, const char * argv[]) {
    double sample_array[1000];
    sample_base* vsample_array[1000];
    for (int i=0; i<1000; ++i){
        sample_array[i]=(double) i*1.5;
        vsample_array[i] = new sample_inherit1();
    }
    for (int i=0; i<1000; ++i){
        function_plus(&sample_array[i]);
        vsample_array[i]->vfunction_plus(&sample_array[i]);
    }
    return 0;
}



