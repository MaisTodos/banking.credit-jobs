from pathlib import Path

import i18n


def init_i18n_translator(path_translator: Path):
    i18n.set("file_format", "json")
    i18n.set("locale", "pt_BR")
    i18n.load_path.append(path_translator)
