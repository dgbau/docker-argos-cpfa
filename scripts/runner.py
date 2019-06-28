#!/usr/bin/env python3
import os, argparse
import xml.etree.ElementTree as ET
os.system("echo hello from the task runner")
parser = argparse.ArgumentParser()
parser.add_argument("-ProbabilityOfSwitchingToSearching", help="Probability Of Switching To Searching", type=float)
parser.add_argument("-ProbabilityOfReturningToNest", help="Probability Of Returning To Nest", type=float)
parser.add_argument("-UninformedSearchVariation", help="Uninformed Search Variation", type=float)
parser.add_argument("-RateOfInformedSearchDecay", help="Rate Of Informed Search Decay", type=float)
parser.add_argument("-RateOfSiteFidelity", help="Rate Of Site Fidelity", type=float)
parser.add_argument("-RateOfLayingPheromone", help="Rate Of Laying Pheromone", type=float)
parser.add_argument("-RateOfPheromoneDecay", help="Rate Of Pheromone Decay", type=float)
parser.add_argument("-PrintFinalScore", help="Print Final Score", type=int)
args = parser.parse_args()
os.system('cp CPFA-ARGoS/experiments/CPFAExample.xml CPFA-ARGoS/experiments/CPFARunner.xml')
config = ET.parse('CPFA-ARGoS/experiments/CPFARunner.xml')
root = config.getroot()
cpfa_params = root.find('loop_functions').find('CPFA').attrib
print(cpfa_params)
for idx, item in enumerate(cpfa_params):
    print(idx, item, cpfa_params[item])
    print('cpfa', list(cpfa_params)[idx])
    print('args', list(vars(args))[idx], getattr(args, list(cpfa_params)[idx]))
    list(cpfa_params)[idx] = getattr(args, list(cpfa_params)[idx])
    print('cpfa-new', list(cpfa_params)[idx], cpfa_params[list(cpfa_params)[idx]])
    
for idx, arg in enumerate(vars(args)):
    print(idx, arg, getattr(args, arg))
config.write('CPFA-ARGoS/experiments/CPFARunner_temp.xml')
os.system('ls CPFA-ARGoS/experiments')
os.system('cat CPFA-ARGoS/experiments/CPFARunner_temp.xml')
os.system("cd CPFA-ARGoS && pwd && argos3 --config-file experiments/CPFARunner_temp.xml")
