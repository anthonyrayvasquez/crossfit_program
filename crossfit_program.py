import random
#Lists of all applicable data
weeks = [1,2,3]
days = [1,2,3,4,5,6,7]
modality_combinations = ['M','GW','MGW','MG','W','G','WM']
gymnastics_exercises = ['Air Squat','Pull Up','Push Up', 'Dip', 'Handstand Push Up','Rope Climb',
'Muscle Up', 'Sit Up', 'Box Jump', 'Burpee', 'Lunges']
metabolic_conditioning_exercises = ['Run', 'Bike', 'Row', 'Jump Rope']
weightlifting_exercises = ['Deadlifts','Cleans','Overhead Press','Push Press','Bench Press',
'Snatch','Clean and Jerk','Kettlebell Swing','Front Squat','Back Squat']

set_structures = {'Time':[10,12,15,20,25,30,45] ,
'Rounds':[3,4,5]}
reps = list(range(3,30,3))
#function to determine what modality/modality combo depending on the week and day

def get_modality(week, day):
    if week == 1:
        modality_combo = dict(zip(days[0:5],modality_combinations[0:5]))
    elif week == 2:
        modality_combo = dict(zip(days[0:5], modality_combinations[5:7]+modality_combinations[2::-1]))
    elif week == 3:
        modality_combo = dict(zip(days[0:5], modality_combinations[4:1:-1] + modality_combinations[6:4:-1]))
    modality = modality_combo.get(day)
    return modality

#function to generate a random execise depending on the modality
def get_exercise(modality):
    if modality == 'M':
        exercise = random.choice(metabolic_conditioning_exercises)
    elif modality == 'G':
        exercise = random.choice(gymnastics_exercises)
    elif modality == 'W':
        exercise = random.choice(weightlifting_exercises)
    elif modality == 'MG':
        exercise = random.choice(weightlifting_exercises) + ' ' + random.choice(gymnastics_exercises)
    elif modality == 'GW':
        exercise = random.choice(gymnastics_exercises) + ' ' + random.choice(weightlifting_exercises)
    elif modality == 'WM':
        exercise = random.choice(weightlifting_exercises) + ' ' + random.choice(metabolic_conditioning_exercises)
    elif modality == 'MGW':
        exercise = random.choice(weightlifting_exercises) + ' ' + random.choice(gymnastics_exercises) + ' ' + random.choice(metabolic_conditioning_exercises)
    return exercise

#don't forget the G case
def get_set_structure(modality):
    if modality == 'M':
        set_structure = random.choice([30,35,40,45,50,55,60])
    elif modality == 'W':
        set_structure = [random.choice(range(1,6)), random.choice(range(1,6))]
    elif modality == 'G':
        set_structure = 'Spend some time practicing for 45 minutes'
    elif modality == 'MG' or modality == 'GW' or modality == 'WM':
        set_structure = random.choice(set_structures['Rounds'])
    elif modality == 'MGW':
        set_structure = random.choice(set_structures['Time'])
    return set_structure

week = int(input('What week are you on? '))
day = int(input('What day are you on? '))

modality = get_modality(week, day)
exercise = get_exercise(modality)
set_structure = get_set_structure(modality)

def get_WOD(modality, set_structure):
    if modality == 'M':
        print('The Workout of the Day is: {time} minute {exercise}'.format(time=set_structure, exercise=exercise))
    elif modality == 'W':
        print('The Workout of the Day is: {sets}x{reps} {exercise}'.format(sets = set_structure[0], reps = set_structure[1], exercise = exercise))
    elif modality == 'G':
        print('The Workout of the Day is: {exercise}. {set_structure}'.format(exercise = exercise, set_structure=set_structure))
    #elif modality == 'MG' or modality == 'GW' or modality == 'WM':
        #print('The Workout of the Day is: {rounds} rounds for time of {reps} {exercise}, {reps} {exercise}')
get_WOD(modality, set_structure)
