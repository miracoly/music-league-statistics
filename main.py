from functional import seq
from tap import Tap

from src.console import print_lvl_1, print_lvl_2, print_lvl_3
from src.league import get_leagues_of
from src.player import get_me
from src.statistic import write_to_csv, get_statistic_of_league


class SimpleArgumentParser(Tap):
    session: str  # Your session ID which is used for every request to music league. You find it in the cookie header. Use double quotes or no quotes at all.
    output: str = "statistics.csv"  # Specify filename of CSV output.


def main():
    args = SimpleArgumentParser(description="Fetches all leagues of user and creates statistics.").parse_args()

    print_lvl_1("Fetching infos about me...")
    me = get_me(args.session)
    print_lvl_2(f"my user id: {me.id}")
    print_lvl_2(f"my user name: {me.name}")

    print_lvl_1("Fetching leagues...")
    leagues = get_leagues_of(me.id, args.session)
    print_lvl_2(f"leagues found: {len(leagues)}")
    seq(leagues).for_each(lambda l: print_lvl_3(f"* {l.name}"))

    print_lvl_1("Fetching details...")
    statistics = seq(leagues) \
        .flat_map(lambda l: get_statistic_of_league(l, args.session)) \
        .list()

    print_lvl_1("Write to Output...")
    write_to_csv(statistics, args.output)
    print_lvl_2(f"statistics written to {args.output}")

    print_lvl_1("Success.")


if __name__ == '__main__':
    main()
