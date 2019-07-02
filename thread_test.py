from concurrent.futures import ThreadPoolExecutor
import time, os
messages= [
"a", 
"b", 
"c", 
"d", 
"e", 
"f", 
"g", 
"h", 
"i", 
"j", 
"k", 
"l"
]

def fun(arg):
    # time.sleep(1)
    print(arg)
    return arg

def run():
    os.system('docker run --rm -v $PWD/scripts:/scripts -it dbitz/argos-cpfa:v1 bash \
    -c "python3 /scripts/runner.py \
    -ProbabilityOfSwitchingToSearching 0.40 \
    -ProbabilityOfReturningToNest 0.02 \
    -UninformedSearchVariation 6.0 \
    -RateOfInformedSearchDecay 0.58 \
    -RateOfSiteFidelity 4.0 \
    -RateOfLayingPheromone 3.5 \
    -RateOfPheromoneDecay 0.08 \
    -FoodDistribution 0 \
    -PrintFinalScore 1"')
# We want 50 threads in the pool
pool = ThreadPoolExecutor(12)
 
i = 0
for my_message in messages:
    i+=1
    # print(i)
    future = pool.submit(run)