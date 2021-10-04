import tkinter as tk
#from gui import values
import os
def run_sim(values):
    new_line_chars = {'Linux' : '\n','MacOSX' : '\n', 'Windows' : '\r\n'}

    from sys import platform
    if platform == "linux" or platform == "linux2":
        nl = new_line_chars['Linux']
        print('Working on Linux')
    elif platform == "darwin":
        nl = new_line_chars['MacOSX']
        print('Working on Darwin')
    elif platform == "win32":
        nl = new_line_chars['Windows']
        print('Working on Windows')

    # For showing message errors 
    def open_dialog(error_str):
        root = tk.Tk()
        # Background canvas
        canvas = tk.Canvas(root, height=100, width=300, bg='white')
        canvas.pack()

        # White centered frame
        frame = tk.Frame(root, bg='white')
        frame.place(relwidth=1, relheight=1, relx=0., rely=0.)

        text = error_str + ' is not specified correctly'
        label = tk.Label(frame, text=text, bg='white')
        label.pack()

        root.mainloop()


    # What to do when there is an error
    def when_error():
        exit()


    DICT = values
    #for i in [*DICT]:
     #   new_val = str(DICT[i])
      #  DICT[i] = new_val
    print(DICT)
    # Check that the important things are stated
    mandatory_params = [*DICT]
    mandatory_params.remove('Neighbor')
    mandatory_params.remove('Modify neighbor list')

    for i in mandatory_params:
        if len(str(DICT[i]).strip()) == 0:
            if __name__ == "__main__":
                open_dialog(i)
            when_error()

    # Now let's write the input file for lammps
    in_file = open('in.sim', 'w')

    # (1) SYSTEM INITIALIZATION
    # Some fundamental properties of the script
    DIMS = DICT['Dimension']
    UNITS = DICT['Units']
    BOUNDS = DICT['Boundary']
    ATOM_STYLE = DICT['Atom style']

    init_line = '# System Initialization'
    init_line += 'units ' + UNITS + nl + 'dimension ' + DIMS + nl +\
                'boundary ' + BOUNDS + nl + 'atom_style ' + ATOM_STYLE + nl

    # Now let's write the init section of the script
    init_line += nl+nl # For easy reading...
    in_file.write(init_line)


    # (2) SYSTEM DEFINITION
    # Necessary definition terms
    LATTICE = DICT['Lattice']
    LATT_PARAM = DICT['Lattice parameter']
    REGION_X = [DICT['Region x min'], DICT['Region x max']]
    REGION_Y = [DICT['Region y min'], DICT['Region y max']]
    REGION_Z = [DICT['Region z min'], DICT['Region z max']]

    THERMO = str(int(DICT['Steps'])//10)

    def_line = '# System Definition' + nl
    def_line += 'lattice ' + LATTICE + ' ' + LATT_PARAM + nl +\
                'region box block ' + REGION_X[0] + ' ' + REGION_X[1] +\
                ' ' + REGION_Y[0] + ' ' + REGION_Y[1] +\
                ' ' + REGION_Z[0] + ' ' + REGION_Z[1] + nl +\
                'create_box 1 box' + nl +\
                'create_atoms 1 box' + nl 

    def_line += 'thermo ' + THERMO + nl

    # Now let's write system settings section of the script
    def_line += nl+nl # For easy reading...
    in_file.write(def_line)

    # (3) SIMULATION SETTINGS
    PAIR_STYLE = DICT['Pair style']
    PAIR_COEFF = DICT['Pair coefficients']
    MASS = DICT['Mass']

    simset_line = '# Simulation Settings' + nl
    simset_line += 'pair_style ' + PAIR_STYLE + nl +\
                'pair_coeff 1 1 ' + PAIR_COEFF + nl +\
                'mass 1 ' + MASS + nl

    # Check for neighbors and modify neighbors commands
    NEIGH = DICT['Neighbor']
    NEIGH_MOD = DICT['Modify neighbor list']

    if not len(NEIGH.strip()) == '':
        simset_line += 'neighbor ' + NEIGH + ' bin' + nl 
    if not len(NEIGH_MOD.strip()) == '':
        params = str(NEIGH_MOD).split(',')
        if not len(params) == 2:
            if __name__ == "__main__":
                open_dialog('Modify neighbor list')
            when_error()
        else:
            simset_line += 'neigh_modify every ' + params[0] + ' delay ' + params[1] + ' check yes' + nl

    # Now let's write simulation settings section of the script
    simset_line += nl+nl # For easy reading...
    in_file.write(simset_line)



    # (4) Run settings
    # Mandatory minimization for now: minimize 1.0e-4 1.0e-6 1000 10000
    #MINIMIZATION = 'minimize 1.0e-4 1.0e-6 1000 10000' + nl
    #MINIMIZATION += 'min_style fire' + nl
    #MINIMIZATION += 'minimize 1.0e-7 1.0e-8 5000 10000'
    MINIMIZATION = ''
    # Velocity command: velocity all create 300.0 4928459 rot yes dist gaussian mom yes 
    TEMPERATURE = DICT['Temperature']
    VEL_COMMAND = 'velocity all create ' + TEMPERATURE + ' 4928459 rot yes dist gaussian mom yes'
    FIX = DICT['Fix']
    TIME_STEP = DICT['Time step']
    STEPS = DICT['Steps']

    run_line = '# Run' + nl
    run_line += MINIMIZATION + nl +\
                VEL_COMMAND + nl +\
                'fix 1 all ' + FIX + nl +\
                'timestep ' + TIME_STEP + nl +\
                'run ' + STEPS + nl

    # Now let's write simulation run section of the script
    run_line += nl+nl # For easy reading...
    in_file.write(run_line)


    in_file.close()


    # Run lammps exec
    os.system('lmp_serial -in in.sim')