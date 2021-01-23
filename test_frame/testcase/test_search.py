from test_frame.app import App


def test_search():
    app = App()
    resutl = app.start().goto_main().goto_market_page().goto_search().search()
    assert resutl == True