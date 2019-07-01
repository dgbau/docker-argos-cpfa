#!/usr/bin/env python3
import os, argparse, datetime
import xml.etree.ElementTree as ET

# Set argument parameters
parser = argparse.ArgumentParser()
parser.add_argument("-ProbabilityOfSwitchingToSearching", help="Probability Of Switching To Searching", type=float)
parser.add_argument("-ProbabilityOfReturningToNest", help="Probability Of Returning To Nest", type=float)
parser.add_argument("-UninformedSearchVariation", help="Uninformed Search Variation", type=float)
parser.add_argument("-RateOfInformedSearchDecay", help="Rate Of Informed Search Decay", type=float)
parser.add_argument("-RateOfSiteFidelity", help="Rate Of Site Fidelity", type=float)
parser.add_argument("-RateOfLayingPheromone", help="Rate Of Laying Pheromone", type=float)
parser.add_argument("-RateOfPheromoneDecay", help="Rate Of Pheromone Decay", type=float)
parser.add_argument("-PrintFinalScore", help="Print Final Score", type=int)
parser.add_argument("-FoodDistribution", help="Food Distribution", type=int)
args = parser.parse_args()

# Copy example XML file to temp 
os.system('cp /CPFA-ARGoS/experiments/CPFAExample.xml /CPFA-ARGoS/experiments/CPFARunner.xml')

# Read and parse XML, extract needed experiment constants
tree = ET.parse('/CPFA-ARGoS/experiments/CPFARunner.xml')
root = tree.getroot()
cpfa_params = root.find('loop_functions').find('CPFA')
cpfa_settings = root.find('loop_functions').find('settings')
foodCount = int(root.find('loop_functions').find('settings').attrib['FoodItemCount'])
maxSimTime = int(root.find('loop_functions').find('settings').attrib['MaxSimTimeInSeconds'])

# Set args in XML foe and rewrite
for arg in vars(args):
    print("{} {}".format(arg, getattr(args, arg)))
    cpfa_params.set(arg, str(getattr(args, arg)))
    if (arg == 'FoodDistribution'): 
        cpfa_settings.set(arg, str(getattr(args, arg)))
tree.write('/CPFA-ARGoS/experiments/CPFARunner.xml')

# Exectute Argos Experiment and write output to temp file
os.system("argos3 --config-file experiments/CPFARunner.xml >> /scripts/temp_out")

# Read output file, extract score and remove file
score = 0
filepath = '/scripts/temp_out' 
with open(filepath) as fp:  
   line = fp.readline()
   line = line.strip()
   while line:
       if str(maxSimTime) in line:
           score = float(line.split(',')[1].strip())
           break
       line = fp.readline()
os.remove(fp.name)

# Print score and score/foodCount to stdout, write score to file
print(score, score/foodCount)
f = open("/scripts/score_{}.txt".format(datetime.datetime.now().microsecond), "w")
f.write("{}\n".format(str(score)))
f.write("{}\n".format(str(score/foodCount)))
for arg in vars(args):
    f.write("{}, {}\n".format(arg, getattr(args, arg)))
f.close()
