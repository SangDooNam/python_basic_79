#!/usr/bin/env python

from cleaning_robot import CleaningRobot


def main():
    test_failed = False
    # TODO - initiate cleaning robot and test what happens when it encounters
    # an inner door, the main door or a prison guard. Then modify cleaning_robot.py
    # so that it works accordingly.
    mode_activating = CleaningRobot(testing_mode=True)
    inner_door = mode_activating.when_encounter_inner_door()
    outer_door = mode_activating.when_encounter_outer_door()
    prison_guards = mode_activating.when_encounter_guard()

    if (
        ("Door unlocked." in inner_door and "Door entered." in inner_door)
        and not "Turn around." in inner_door
        and not "Door locked." in inner_door
    ):
        test_failed
    else:
        test_failed = True

    if (
        ("Door unlocked." in outer_door and "Turn around." in outer_door)
        and not "Door entered." in outer_door
        and not "Door locked." in outer_door
    ):
        test_failed
    else:
        test_failed = True

    if len(prison_guards):
        test_failed = True

    if test_failed:
        print("Unfortunately, one or several tests failed.")
    else:
        print("All tests ran successfully.")


if __name__ == "__main__":
    main()



