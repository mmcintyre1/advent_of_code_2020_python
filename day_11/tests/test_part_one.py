from textwrap import dedent

from day_11.part_one import plane_parser


def test_plane_shuffler():
    seat_data = dedent("""
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """).strip()
    plane = plane_parser(seat_data)
    while not plane.boarded:
        plane.board_plane()
        print(plane)
    assert plane.get_occupied_seats() == 37
