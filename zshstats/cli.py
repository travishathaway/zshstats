import click
import rich as r
from rich.columns import Columns
from zshstats import filters as f
from zshstats import formatters as fmt
from zshstats import parsers as p
from zshstats import reducers as red
from zshstats.data import read_zsh_history_lines


@click.command()
def main():
    rows = tuple(
        p.parse_rows(
            f.filter_valid_rows(
                read_zsh_history_lines()
            )
        )
    )

    limit = 10

    nrml_cmds = '\n'.join(
        tuple(
            fmt.format_leading_number(
                red.count_cmds(
                    f.filter_not_sudo(rows),
                    cmd_key='cmd'
                )
            )
        )[0:limit]
    )

    sudo_cmds = '\n'.join(
        tuple(
            fmt.format_leading_number(
                red.count_cmds(
                    f.filter_sudo(rows),
                    cmd_key='sudo_cmd'
                )
            )
        )[0:limit]
    )

    sudo_cmds = f'Top {limit} sudo commands\n' + sudo_cmds
    nrml_cmds = f'Top {limit} commands\n' + nrml_cmds

    r.print(Columns((nrml_cmds, sudo_cmds), equal=True, expand=True))


if __name__ == '__main__':
    main()
