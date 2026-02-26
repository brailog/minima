from minima.engine.context import current_session


class Browser:
    """
    High-level interface for browser-level actions.
    Can dynamically fetch the current session from contextvars, or use an
    explicitly provided session/controller.
    """

    @classmethod
    def _get_active_session(cls, session_override: object | None = None):
        """
        Determines which session to use: the explicit override or the contextvar.
        """
        if session_override is not None:
            return session_override

        try:
            # Assuming current_session is imported from your context module
            return current_session.get()
        except LookupError:
            raise RuntimeError(
                "No active browser session found in context, and no session was explicitly passed. "
                "Make sure you are running inside the @browser_session decorator or "
                "pass the session instance directly to the method."
            )

    @classmethod
    def open_url(cls, url: str, session: object | None = None) -> None:
        cls._get_active_session(session).open_url(url)

    @classmethod
    def accept_alert(cls, timeout: int = 5, session: object | None = None) -> None:
        cls._get_active_session(session).accept_alert(timeout)

    @classmethod
    def switch_to_new_tab(cls, session: object | None = None) -> None:
        cls._get_active_session(session).switch_to_new_tab()

    @classmethod
    def switch_to_original_tab(cls, session: object | None = None) -> None:
        cls._get_active_session(session).switch_to_original_tab()

    @classmethod
    def close_current_tab(cls, session: object | None = None) -> None:
        cls._get_active_session(session).close_current_tab()

    @classmethod
    def close_browser(cls, session: object | None = None) -> None:
        cls._get_active_session(session).close_browser()
