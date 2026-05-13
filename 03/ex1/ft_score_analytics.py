import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score_list: list[int] = list()
    for i in range(1, len(sys.argv)):
        try:
            score_list.append(int(sys.argv[i]))
        except ValueError:
            print("Invalid parameter:", f"'{sys.argv[i]}'")
    if len(score_list) == 0:
        print("No scores provided.",
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print("Scores processed:", score_list)
    print("Total players:", len(score_list))
    print("Total score:", sum(score_list))
    print("Average score:", round((sum(score_list)/len(score_list)), 1))
    print("High score:", max(score_list))
    print("Low score:", min(score_list))
    print("Score range:", max(score_list) - min(score_list))
    return


if __name__ == '__main__':
    main()
