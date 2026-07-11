from threading import Lock


class DerivOAuthStorage:

    def __init__(self):

        self._lock = Lock()

        self._sessions: dict[str, dict] = {}

    # =====================================================
    # GUARDAR
    # =====================================================

    def save(

        self,

        state: str,

        code_verifier: str,

        code_challenge: str,

    ):

        with self._lock:

            self._sessions[state] = {

                "code_verifier": code_verifier,

                "code_challenge": code_challenge,

            }

    # =====================================================
    # OBTENER
    # =====================================================

    def get(self, state: str):

        with self._lock:

            return self._sessions.get(state)

    # =====================================================
    # ELIMINAR
    # =====================================================

    def remove(self, state: str):

        with self._lock:

            return self._sessions.pop(state, None)

    # =====================================================
    # EXISTE
    # =====================================================

    def exists(self, state: str):

        with self._lock:

            return state in self._sessions

    # =====================================================
    # LIMPIAR
    # =====================================================

    def clear(self):

        with self._lock:

            self._sessions.clear()

    # =====================================================
    # CANTIDAD
    # =====================================================

    def count(self):

        with self._lock:

            return len(self._sessions)

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        with self._lock:

            return {

                "sessions": len(self._sessions),

                "states": list(self._sessions.keys()),

            }


# =====================================================
# INSTANCIA GLOBAL
# =====================================================

storage = DerivOAuthStorage()