import sys
from datetime import datetime, timedelta, timezone
from math import ceil

# Hardcoding the date of the season end in a constant : 13/06/2023 at 20:00 UTC+2
SEASON_END = datetime(2023, 6, 13, 20, 0, 0).replace(tzinfo=timezone(timedelta(hours=2))).astimezone(timezone.utc)
print(f"Season end date : {SEASON_END.year}-{SEASON_END.month}-{SEASON_END.day} {SEASON_END.hour}:{SEASON_END.minute}:{SEASON_END.second} UTC")


def calc(initial: int, coins_earned_this_week: int):
    """
    In one week, one can earn 60 coins. Weeks start on Tuesday at 20:00. This function calculates how many coins one
    can have by the end of "days_left" days, starting with "initial" coins and assuming one earned 60 coins per week,
    starting at current date and time, and assuming this week's earnings are "coins_earned_this_week"

    :param initial: the number of coins one has right now, includes coins already earned this week
    :param coins_earned_this_week: the number of coins one has earned this week
    :return: the number of total coins one can have by the end of "days_left" days, starting with "initial" coins and
             assuming one earned 60 coins per week, starting at current date and time.
    """
    now = datetime.now().replace(tzinfo=timezone.utc)
    print(f"Current date : {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second} UTC")

    days_until_tuesday = 2 - now.weekday()
    if days_until_tuesday < 0:
        days_until_tuesday += 7

    if now.weekday() == 2 and now.hour >= 20:
        days_until_tuesday = 0

    weeks_left = ceil((SEASON_END - now - timedelta(days=days_until_tuesday)).days / 7)

    coins_by_season_end = initial + weeks_left * 60 + (60 - coins_earned_this_week)

    return coins_by_season_end


if __name__ == '__main__':
    bold_and_green = lambda x: f"\033[1;32m{x}\033[0m"
    try:
        init = int(sys.argv[1])
        already_earned = int(sys.argv[2])
        result = calc(init, already_earned)
        print()
        print(f"Unless I fucked up, "
              f"\n\tby the end of {bold_and_green('season 4')}, and "
              f"\n\t\tassuming you gain {bold_and_green('60 coins every week')}, you'll have :" 
              f"\n\t\t\t{bold_and_green(str(result) + ' coins')}")

    except IndexError as e:
        print("Please provide your current total amount of premium coins and the number of coins you won during the "
              "current week as integers (input 0 if none)")
        # outputting error message to stderr
        print(e, file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print("Please provide your current total amount of premium coins and the number of coins you won during the "
              "current week as integers (input 0 if none)")
        # outputting error message to stderr
        print(e, file=sys.stderr)
        sys.exit(1)
