import os
import sys
from multiprocessing import Pool, cpu_count

inertia_default = 0.5
particle_default = 40
cognition_default = 1
social_default = 1

def part():
    for particle in range(10,101,10):
        for i in range(20):
            command = f"python3 pso.py --num_particles {particle} --inertia {inertia_default} --cognition {cognition_default} --social {social_default} --gen {i}"
            os.system(command)

def inert():
    for inertia in range(1, 11):
        dec_inertia = inertia/10
        if dec_inertia == inertia_default:
            continue
        for i in range(20):
            command = f"python3 pso.py --num_particles {particle_default} --inertia {dec_inertia} --cognition {cognition_default} --social {social_default} --gen {i}"
            os.system(command)

def run_set(cognition):
    dec_cog = cognition/10
    for social in range(1, 41):
        dec_social = social/10
        if dec_social == social_default and dec_cog == cognition_default:
            continue
        for i in range(20):
            command = f"python3 pso.py --num_particles {particle_default} --inertia {inertia_default} --cognition {dec_cog} --social {dec_social} --gen {i}"
            os.system(command)

    return cognition

if __name__ == "__main__":
    cognitions = [i for i in range(1,41)]
    with Pool(cpu_count()) as p:
        print(p.map(run_set, cognitions))
