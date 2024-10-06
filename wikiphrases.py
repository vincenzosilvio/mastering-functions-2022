#!/usr/bin/env python

import fire
from nlplogic.corenlp import get_phrases

# Da terminale dovrò inserire --nome_argomento
if __name__ == "__main__":
    fire.Fire(get_phrases)
