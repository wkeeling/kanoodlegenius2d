from unittest import TestCase

from kanoodlegenius2d.ui.selectplayerscreen import PlayerPaginator


class PlayerPaginationTest(TestCase):

    def setUp(self):
        self._players = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6']
        self._paginator = PlayerPaginator(self._players, page_size=2)

    def test_get_first_page(self):
        self.assertEqual(self._paginator.players(), ['player1', 'player2'])

    def test_get_second_page(self):
        self._paginator.next_page()
        self.assertEqual(self._paginator.players(), ['player3', 'player4'])

    def test_get_third_page(self):
        self._paginator.next_page()
        self._paginator.next_page()
        self.assertEqual(self._paginator.players(), ['player5', 'player6'])

    def test_has_next_page(self):
        self.assertTrue(self._paginator.has_next_page())
        self._players.remove('player6')
        self._paginator.next_page()
        self.assertTrue(self._paginator.has_next_page())

    def test_does_not_have_next_page(self):
        self._paginator.next_page()
        self._paginator.next_page()
        self.assertFalse(self._paginator.has_next_page())

    def test_get_prev_page(self):
        self._paginator.next_page()
        self._paginator.next_page()
        self._paginator.prev_page()
        self.assertEqual(self._paginator.players(), ['player3', 'player4'])

    def test_has_prev_page(self):
        self._paginator.next_page()
        self.assertTrue(self._paginator.has_prev_page())

    def test_does_not_have_prev_page(self):
        self.assertFalse(self._paginator.has_prev_page())

    def test_pagination_after_player_removal(self):
        self._paginator.next_page()  # Now on page 2
        self._paginator.remove('player3')
        self.assertEqual(self._paginator.players(), ['player4', 'player5'])

    def test_pagination_after_page_removal(self):
        self._paginator.next_page()  # Now on page 2
        self._paginator.remove('player3')
        self._paginator.remove('player4')
        self._paginator.remove('player5')
        self._paginator.remove('player6')
        self.assertEqual(self._paginator.players(), ['player1', 'player2'])

    def test_has_next_page_after_page_removal(self):
        self._paginator.remove('player3')
        self._paginator.remove('player4')
        self._paginator.remove('player5')
        self._paginator.remove('player6')
        self.assertFalse(self._paginator.has_next_page())

    def test_does_not_paginate_below_page_1(self):
        self._paginator.prev_page()
        self.assertEqual(self._paginator.players(), ['player1', 'player2'])

    def test_does_not_paginate_above_max_pages(self):
        self._paginator.next_page()
        self._paginator.next_page()
        self._paginator.next_page()
        self.assertEqual(self._paginator.players(), ['player5', 'player6'])
