import rig_manager as rm

manager = rm.RigManager(
        working_dir=input('Enter path to the rig directory, bare Enter to reuse from previous session: ')
    )

COMMANDS = {
    'L': manager.launch,
    'N': lambda: manager.set_ncores(n=int(input('Enter desired number of cores to use: '))),
    'S': manager.stop,
    'T': manager.get_stats
}


def main():
    while True:
        command = input(
            'Enter command, bare Enter to quit:' \
            '\nL - [L]aunch the rig' \
            '\nN - Adjust the [N]umber of active cores' \
            '\nT - View mining s[T]ats' \
            '\nS - [S]top the rig' \
            '\n>>> '
        )
        if not command:
            break
        COMMANDS.get(command, lambda: print('Bad command!'))()


if __name__ == '__main__':
    main()