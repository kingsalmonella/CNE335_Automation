import Server


def print_program_info():

    print("Server Automator v0.1 by Jack")

if __name__ == '__main__':

    print_program_info()

    server = Server.Server('3.17.179.81')

    print(server.ping())




