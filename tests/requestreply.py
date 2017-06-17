# -*- coding: utf-8 -*-

from unittest import TestCase, TestLoader

from radio import (Radio, ListenerNotFound, ReplyHandlerAlreadyBound,
                   HandlerAlreadyBound)


def init_radio(f):

    def wrap(self, *args):
        self.radio = Radio()
        return f(self, *args)

    return wrap


class TestRadioRequestReplyMethods(TestCase):

    @init_radio
    def test_request_reply_stop_replying(self):
        '''
        "request", "reply" and "stopReplying" methods work correctly.
        '''

        def foo_handler(): return 'foo'
        def bar_handler(my_arg=222): return my_arg

        self.radio.reply('foo', foo_handler)
        self.radio.reply('bar', bar_handler)
        self.assertEqual(self.radio.request('foo'), 'foo')
        self.assertEqual(self.radio.request('bar'), 222)
        self.assertEqual(self.radio.request('bar', 333), 333)
        self.assertEqual(self.radio.request('bar', my_arg=444), 444)
        self.radio.stopReplying('foo')
        self.radio.stopReplying('bar')

        with self.assertRaises(ListenerNotFound):
            self.radio.request('foo')
        with self.assertRaises(ListenerNotFound):
            self.radio.request('bar')

    @init_radio
    def test_kwargs(self):
        '''
        Keyword arguments works correctly.
        '''

        foo_list = []
        def foo_handler(foo, bar): return (foo, bar)
        self.radio.reply('foo', foo_handler)
        self.assertEqual(self.radio.request('foo', bar=5, foo=10), (10, 5))

    @init_radio
    def test_on_already_bound(self):
        '''
        "reply" fails when trying to bound handler that is already bounded.
        '''

        def foo_handler(): pass
        self.radio.reply('foo', foo_handler)
        self.radio.reply('bar', foo_handler)

        # General exception
        with self.assertRaises(HandlerAlreadyBound):
            self.radio.reply('foo', foo_handler)
        # Child exception
        with self.assertRaises(ReplyHandlerAlreadyBound):
            self.radio.reply('foo', foo_handler)

    @init_radio
    def test_off_handler_that_was_not_bounded(self):
        '''
        "stopReplying" fails when trying to unbound handler that was not
        bounded.
        '''

        def foo_handler(): pass

        with self.assertRaises(ListenerNotFound):
            self.radio.stopReplying('foo', foo_handler)

    @init_radio
    def test_off_soft_mode(self):
        '''
        "stopReplying" will not fail if safe-argument is set to True.
        '''

        def foo_handler(): pass
        self.radio.stopReplying('foo', foo_handler, soft=True)
        self.radio.stopReplying('foo', foo_handler, soft=True)

    @init_radio
    def test_trigger_fail_on_incorrect_arguments(self):
        '''
        "request" fails when arguments for handler is incorrect.
        '''

        def foo_handler(required_arg): pass
        self.radio.reply('foo', foo_handler)

        with self.assertRaises(TypeError):
            self.radio.request('foo')


suite = TestLoader().loadTestsFromTestCase(TestRadioRequestReplyMethods)
