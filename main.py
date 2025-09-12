import rig_manager as rm

manager = rm.RigManager(
        config_path=input('Enter path to the rig config file: ')
    )

COMMANDS = {
    'L': manager.launch,
    'N': lambda: manager.set_ncores(n=int(input('Enter desired number of cores to use: '))),
    'S': manager.stop
}


def main():
    while True:
        command = input(
            'Enter command:' \
            '\nL - [L]aunch the rig' \
            '\nN - Adjust the [N]umber of active cores' \
            '\nS - [S]top the rig' \
            '\n>>> '
        )
        if not command:
            break
        COMMANDS.get(command, lambda: print('Bad command!'))()


if __name__ == '__main__':
    main()