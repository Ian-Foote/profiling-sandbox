import sys


def install_profiler():
    def profiler(frame, event, arg):
        if frame.f_code.co_name == "add":
            print(frame)

    sys.setprofile(profiler)
