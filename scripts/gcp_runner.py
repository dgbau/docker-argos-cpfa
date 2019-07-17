import os, argparse, datetime, random
import xml.etree.ElementTree as ET

def run_trial(args):
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
        # print("{} {}".format(arg, getattr(args, arg)))
        cpfa_params.set(arg, str(getattr(args, arg)))
        if (arg == 'FoodDistribution'): 
            if (args.randomFoodDist == 1):  
                # print('randomizing food distribution')              
                cpfa_settings.set(arg, str(random.randint(0, 2)))
            else:
                cpfa_settings.set(arg, str(getattr(args, arg)))
            print('food distribution {}'.format(cpfa_settings.attrib[arg]))

    tree.write('/CPFA-ARGoS/experiments/CPFARunner.xml')

    # Exectute Argos Experiment and write output to temp file
    os.system("argos3 --config-file experiments/CPFARunner.xml >> /root/scripts/temp_out")

    # Read output file, extract score and remove file
    score = 0
    filepath = '/root/scripts/temp_out' 
    with open(filepath) as fp:  
        line = fp.readline()
        line = line.strip()
        while line:
            if str(maxSimTime) in line:
                score = float(line.split(',')[1].strip())
                break
            line = fp.readline()
    os.remove(fp.name)

    # print(score, score/foodCount)
    return(score/foodCount)
